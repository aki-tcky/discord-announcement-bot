# 📅 Discord定期アナウンスBot

このBotは、**毎月1日にExcelファイルから予定や情報を読み取り、Discordサーバーに自動でアナウンスを送信**するツールです。PythonとAPSchedulerを使ってスケジューリングを実現しています。

---

## ✅ 主な機能

- 毎月1日に指定チャンネルへアナウンスメッセージを送信
- Excelファイルからデータを読み取り、動的な内容を送信可能
- APSchedulerによる非同期スケジューリング

---

## 🧾 使用例

> 「data/schedule.xlsx」 に記載された予定に基づき、以下のようなメッセージを送信：

📢 今月のお知らせです！

〇〇イベント: 3月5日（金）

提出締切: 3月10日（月）

ミーティング: 3月20日（水） 18:00～


---

## 🔧 セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/aki-tcky/discord-announcement-bot.git
cd discord-announcement-bot
```

### 2. 必要パッケージをインストール
```bash
pip install -r requirements.txt
```
### 3. BotトークンとチャンネルIDを設定
config/settings.py を編集：
```bash
BOT_TOKEN = 'あなたのBotのトークン'
TARGET_CHANNEL_ID = 123456789012345678  # 送信先チャンネルのID（整数で記入）
```

### 4. Excelファイルの準備
data/schedule.xlsx をあなたの予定表に差し替えてください。

## 🚀 実行方法
以下のコマンドでBotを起動できます：

``` bash
python main.py
```
Botがログインし、スケジューラが自動的に起動します。

## 📁 ディレクトリ構成
```bash
discord_bot/
├── main.py                  # メイン実行ファイル（Bot起動）
├── bot/
│   ├── __init__.py
│   ├── announce.py          # Discordへのアナウンス機能
│   ├── scheduler.py         # 毎月の実行スケジュール設定（APScheduler）
│   └── excel_reader.py      # Excelデータの読み込み＆対象抽出
├── config/
│   └── settings.py          # トークンや定数の設定
├── data/
│   └── schedule.xlsx        # データファイル（予定表など）
├── requirements.txt         # 使用ライブラリ一覧
└── README.md                # プロジェクト概要（このファイル）
```
## 📦 使用ライブラリ
discord.py

APScheduler

openpyxl（Excelファイルの読み込み）

## 📌 備考
Botがチャンネルでメッセージを送れるよう、該当チャンネルで「メッセージ送信」権限を付与してください。

スケジュールのテストには、トリガー時間を短めに設定して検証可能です。

## 🛠 カスタマイズ案
Embedでのアナウンス表示対応

複数チャンネル・複数Botへの対応

GoogleカレンダーやNotion連携など

## 📝 ライセンス
MIT License



作成者: [aki_tcky]
お問い合わせ・Issue歓迎！
