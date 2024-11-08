from django.db import models
from django.conf import settings

class Chat(models.Model):
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    room_name=models.CharField(max_length=15)
    def __str__(self):
        return self.body
