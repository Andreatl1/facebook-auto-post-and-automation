from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=99)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    path = models.CharField(max_length=60)
    groups = models.CharField(max_length=2048)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.title