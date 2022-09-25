# Rest Framework Views
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Rest Framework Filters
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from news.models import Category, Tag, NewsItem

from news.api.serializers import (
    CategoriesSerializer,
    TagsSerializer,
    NewsItemListSerializer,
    NewsItemDetailSerializer
)

# /news
# http://127.0.0.1:8000/api/news/list/?tags__slug=bmw&category__slug=renderings
class NewsItemListAPIView(ListAPIView):
    queryset = NewsItem.objects.filter(status=1)
    serializer_class = NewsItemListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__slug', 'category__slug', 'user__username']

class NewsItemDetailAPIView(RetrieveAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemDetailSerializer
    lookup_field = 'slug'
