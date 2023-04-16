from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelsTests(TestCase):

    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="user8",
            first_name="Vasya",
            last_name="Pupkin",
            email="ad@min.ua",
            password="345ert345",
            years_of_experience=5,
        )
        self.topic = Topic.objects.create(
            name="Computing"
        )
        self.newspaper = Newspaper.objects.create(
            title="Introduction to version control with Git",
            content="What is a commit message? ...",
            topic=self.topic,
        )

    def test_topic_str(self) -> None:
        obj = self.topic
        self.assertEqual(str(obj), "Computing")

    # def test_newspaper_str(self) -> None:
    #     obj = self.newspaper
    #     self.assertEqual(str(obj), obj.model)
    #
    # def test_driver_str(self) -> None:
    #     obj = self.driver
    #     self.assertEqual(
    #         str(obj), f"{obj.username} ({obj.first_name} {obj.last_name})"
    #     )
    #
    # def test_driver_get_absolute_url(self):
    #     driver = self.driver
    #     self.assertEqual(driver.get_absolute_url(), "/drivers/1/")
