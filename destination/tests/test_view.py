from django.test import TestCase, Client
from django.urls import reverse
from destination.models import Destination, Comment, UserProfile
import json

class Test_Views(TestCase):
  
    
    def test_index(self):
        response = self.client.get(reverse('destination:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/index.html')
        
    def test_help(self):
        response = self.client.get(reverse('destination:help'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/help.html')
        
    def test_destination_menu(self):
        response = self.client.get(reverse('destination:destination_menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/destination_menu.html')
        
    def test_show_destination(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/destination.html')
        
    def test_edit_destination(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/destination.html')
        
    def test_like_destination(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_destination(self):
        response = self.client.get(reverse('destination:destination_menu'))
        self.assertEqual(response.status_code, 200)
        
    def test_comment_destination(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
        
    def test_delete_comment(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
        
    def test_add_destination(self):
        response = self.client.get(reverse('destination:show_destination', args=['destination_name_slug']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/destination.html')
        
    def test_register(self):
        response = self.client.get(reverse('destination:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/register.html')      
        
    def test_login(self):
        response = self.client.get(reverse('destination:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination/login.html')
        
    def test_logout(self):
        response = self.client.get(reverse('destination:index'))
        self.assertEqual(response.status_code, 200)


    def test_my_profile(self):
        self.assertTemplateUsed( 'destination/my_profile.html')
        
    def test_user_profile(self):
        self.assertTemplateUsed( 'destination/user_profile.html')
        
    def test_edit_profile(self):
        response = self.client.get(reverse('destination:edit_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed( 'destination/edit_profile.html')
        
    def test_change_password(self):
        response = self.client.get(reverse('destination:my_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed( 'destination/change_password.html')
        
    