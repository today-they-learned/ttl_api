import imp
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

# 아래와 같이 스케쥴을 등록할 수 있습니다.
# app.conf.beat_schedule = {
#     "every-15-second": {
#         "task": "polls.tasks.say_hello",
#         "schedule": 15,
#         #        'args': (,)
#     }
# }

# Django 에 등록된 모든 task 모듈을 로드합니다.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
