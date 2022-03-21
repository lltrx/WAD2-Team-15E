from django.contrib import admin
from destination.models import UserProfile, Destination

# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class UserProfileAdmin(admin.ModelAdmin):
    profile_list = ('user' , 'about', 'picture')

    def user_about(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by( 'user')
        return queryset

    user_about.description = 'about'

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Destination, DestinationAdmin)


