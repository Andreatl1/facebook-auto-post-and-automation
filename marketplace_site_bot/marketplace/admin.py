from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.2/intro/tutorial07/ for more info about admin model usages
    #fields = [] here you can rearrange the fields
    #fieldsets = [
    # (None, {"fields": ["name_field"]}),
    # ("Other", {"fields": ["name1_field"]}),
    # ]
    pass

admin.site.register(Post, PostAdmin)