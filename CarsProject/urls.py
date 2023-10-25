from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CarsProject API",
        default_version='v1',
        description="Enjoy!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('account/', include('cars_account.urls')),
    path('cars/', include('cars_inventory.urls')),
    path('sales/', include('sales_contract.urls')),
    path('customer/', include('customer_profile.urls')),
    path('payment/', include('payment.urls')),
    path('deliver/', include('car_deliver.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('swagger(<format>|.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
