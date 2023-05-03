from django.contrib import admin

from .models import Category, Group, State, Post, Photo

class PhotoAdmin(admin.StackedInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.2/intro/tutorial07/ for more info about admin model usages
    #fields = [] here you can rearrange the fields
    #fieldsets = [
    # (None, {"fields": ["name_field"]}),
    # ("Other", {"fields": ["name1_field"]}),
    # ]
    inlines = [PhotoAdmin]
    fields = ["title", "active", "price", "category_id", "state_id", "path", "post_groups"]

    #formfield_overrides = {}
    class Meta:
        model = Post

#https://medium.com/@skodak95alexis/multiple-file-upload-in-django-admin-814aec01dc4b
#https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/#uploading-multiple-files
#https://gist.github.com/serdardurbaris/039c69fdab60a4c68e34314e2b1ccf35
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(State)
admin.site.register(Group)
