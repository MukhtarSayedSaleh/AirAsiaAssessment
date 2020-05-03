from hotels.models import Package
from rest_framework import viewsets
from rest_framework import permissions
from hotels.serializers import PackageSerializer


class PackageViewSet(viewsets.ModelViewSet):
    """
    CRUD API endpoints for Package model
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    
    # we will keep it open for the world for this assessment,
    # however, in reality a proper permission class should be applied
    # to prevent unauthorised consumers from consume it.
    permission_classes = [permissions.AllowAny]