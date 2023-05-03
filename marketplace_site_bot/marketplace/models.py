from django.db import models
from PIL import Image


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=99)
    price = models.IntegerField()

    description = models.CharField(max_length=400, null=True)
    active = models.BooleanField(default=True)


    path = models.CharField(max_length=60)
    
    state_id = models.ForeignKey(State, on_delete=models.RESTRICT)
    post_groups = models.ManyToManyField(Group)
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Photo(models.Model):
    post_id = models.ForeignKey(
        Post, on_delete=models.RESTRICT, related_name="photos")
    photo = models.ImageField(upload_to="../img/")

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.photo.path, quality=100, optimize=True)
