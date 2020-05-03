import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Package
from .serializers import PackageSerializer

client = Client()

# GET Single Package
class GetSinglePackageTest(TestCase):
    def setUp(self):
        self.package_1 = Package.objects.create(description='TestPackage1', price=100, duration=2, valid_until='2021-01-01')
        self.package_2 = Package.objects.create(description='TestPackage2', price=100, duration=2, valid_until='2021-01-01')
        self.package_3 = Package.objects.create(description='TestPackage3', price=100, duration=2, valid_until='2021-01-01')

    def test_get_valid_single_package(self):
        response = client.get('/package/' + str(self.package_1.pk) + '/')
        package = Package.objects.get(pk=self.package_1.pk)
        serializer = PackageSerializer(package)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_package(self):
        response = client.get('/package/-1/') # invalid package ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# GET Multiple Packages
class GetMultiplePackagesTest(TestCase):

    def test_get_multipple_package(self):
        response = client.get('/package/')
        # get data from db to be able to assert
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# POST
class CreateNewPackageTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'hotel': 'AirAsia Hotel',
            'description': 'Test package 1',
            'duration': 4,
            'price': 1500,
            'valid_until': '2022-01-01'
        }
        self.invalid_payload = {
            'Hotel': 100,
            'description': True,
            'duration': -1,
            'price': -1500,
            'valid_until': '2022-02-55'
        }

    def test_create_valid(self):
        response = client.post(
            '/package/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            '/package/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# PUT
class UpdateSinglePackageTest(TestCase):

    def setUp(self):
        self.package_1 = Package.objects.create(description='TestPackage1', price=100, duration=2, valid_until='2021-01-01')
        self.package_2 = Package.objects.create(description='TestPackage2', price=100, duration=2, valid_until='2021-01-01')
        self.valid_payload = {
            'hotel': 'AirAsia Hotel',
            'description': 'Test package 1',
            'duration': 4,
            'price': 1500,
            'valid_until': '2022-01-01'
        }
        self.invalid_payload = {
            'Hotel': 100,
            'description': True,
            'duration': -1,
            'price': -1500,
            'valid_until': '2022-02-55'
        }

    def test_valid_update_package(self):
        response = client.put(
            '/package/'+str(self.package_1.pk)+'/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_package(self):
        response = client.put(
            '/package/'+str(self.package_1.pk)+'/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# DELETE
class DeleteSinglePackageTest(TestCase):
    
    def setUp(self):
        self.package_1 = Package.objects.create(description='TestPackage1', price=100, duration=2, valid_until='2021-01-01')
        self.package_2 = Package.objects.create(description='TestPackage2', price=100, duration=2, valid_until='2021-01-01')

    def test_valid_delete_package(self):
        response = client.delete('/package/'+str(self.package_1.pk)+'/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_package(self):
        response = client.delete('/package/-1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
