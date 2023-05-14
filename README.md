# 音声入力デモ

このリポジトリには、音声入力を行う2つの方法をデモンストレーションするPythonスクリプトが含まれています。一つはPush-to-Talk方式で、もう一つはVoice Activity Detection (VAD)方式です。

- `push_to_talk_demo.py`: キーを押している間だけ音声を録音します。
- `vad_demo.py`: 音声が検出された時だけ録音します。

## インストール手順

このデモを実行するには、いくつかのPythonライブラリが必要です。これらは`requirements.txt`にリストアップされています。次のコマンドでインストールできます。

```sh
pip install -r requirements.txt
```

## スクリプトの実行手順

それぞれのスクリプトは単体で実行可能です。

Push-to-Talkデモを実行するには、以下のコマンドを実行します。

```sh
python push_to_talk_demo.py
```

VADデモを実行するには、以下のコマンドを実行します。

```sh
python vad_demo.py
```
