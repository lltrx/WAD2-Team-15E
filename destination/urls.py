from django.urls import path
from destination import views
from django.conf.urls import url


app_name = 'destination'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('destination_menu/', views.destination_menu, name='destination_menu'),
    path('destination/<slug:destination_name_slug>/', views.show_destination, name='show_destination'),
    path('destination/<slug:destination_name_slug>/edit/', views.edit_destination, name='edit_destination'),
    path('destination/<slug:destination_name_slug>/like_destination/', views.like_destination, name='like_destination'),
    path('destination/<slug:destination_name_slug>/delete_destination/', views.delete_destination, name='delete_destination'),
    path('destination/<slug:destination_name_slug>/comment_destination/', views.comment_destination, name='comment_destination'),
    path('delete_comment/<str:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('user_profile/<slug:username>/', views.user_profile, name='user_profile'),
    path('my_profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
] 
