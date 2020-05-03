from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from hotels import views

router = routers.DefaultRouter()
router.register(r'package', views.PackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
