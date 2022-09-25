from django.urls import path
from news.api.views import (
    NewsItemListAPIView,
    NewsItemDetailAPIView
)

app_name = 'news'

urlpatterns = [
    path('list/', NewsItemListAPIView.as_view(), name='news_list'),
    path('detail/<slug>/', NewsItemDetailAPIView.as_view(), name='news_detail')
]