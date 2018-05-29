from rest_framework import serializers

from feeds.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedItem
        fields = ('id', 'content', 'user')
