
from django.contrib import admin
from django.urls import path, include
from core.views import ImoveisViewSet
from core.views import ImobiliariaViewSet
from rest_framework import routers
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'imoveis', ImoveisViewSet)
router.register(r'imobiliarias', ImobiliariaViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Teste Resale",
      default_version='v1',
      description="API Imobiliaria Resale",
      terms_of_service="",
      contact=openapi.Contact(email="gustavo.grc@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),    
    path('documentacao/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
