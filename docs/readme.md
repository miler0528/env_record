# env_record
BME-280、ESP32、PCを接続し、環境データを取得し、CSVとSQLDBに保存します。

BME-280とESP32の接続については、以下を参照。

https://qiita.com/miler0528/items/a420e6580757bbbdf2ec


# Requirement

* python
    * huga 3.5.2
* ESP32
    * Adafruit BME280 Library

# Installation

* python
```bash
$ pip install -r requirements.txt
```

* ESP32
    - VSCODEの拡張機能「PlatformIO」を使用しています。
    - 詳細はplatformio.iniを確認ください

# Usage

1. esp32フォルダをプロジェクトフォルダとして、VS Code上のPlatformIOから開く
2. PlatformIOからAdafruit BME280 Libraryをインストール
3. プログラムをコンパイルして書き込む
4. PC上のDBを設定し、secret_template.pyに設定値を書き込み、secret.pyにリネームする
5. receive_ser.py中のCOMポートを書き換える（必要なくなるように修正予定）
6. receive_ser.pyを実行する

# Note
- DB上に必要なカラムを設定してから実行ください。
- COMポート

# Author
* miler0528
* miler.yoshio@gmail.com

# License

作者は本プログラムを使用することによる如何なる損害についても責任を負いません。
その条件の下でLicense Free.
