from django.contrib import admin
from rango.models import UserProfile, Destination

# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Destination, DestinationAdmin)
admin.site.register(UserProfile)

