from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Voting(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
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
    text = models.TextField()
    status = models.TextField()


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
