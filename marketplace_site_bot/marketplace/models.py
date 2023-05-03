from django.db import models

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
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    option = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    path = models.CharField(max_length=60)
    groups = models.CharField(max_length=2048)
    label = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    post_groups = models.ManyToManyField(Group)
    state_id = models.ForeignKey(State, on_delete=models.RESTRICT)
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)
    def __str__(self):
        return self.title
    
