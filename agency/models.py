from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # TODO: ordering by date_published
    # class Meta:
    #     ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Redactor(AbstractUser):
    # username = models.CharField(max_length=255, unique=True)
    years_of_experience = models.IntegerField(max_length=63)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "publishers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    # def get_absolute_url(self):
    #     return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
