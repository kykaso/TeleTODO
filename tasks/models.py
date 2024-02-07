from django.db import models


# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['date_created']

    def __init__(self):
        self.title = None

    def __str__(self):
        return self.title
