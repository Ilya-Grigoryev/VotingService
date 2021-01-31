from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Voting(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    status = models.TextField()
    type = models.SmallIntegerField()


class Options(models.Model):
    text = models.TextField()
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)


class VotedUsers(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    option = models.ForeignKey(to=Options, on_delete=models.CASCADE)


class AbuseReports(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(default='open')
    image = models.ImageField(null=True, blank=True, upload_to='images/')


class Messages(models.Model):
    dialog = models.ForeignKey(to=AbuseReports, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Likes(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)


class Dislikes(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/')
    status = models.TextField(default='')


class BackupCode(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    code = models.TextField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
