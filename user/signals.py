from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from user.models import User
from article.tasks import collect_github_til_task, collect_velog_til_task


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(pre_save, sender=User)
def collect_github_til(sender, instance, **kwargs):
    if instance is None:
        return

    current_user = instance
    previous_user = User.objects.filter(id=instance.id).first()

    if current_user.repository and (
        previous_user is None or current_user.repository != previous_user.repository
    ):
        collect_github_til_task.subtask(
            current_user.id, current_user.repository
        ).apply_async()


@receiver(pre_save, sender=User)
def collect_velog_til(sender, instance, **kwargs):
    if instance is None:
        return

    current_user = instance
    previous_user = User.objects.filter(id=instance.id).first()

    if current_user.velog_username and (
        previous_user is None
        or current_user.velog_username != previous_user.velog_username
    ):
        collect_velog_til_task.subtask(
            current_user.id, current_user.velog_username
        ).apply_async()
