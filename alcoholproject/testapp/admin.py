from django.contrib import admin
from testapp.models import Alcohol
# Register your models here.
class AlcoholAdmin(admin.ModelAdmin):
    list_display = ['name','type','percent','price']

admin.site.register(Alcohol,AlcoholAdmin)