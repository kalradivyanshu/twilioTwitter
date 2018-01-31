from crontab import CronTab
my_cron = CronTab(user='ubuntu')
for job in my_cron:
    job.delete()
job = my_cron.new(command='python3 ~/twilioTwitter/server/cronJobber.py')
job.hour.every(1)
my_cron.write()
