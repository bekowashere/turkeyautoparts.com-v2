from django.urls import path
from glossary.api.views import (
    GlossaryTermListAPIView,
    GlossaryTermDetailAPIView
)

app_name = 'glossary'

urlpatterns = [
    path('list/', GlossaryTermListAPIView.as_view(), name='glossary_list'),
    path('detail/<slug>/', GlossaryTermDetailAPIView.as_view(), name='glossary_detail'),
]
