from user.models import User
from article.tasks.collect_velog_til_task import collect_velog_til_task
from celery import shared_task


@shared_task
def refresh_user_collect_velog():
    users = User.objects.all()
    for user in users:
        if user.velog_username:
            collect_velog_til_task.apply_async(user.id, user.velog_username)
