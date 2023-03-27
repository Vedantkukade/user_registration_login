from django.contrib import admin
from .models import userregister
# Register your models here.
@admin.register(userregister)
class data(admin.ModelAdmin):
    list_display=['username','fname','lname','dob','address1','address2','postal_code','phone_number']
