from django.contrib import admin
from blog.models import *
from comments.models import *
from core.models import *
from like.models import *

# Register your models here.


class PostInline(admin.TabularInline):
    model = Post


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(LikeDislike)
class LikeABoss(admin.ModelAdmin):
    list_display = "id", "__str__"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name",


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "name",
    inlines = CommentInline,


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = "id", "name",
    inlines = PostInline,


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = "id", "author",


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass