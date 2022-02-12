import logging

from django.views.generic.base import View
from braces.views import CsrfExemptMixin


class BaseView(CsrfExemptMixin, View):
    """BaseView"""

    logger = logging.getLogger(__name__)
    lookup_field = "id"

    @property
    def current_user(self):
        """Return request user(current user)"""

        return self.request.user

    @property
    def is_authenticated_user(self):
        """Return whether current user is authenticated"""

        return self.current_user.is_authenticated

    @property
    def is_anonymous_user(self):
        """Return whether current user is anonymous"""

        return self.current_user.is_anonymous
