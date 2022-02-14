from utils.analyze_velog_til import AnalyzeVelogTIL
from article.models import Article
from user.models import User, Grass
from celery import shared_task
from datetime import datetime


@shared_task
def collect_velog_til_task(user_id, velog_username):
    user = User.objects.filter(id=user_id).first()

    if user is None or velog_username is None:
        return

    analyzation = AnalyzeVelogTIL(velog_username)
    analyzation.perform()

    results = analyzation.results

    for result in results:
        created_at = datetime.strptime(result["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        article, is_created = Article.objects.get_or_create(
            user=user,
            source="vl",
            title=str(result["title"]).strip(),
            content=str(result["content"]).strip(),
        )

        for tag in result["tags"]:
            if len(tag) > 0:
                article.tags.add(tag)

        if is_created:
            grass, _ = Grass.objects.get_or_create(
                user=user,
                created_at=created_at,
            )
            grass.write_count += 1
            grass.save()
