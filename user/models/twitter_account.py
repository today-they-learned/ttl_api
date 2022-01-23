from .sns_account import SnsAccount


class TwitterAccount(SnsAccount):
    """Model definition for TwitterAccount."""

    @staticmethod
    def get_user_related_name():
        return "twitter_account"

    class Meta:
        """Meta definition for TwitterAccount."""

        db_table = "twitter_accounts"
        verbose_name = "TwitterAccount"
        verbose_name_plural = "TwitterAccounts"
        default_related_name = "twitter_account"
