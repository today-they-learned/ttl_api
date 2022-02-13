from utils.analyze_velog_til import AnalyzeVelogTIL
from article.models import Article
from user.models import User
from celery import shared_task


@shared_task
def collect_velog_til_task(user_id, velog_username):
    user = User.objects.filter(id=user_id).first()

    if user is None or velog_username is None:
        return

    analyzation = AnalyzeVelogTIL(velog_username)
    analyzation.perform()

    results = analyzation.results

    for result in results:
        Article.objects.get_or_create(
            user=user,
            source="vl",
            title=result["title"],
            content=result["content"],
            tags=result["tags"],
            created_at=result["created_at"],
        )
