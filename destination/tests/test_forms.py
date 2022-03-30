from django.test import TestCase
from destination.forms import *


class Test_forms(TestCase):
    
    def test_destination_form_vaild_data(self):
        form = DestinationForm(data={'name': 'Test Destination',
                                     'description': 'Test Description',
                                     'image': 'Test Image',
                                     'destination_type': 'Test Destination Type'
                                     })
        
        self.assertFalse(form.is_valid())
    
    def test_destination_form_invalid_data(self):
        form = DestinationForm(data={ })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        
        
    def test_registration_form_valid_data(self):
        form = RegistrationForm(data={'username': 'Test Username',
                                      'first_name': 'Test First Name',
                                      'last_name': 'Test Last Name',
                                      'email': 'Test Email',
                                      'password1': 'Test Password',
                                      'password2': 'Test Password' })
        
        self.assertFalse(form.is_valid())
        
    def test_registration_form_invalid_data(self):
        form = RegistrationForm(data={ })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
        
    def test_user_profile_form_valid_data(self):
        form = UserProfileForm(data={'picture': 'Test Picture',
                                     'about': 'Test About' })
        
        self.assertTrue(form.is_valid())
        
    def test_user_profile_form_invalid_data(self):
        form = UserProfileForm(data={ })
        
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
        
    def test_user_profile_change_form_valid_data(self):
        form = UserProfileChangeForm(data={'picture': 'Test Picture',
                                           'about': 'Test About' })
        
        self.assertTrue(form.is_valid())
        
    def test_user_profile_change_form_invalid_data(self):
        form = UserProfileChangeForm(data={ })
        
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
        
    def test_edit_profile_form_valid_data(self):
        form = EditProfileForm(data={'email': 'Test Email',
                                     'first_name': 'Test First Name',
                                     'last_name': 'Test Last Name' })
        
        self.assertFalse(form.is_valid())
        
    def test_edit_profile_form_invalid_data(self):
        form = EditProfileForm(data={ })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        
    def test_comment_form_valid_data(self):
        form = CommentForm(data={'comment': 'Test Comment'})
        
        self.assertFalse(form.is_valid())
        
    def test_comment_form_invalid_data(self):
        form = CommentForm(data={ })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        
        
        