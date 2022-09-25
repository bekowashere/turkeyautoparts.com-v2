from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenRefreshView
from account.api.views import (
    MyTokenObtainPairView,
    CustomerUserMyTokenObtainPairView,
    SupplierUserMyTokenObtainPairView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls')),
    path('api/auto/', include('auto.api.urls')),
    path('api/autopart/', include('autopart.api.urls')),
    path('api/glossary/', include('glossary.api.urls')),
    path('api/news/', include('news.api.urls')),
    path('api/order/', include('order.api.urls')),
    path('api/world/', include('world.api.urls')),

    # TOKEN - LOGIN
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/customer/', CustomerUserMyTokenObtainPairView.as_view(), name='login_customer'),
    path('api/login/supplier/', SupplierUserMyTokenObtainPairView.as_view(), name='login_supplier'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)