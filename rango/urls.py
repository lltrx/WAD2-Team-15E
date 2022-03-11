from django.urls import path
from rango import views
from django.conf.urls import url

app_name = 'rango'

urlpatterns = [
    # Need to be change for our Project
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('destination/', views.destination, name='destination'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

'''
urlpatterns = [
    # Need to be change for our Project
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
]
'''