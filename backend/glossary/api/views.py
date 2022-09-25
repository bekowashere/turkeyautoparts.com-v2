# Rest Framework Views
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from glossary.models import GlossaryCategory, GlossaryTerm

from glossary.api.serializers import GlossaryCategorySerializer, GlossaryTermSerializer

class GlossaryTermListAPIView(ListAPIView):
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryTermSerializer

class GlossaryTermDetailAPIView(RetrieveAPIView):
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryTermSerializer
    lookup_field = 'slug'