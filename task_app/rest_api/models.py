from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False, unique=True, blank=False,
        verbose_name="id",
        help_text="ID Task"
    )
    title = models.CharField(
        null=False, unique=True, blank=False,
        max_length=200,
        verbose_name="title",
        help_text="Title Task"
    )
    description = models.TextField(
        null=False, blank=False,
        verbose_name="description",
        help_text="Description Task"
    )
    status = models.BooleanField(
        null=False, blank=False, default=False,
        verbose_name="status",
        help_text="Status Task, True-Complete/False-Incomplete"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="owner",
        help_text="Owner Task"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']