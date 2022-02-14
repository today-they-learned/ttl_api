from user.models import User
from collect_github_til_task import collect_github_til_task

def put_user_collect_github():
    users = User.objects.all()
    for user in users:
        if user.repository:
            collect_github_til_task.apply_async(user.id,user.repository)
