from django.contrib import admin
from .models import user, category, Subscription
from listing.models import announcement, AIGeneration
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_authenticated')
    search_fields = ('username', 'email')
    list_filter = ('is_authenticated',)


@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'img')
    search_fields = ('title',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'expires_at', 'created_at')
    list_filter = ('plan',)
    search_fields = ('user__username', 'plan')

@admin.register(announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'created_at')
    search_fields = ('title', 'city')
    list_filter = ('city',)

@admin.register(AIGeneration)
class AIGenerationAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'created_at')
    search_fields = ('user__username', 'listing__title')
    list_filter = ('created_at',)