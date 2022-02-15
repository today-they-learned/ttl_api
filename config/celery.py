import imp
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Django 에 등록된 모든 task 모듈을 로드합니다.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    "refresh-github-every-45-minute": {
        "task": "refresh_user_collect_github",
        "schedule": crontab(minute="*/45"),
    },
    "refresh-velog-every-15-minute": {
        "task": "collect_velog_til_task",
        "schedule": crontab(minute="*/15"),
    },
}
