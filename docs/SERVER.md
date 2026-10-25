# サーバー運用ガイド

server もクライアントと同じ `pack.toml` を参照し、packwiz-installer の server side filter でクライアント専用 MOD を除いて同期します

## 構成

| 項目 | 値 |
|---|---|
| ディレクトリ | `/opt/minecraft/lunatic-craft2` |
| service | `lunatic-craft2.service`（起動前に packwiz 同期） |
| Java | `/usr/lib/jvm/java-21-openjdk-amd64`（`openjdk-21-jre-headless`） |
| メモリ | `-Xms4G -Xmx9G`（`user_jvm_args.txt`） |
| 描画距離 | view-distance 10 / simulation-distance 8 |
| バックアップ | Simple Backups が 2 時間ごとに `simplebackups/` へ出力。`simplebackups` は HDD の `/opt/minecraft/backups/lunatic-craft2` への symlink |
| 遠景 | Distant Horizons。server の `config/DistantHorizons.toml` で `numberOfThreads = 2`、`maxGenerationRequestDistance = 256` に絞る |
| Web 地図 | BlueMap（8100 番）。server の `config/bluemap/core.conf` で `accept-download: true`、`render-thread-count: 2` |
| Discord | Simple Discord Link。トークンとチャンネルは server の `config/simple-discord-link/simple-discord-link.toml` にだけ置く |

`server.properties` と Discord の設定は repository で管理しません。RCON のパスワードも server の `server.properties` にだけあります

## ガイド本

初回参加時にガイド本を渡すデータパックは、ワールドに入れるため packwiz では配りません。新しいワールドを作ったら、repository の `datapacks/lunatic_guide` を server の `world/datapacks/` にコピーして `/reload` します。本の中身（`patchouli_books/`）は packwiz で配ります

## 更新手順

1. pack 定義を更新して GitHub へ push する
2. 接続中のプレイヤーに予告する
3. `systemctl restart lunatic-craft2` で再起動する。起動前に packwiz が差分を同期する
4. `journalctl -u lunatic-craft2 -f` で `Done (` を確認する

ワールド生成に関わる MOD を変えるときは、既存ワールドに入れる前に手元の dedicated server で確かめます
