from config.settings import TARGET_CHANNEL_ID

#ここで、引数botはmain.py内で作成されたBotインスタンス
async def send_announcement(bot):
    channel = bot.get_channel(TARGET_CHANNEL_ID)
    if channel:# bot.get_channelはbool型
        await channel.send("今月のお知らせです！")  
    else:
        print("チャンネルが見つかりませんでした。")
