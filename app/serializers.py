from rest_framework import serializers
from .models import Advertisement
from listing.models import announcement, AIGeneration, Favorite
class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ['created_at']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields = '__all__'
        read_only_fields = ['created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['created_at']