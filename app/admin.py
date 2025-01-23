from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Article, UserProfile 


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at","updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")


class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)
