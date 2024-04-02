from django.contrib import admin
from app1.models import info , doctor
# Register your models here.
class signupadmin(admin.ModelAdmin):
    list_display=['phonenumber']
admin.site.register(info)
admin.site.register(doctor)