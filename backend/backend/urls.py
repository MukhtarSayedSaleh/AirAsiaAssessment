from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from hotels import views

schema_view = get_schema_view(
   openapi.Info(
      title="AirAsia Assessment API",
      default_version='v1',
      description="By: Muktar sayed saleh",
      contact=openapi.Contact(email="mokhtar_ss@hotmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'package', views.PackageViewSet)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]
