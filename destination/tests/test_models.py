from django.test import TestCase
from destination.models import Destination, Comment, UserProfile

class Test_models(TestCase):
    
    def setUp(self):
        self.d = Destination.objects.create(
            name='Test Destination',
            description='Test Description',
            image='Test Image',
            destination_type='Test Destination Type',
        )
        
    def test_destination_model(self):
        d = Destination.objects.get(id=1)
        self.assertEqual(d.name, 'Test Destination')
        self.assertEqual(d.description, 'Test Description')
        self.assertEqual(d.image, 'Test Image')
        self.assertEqual(d.destination_type, 'Test Destination Type')
        
    def test_total_likes(self):
        d = Destination.objects.get(id=1)
        self.assertEqual(d.total_likes(), 0)
        
