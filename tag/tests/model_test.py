from django.test import TestCase
from parameterized import parameterized

from .factories import TagFactory


class TagModelTest(TestCase):
    """Tag Model Test"""

    @parameterized.expand([
        ('python', 'python'),
        ('cpp', 'cpp'),
        ('태그', '태그'),
        ('ruby on rails', 'ruby on rails'),
    ])
    def test_is_createable(self, name, expected):
        """Tag가 name만으로 정상적으로 생성되는지"""

        tag = TagFactory(name=name)
        self.assertEqual(expected, tag.name)
