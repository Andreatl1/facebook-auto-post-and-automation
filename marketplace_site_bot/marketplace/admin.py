from django.contrib import admin

from .models import Category, Group, State, Post

class PostAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.2/intro/tutorial07/ for more info about admin model usages
    #fields = [] here you can rearrange the fields
    #fieldsets = [
    # (None, {"fields": ["name_field"]}),
    # ("Other", {"fields": ["name1_field"]}),
    # ]
    fields = ["title", "price", "category", "state", "description", "path", "groups", "label", "type", "option"]

    #formfield_overrides = {}

#https://medium.com/@skodak95alexis/multiple-file-upload-in-django-admin-814aec01dc4b
#https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/#uploading-multiple-files
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(State)
admin.site.register(Group)
