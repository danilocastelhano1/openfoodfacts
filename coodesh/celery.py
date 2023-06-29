import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coodesh.settings")

app = Celery("coodesh")

CELERY_BEAT_SCHEDULE = {
    "scrap_products": {
        "task": "coodesh.api.tasks.scrap_products",
        "schedule": crontab(
            minute=settings.CRONTAB_TIME[0],
            hour=settings.CRONTAB_TIME[1],
            day_of_week=settings.CRONTAB_TIME[2],
            day_of_month=settings.CRONTAB_TIME[3],
            month_of_year=settings.CRONTAB_TIME[4],
        ),
    },
}
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
