from user.models import User
from article.tasks.collect_github_til_task import collect_github_til_task
from celery import shared_task


@shared_task
def refresh_user_collect_github():
    users = User.objects.all()
    for user in users:
        if user.repository:
            collect_github_til_task.apply_async(user.id, user.repository)
