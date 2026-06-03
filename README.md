# theta-x-live

RICOH THETA X と PC を接続し、Python でリアルタイム 360° 映像を取得・表示するプロジェクト。

## 必要環境

- Python 3.11+
- RICOH THETA X

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# .env を編集して各値を設定する
```

### `.env` の設定

```
THETA_SERIAL=カメラのシリアル番号（例: YR15122416）
THETA_PASSWORD=カメラの Wi-Fi パスワード（AP モード設定画面で確認）
THETA_IP=カメラの IP アドレス（接続モードによって異なる）
```

> `.env` は `.gitignore` に含まれており、リポジトリにはコミットされません。

---

## 接続モード

### CL モード（推奨）

カメラと PC を同じ Wi-Fi ネットワークに接続する方式。  
PC のインターネット接続を維持したまま使用できる。

**カメラ側の設定：**

```
カメラ設定 → 接続 → Wi-Fi → クライアントモード（CL）→ 接続先 Wi-Fi を選択
```

**`.env` の `THETA_IP` にカメラの IP を設定する：**

カメラ画面のカメラ情報からIP addressを取得

```
THETA_IP=10.32.x.x  # IP
```

---

### AP モード

カメラ自身が Wi-Fi アクセスポイントになる方式。  
PC はカメラの SSID に直接接続するため、接続中はインターネットが使用できない。

**カメラ側の設定：**

```
カメラ設定 → 接続 → Wi-Fi → アクセスポイントモード（AP）
```

**Mac の Wi-Fi から SSID を選択して接続：**

```
SSID:     THETAYR＜シリアル番号＞.OSC
Password: ＜シリアル番号の数字部分＞（カメラ画面の「カメラ情報」で確認）
```

**`.env` の `THETA_IP` を固定 IP に設定：**

```
THETA_IP=192.168.1.1
```

---

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

---

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
