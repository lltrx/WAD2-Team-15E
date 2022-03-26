
from django.contrib import admin
from django.urls import path
from django.urls import include
from destination import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.index, name='index'),
     path('', include('destination.urls')),
     path('admin/', admin.site.urls),
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='destination/password_reset.html'), 
          name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='destination/password_reset_done.html' ),
         name='password_reset_done'),
     path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='destination/password_reset_confirm.html'),
         name='password_reset_confirm'),
     path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view( template_name='destination/password_reset_complete.html' ),
         name='password_reset_complete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
