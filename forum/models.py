from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User
from userauth.models import CustomUser


# Create your models here.
class Forum(models.Model):
    author = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_replies(self):
        return self.replies.filter(parent=None)

class Reply(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, null=False, on_delete=models.CASCADE, related_name='replies')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    desc = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

    def get_childs(self):
        return Reply.objects.filter(parent=self)