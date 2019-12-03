from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    total_views = models.PositiveIntegerField(default=0)
    comments = models.IntegerField(default=0)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_time',)
