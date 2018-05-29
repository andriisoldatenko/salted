from django.contrib import admin
from django.urls import path

from feeds.api.views import (
    AllFeedItemListAPIView,
    MyFeedItemListAPIView,
    TrackedFeedItemListAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Api urls for feeds
urlpatterns += [
    path('api/feeds/all/', AllFeedItemListAPIView.as_view(),
         name='all feeds'),
    path('api/feeds/my/', MyFeedItemListAPIView.as_view(),
         name='my feed'),
    path('api/feeds/tracked/', TrackedFeedItemListAPIView.as_view(),
         name='tracked by me feed')
]
