# APSchedulerを用いた定期実行スケジューリング
# announce.send_announcementを定期実行
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from .announce import send_announcement

#ここで、引数botはmain.py内で作成されたBotインスタンス
def setup_scheduler(bot):
    scheduler = AsyncIOScheduler()

    # 毎月1日 9:00（日本時間）に実行
    trigger = CronTrigger(day=1, hour=9, minute=0, timezone='Asia/Tokyo')
    scheduler.add_job(send_announcement, trigger, args=[bot])

    scheduler.start()
