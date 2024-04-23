# myapp/tasks.py

from django_cron import CronJobBase, Schedule
from datetime import datetime, timedelta


class MyCronJob(CronJobBase):
    RUN_EVERY_SECONDS = 10  # run every 10 seconds

    schedule = Schedule(run_every_seconds=RUN_EVERY_SECONDS)
    code = 'cronapp.my_cron_job'  # a unique code for this cron job

    def do(self):
        # Your task logic here
        print("Running my cron job at", datetime.now())
