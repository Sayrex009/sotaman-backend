from django.contrib import admin
from .models import user, category, Subscription

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