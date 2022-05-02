from django.db import models
from uuid import uuid4


class StreamHelper(models.Model):
    myUUID = models.UUIDField(default=uuid4)
    user = models.CharField(max_length=30)
    descr = models.CharField(max_length=30, default="descr")
    name = models.CharField(max_length=20, default="somename")
    count = models.IntegerField(default=0)
