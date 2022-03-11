from django.contrib import admin
from rango.models import UserProfile, Destination

# Register your models here.


'''
class PageAdmin(admin.ModelAdmin):
     list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
'''  

class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Destination, DestinationAdmin)
admin.site.register(UserProfile)

#admin.site.register(Category)
#admin.site.register(Page, PageAdmin)
