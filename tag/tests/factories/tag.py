import factory
from faker import Faker
from taggit.models import Tag

fake = Faker()


class TagFactory(factory.django.DjangoModelFactory):
    """Django Taggit Tag Model Factory"""

    name = factory.LazyAttribute(lambda t : fake.name())

    class Meta:
        """Meta Definition for TagFactory."""
        model = Tag
