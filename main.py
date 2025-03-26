import discord
from discord.ext import commands
from bot.scheduler import setup_scheduler       # 毎月1日のスケジューラ設定を読み込み
from config.settings import BOT_TOKEN       # トークンを設定ファイルから読み込み

# Botのインテント（イベント受信の設定）
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容の読み取りを有効化（2022年以降、メッセージ本文の取得には明示的な許可が必要）

# Botインスタンス作成（コマンドプレフィックス指定）
bot = commands.Bot(command_prefix='!', intents=intents)

# announce.py, schedular.pyで、引数となるオブジェクト(bot)があるが、
# あれらはすべて、この変数bot内に格納されたBotインスタンスを受け取ることを前提にしている。

# Botの準備が完了したときに一度だけ呼ばれるイベント
@bot.event
async def on_ready():
    print(f'✅ ログイン完了: {bot.user}')
    setup_scheduler(bot)  # APScheduler のスケジュール起動（毎月1日送信）

# Botを起動しDiscordに接続
bot.run(BOT_TOKEN)
