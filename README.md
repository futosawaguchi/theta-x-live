# theta-x-live

RICOH THETA X と PC を接続し、Python でリアルタイム 360° 映像を取得・表示するプロジェクト。

## 必要環境

- Python 3.9+
- RICOH THETA X
- THETA X を Wi-Fi AP モード で起動し、PC を `THETAXL...` の SSID に接続すること

## セットアップ

```bash
# 依存ライブラリをインストール
pip install -r requirements.txt

# 環境変数を設定
cp .env.example .env
# .env を編集して THETA_SERIAL にカメラのシリアル番号を入力
```

### `.env` の設定

```
THETA_SERIAL=カメラ底面のシリアル番号（例: YR13100001）
THETA_IP=192.168.1.1
```

> シリアル番号は HTTP Digest 認証のユーザー名・パスワードとして使用されます。
> `.env` は `.gitignore` に含まれており、リポジトリにはコミットされません。

## 使い方

### リアルタイムプレビュー

```bash
cd src
python live_preview.py
```

OpenCV ウィンドウに 360° 映像（Equirectangular 形式）がリアルタイム表示されます。  
`q` キーで終了。

### 静止画撮影

```bash
cd src
python capture.py
```

## プロジェクト構成

```
theta-x-live/
├── .env                  # 認証情報（gitignore済み・各自で設定）
├── .env.example          # 変数名のテンプレート
├── requirements.txt
└── src/
    ├── utils.py          # カメラ接続・認証ヘルパー
    ├── live_preview.py   # MJPEGストリーム取得・リアルタイム表示
    └── capture.py        # 静止画・動画キャプチャ
```

## API について

RICOH THETA Web API（OSC: Open Spherical Camera API v2.1）を使用しています。

- 公式仕様: https://github.com/ricohapi/theta-api-specs
- コミュニティ: https://community.theta360.guide
