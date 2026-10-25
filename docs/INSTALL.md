# クライアント導入ガイド

## 必要なもの

- [Prism Launcher](https://prismlauncher.org/)
- 8 GiB 以上の空きメモリ（インスタンスには 8 GiB を割り当てます）

Java 21 は Prism Launcher 9 以降なら自動で用意されます。手動で選ぶ場合は Java 21 を指定してください

## 初回導入

1. [Releases](https://github.com/tsukuyomi-luna/lunatic-craft2/releases/latest) から `lunatic-craft2-<version>-prism.zip` を取得する
2. Prism Launcher で `インスタンスを追加` → `zipからインポート` を開き、zip を指定する
3. インスタンスを起動する

起動前に packwiz-installer が MOD と設定をダウンロードします。初回は数分かかります

## 更新

同じインスタンスを起動するだけです。追加・更新・削除された MOD は起動前に反映されます。更新のたびに zip を入れ直す必要はありません

`saves`、`screenshots`、`shaderpacks`、個人の `options.txt` は上書きされません

## リソースパック

三人称視点のプレイヤーの動きを細かくする Detailed Animations が入っています。`設定 → リソースパック` で有効にしてください

## シェーダー

Iris が入っています。シェーダーパックは各自で `shaderpacks` に入れ、ビデオ設定の `シェーダーパック` から選んでください。Create Aeronautics の乗り物の表示が崩れたら、シェーダーを切ってください

## 注意

- 同期中に Prism Launcher を強制終了しないでください
- 自分で MOD を追加すると、サーバーに入れなくなることがあります
