from django.test import TestCase
from .models import Package

class PackageTest(TestCase):
    def setUp(self):
        Package.objects.create(description='TestPackage1', price=100, duration=2, valid_until='2021-01-01')
        Package.objects.create(description='TestPackage2', price=200, duration=2, valid_until='2021-01-01')

    def test_packages(self):
        package_1 = Package.objects.get(description='TestPackage1')
        package_2 = Package.objects.get(description='TestPackage2')
        self.assertEqual(
            package_1.description, "TestPackage1")
        self.assertEqual(
            package_2.description, "TestPackage2")