from django.contrib import admin
from familiares.models import *

# Register your models here.
class familiarAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'edad')
    
admin.site.register(familiar, familiarAdmin)