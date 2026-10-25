# Lunatic Craft 2

Create と Create Aeronautics を中心に、バニラの遊びを残した Minecraft 1.21.1 / NeoForge 向けの modpack です。工業は Create とそのアドオンだけ、敵の強さはバニラのままにして、MOD に慣れていない人でも追いつけることを目指します

## バージョン

- Minecraft 1.21.1
- NeoForge 21.1.264
- Java 21

## 導入

Prism Launcher 用の zip を [Releases](https://github.com/tsukuyomi-luna/lunatic-craft2/releases/latest) から取得し、`インスタンスを追加 → zipからインポート` で読み込んでください。以後は起動前に packwiz-installer が差分を同期します

詳しくは [クライアント導入ガイド](docs/INSTALL.md) を参照してください

## 構成

- Create — Create、Create Aeronautics（Sable）、Big Cannons、Enchantment Industry、Numismatics、Trading Floor ほか乗り物・物流・装飾のアドオン
- 魔術 — Iron's Spells 'n Spellbooks
- 探索 — Terralith、Tectonic、YUNG's Better 系、IDAS、Integrated Villages / Stronghold
- 生活・建築 — Farmer's Delight、Supplementaries、Quark、Macaw's 系、Handcrafted
- マルチ — FTB Chunks / Teams（地図と土地保護）、FTB Chunks: Sable Aerospace（保護を乗り物にも適用）、Waystones、Simple Discord Link

初回参加時に渡すガイド本（Patchouli）の中身は `patchouli_books/lunatic_guide/` にあります。完全な一覧は `mods/` を参照してください

## サーバー

構築と更新の手順は [サーバー運用ガイド](docs/SERVER.md) を参照してください

## 開発

packwiz は mise で固定しています

```bash
mise install
mise exec -- packwiz refresh
```

MOD は 1.21.1 の NeoForge 版のうち、リリース版があればその最新、なければベータの最新を入れます（アルファは使いません）

配布用 zip は `python3 scripts/build-prism.py` で `build/` に作り、GitHub Release に添付します。zip は pack の URL を指すだけなので、MOD の更新では作り直す必要はありません

## 権利

各 MOD の権利と配布条件は、それぞれの作者と配布元に帰属します。この repository は packwiz の metadata と Lunatic Craft 2 独自の設定を管理します
