#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import tomllib
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_URL = "https://raw.githubusercontent.com/tsukuyomi-luna/lunatic-craft2/main/pack.toml"
BOOTSTRAP_URL = "https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar"
BOOTSTRAP_SHA256 = "a8fbb24dc604278e97f4688e82d3d91a318b98efc08d5dbfcbcbcab6443d116c"


def main() -> None:
    pack = tomllib.loads((ROOT / "pack.toml").read_text(encoding="utf-8"))
    name = pack["name"]
    out = ROOT / "build" / f"lunatic-craft2-{pack['version']}-prism.zip"
    out.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        minecraft = temp / "minecraft"
        minecraft.mkdir()
        bootstrap = minecraft / "packwiz-installer-bootstrap.jar"
        urllib.request.urlretrieve(BOOTSTRAP_URL, bootstrap)
        actual = hashlib.sha256(bootstrap.read_bytes()).hexdigest()
        if actual != BOOTSTRAP_SHA256:
            raise SystemExit(f"bootstrap checksum mismatch: {actual}")
        (temp / "instance.cfg").write_text(
            "[General]\n"
            f"name={name}\n"
            "InstanceType=OneSix\n"
            "OverrideCommands=true\n"
            f'PreLaunchCommand="$INST_JAVA" -jar packwiz-installer-bootstrap.jar {PACK_URL}\n'
            "OverrideMemory=true\n"
            "MinMemAlloc=4096\n"
            "MaxMemAlloc=8192\n"
            f"iconKey={name}\n",
            encoding="utf-8",
        )
        versions = pack["versions"]
        (temp / "mmc-pack.json").write_text(
            json.dumps(
                {
                    "formatVersion": 1,
                    "components": [
                        {"uid": "net.minecraft", "version": versions["minecraft"], "important": True},
                        {"uid": "net.neoforged", "version": versions["neoforge"]},
                    ],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        shutil.copy2(ROOT / "icon.png", temp / f"{name}.png")
        out.unlink(missing_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(temp.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(temp))
    print(out)


if __name__ == "__main__":
    main()
