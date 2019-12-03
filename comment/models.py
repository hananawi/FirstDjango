from django.db import models
from django.utils import timezone
from user.models import User
from article.models import Article

# Create your models here.


class Comment(models.Model):
    content = models.TextField()

    date = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', default='1')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment', default=2)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.content[:50]
