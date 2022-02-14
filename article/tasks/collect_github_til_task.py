import os

from datetime import datetime
from utils.analyze_github_til import AnalyzeGithubTil
from article.models import Article
from user.models import User, Grass
from celery import shared_task


@shared_task
def collect_github_til_task(user_id, repository):
    user = User.objects.filter(id=user_id).first()

    if user is None or repository is None or not "/" in repository:
        return

    username, repository = repository.split("/")

    if username is None or repository is None:
        return

    analyzation = AnalyzeGithubTil(username, repository)
    analyzation.perform()

    results = analyzation.results
    dates_by_file = analyzation.dates_by_file

    for title, content, path in results:
        article, is_created = Article.objects.get_or_create(
            user=user,
            source="gh",
            title=str(title).strip(),
            content=str(content).strip(),
        )

        if is_created:
            path = path.replace(f"./analyze/{username}/{repository}/", "")

            if path not in dates_by_file:
                continue

            created_at, *updated_ats = sorted(
                dates_by_file[path],
                key=lambda t: datetime.strptime(t, "%Y-%m-%d %H:%M:%S%z"),
            )

            if created_at:
                write_grass, _ = Grass.objects.get_or_create(
                    user=user,
                    created_at=datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S%z"),
                )

                write_grass.write_count += 1
                write_grass.save()

            for updated_at in updated_ats:
                if updated_at:
                    edit_grass, _ = Grass.objects.get_or_create(
                        user=user,
                        created_at=datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S%z"),
                    )
                    edit_grass.edit_count += 1
                    edit_grass.save()
