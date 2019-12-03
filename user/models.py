from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)

    register_date = models.DateTimeField(default=timezone.now)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    article_posted = models.IntegerField(default=0)
    comment_reply = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-register_date', )

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     biography = models.TextField(max_length=1000, blank=True)
#     avatar = models.ImageField(upload_to='avatar/%y%m%d/', blank=True)
#
#     def __str__(self):
#         return 'user: {}'.format(self.user.username)
#
#
# # 信号接收函数，每当新建 User 实例时自动调用
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# # 信号接收函数，每当更新 User 实例时自动调用
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
