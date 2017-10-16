from django.contrib import admin
from blog.models import *
from comments.models import *
from core.models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
