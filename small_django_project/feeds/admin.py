from django.contrib import admin

from .models import FeedItem, RegisteredUser


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    pass
