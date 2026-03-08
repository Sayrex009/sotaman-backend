from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category 
from listing.models import announcement, AIGeneration

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'is_staff', 'is_active']
    search_fields = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'img')
    search_fields = ('title',)

@admin.register(announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'created_at')
    search_fields = ('title', 'city')
    list_filter = ('city',)

@admin.register(AIGeneration)
class AIGenerationAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing', 'created_at')
    search_fields = ('user__email', 'listing__title')
    list_filter = ('created_at',)
