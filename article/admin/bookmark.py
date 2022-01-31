from django.contrib import admin
from user.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """"Admin View for Bookmark"""
    
    list_display = (
        "user",
        "created_at"
    )
    
    readonly_fields = (
        "user",
        "created_at"
    )
    ordering = (
        "created_at",
    )
