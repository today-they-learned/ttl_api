from background_task import background
from utils.analyze_github_til import AnalyzeGithubTil
from article.models import Article
from user.models import User


@background(schedule=20)
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

    for title, content in results:
        Article.objects.get_or_create(
            user=user,
            source="gh",
            title=title,
            content=content,
        )
