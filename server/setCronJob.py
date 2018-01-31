from crontab import CronTab
my_cron = CronTab(user='ubuntu')
job = my_cron.new(command='python ~/twilioTwitter/server/cronJobber.py')
job.hour.every(1)
my_cron.write()
