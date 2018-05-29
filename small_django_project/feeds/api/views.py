from rest_framework.generics import ListAPIView

from feeds.api.serializers import FeedItemSerializer
from feeds.models import FeedItem


class AllFeedItemListAPIView(ListAPIView):
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer


class MyFeedItemListAPIView(ListAPIView):
    model = FeedItem
    serializer_class = FeedItemSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TrackedFeedItemListAPIView(ListAPIView):
    model = FeedItem
    serializer_class = FeedItemSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            user__registereduser__tracked_by__user=self.request.user
        )
