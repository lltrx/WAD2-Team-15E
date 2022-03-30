from django.test import SimpleTestCase
from django.urls import reverse, resolve
from destination.views import *

class Test_Ulrs(SimpleTestCase):

    def test_index_url(self):
        url = reverse('destination:index')
        self.assertEquals(resolve(url).func, index)
    
    def test_help_url(self):
        url = reverse('destination:help')
        self.assertEquals(resolve(url).func, help)
        
    def test_destination_menu_url(self):
        url = reverse('destination:destination_menu')
        self.assertEquals(resolve(url).func, destination_menu)
        
    def test_show_destination_url(self):
        url = reverse('destination:show_destination', args=['destination_name_slug'])
        self.assertEquals(resolve(url).func, show_destination)
        
    def test_edit_destination_url(self):
        url = reverse('destination:edit_destination', args=['destination_name_slug'])
        self.assertEquals(resolve(url).func, edit_destination)
        
    def test_like_destination_url(self):
        url = reverse('destination:like_destination', args=['destination_name_slug'])
        self.assertEquals(resolve(url).func, like_destination)
        
    def test_delete_destination_url(self):
        url = reverse('destination:delete_destination', args=['destination_name_slug'])
        self.assertEquals(resolve(url).func, delete_destination)
        
    def test_comment_destination_url(self):
        url = reverse('destination:comment_destination', args=['destination_name_slug'])
        self.assertEquals(resolve(url).func, comment_destination)
        
    def test_delete_comment_url(self):
        url = reverse('destination:delete_comment', args=['comment_pk'])
        self.assertEquals(resolve(url).func, delete_comment)
        
    def test_add_destination_url(self):
        url = reverse('destination:add_destination')
        self.assertEquals(resolve(url).func, add_destination)
        
    def test_register_url(self):
        url = reverse('destination:register')
        self.assertEquals(resolve(url).func, register)
        
    def test_login_url(self):
        url = reverse('destination:login')
        self.assertEquals(resolve(url).func, user_login)
        
    def test_logout_url(self):
        url = reverse('destination:logout')
        self.assertEquals(resolve(url).func, user_logout)
        
    def test_my_profile_url(self):
        url = reverse('destination:my_profile')
        self.assertEquals(resolve(url).func, my_profile)
        
    def test_user_profile_url(self):
        url = reverse('destination:user_profile', args=['username'])
        self.assertEquals(resolve(url).func, user_profile)
        
    def test_edit_profile_url(self):
        url = reverse('destination:edit_profile')
        self.assertEquals(resolve(url).func, edit_profile)
        
    def test_change_password_url(self):
        url = reverse('destination:change_password')
        self.assertEquals(resolve(url).func, change_password)
        
        
    