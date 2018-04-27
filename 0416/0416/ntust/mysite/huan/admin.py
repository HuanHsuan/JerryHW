from django.contrib import admin

# Register your models here.
from .models import Profile,Introduction,Hobby

admin.site.register(Hobby)
admin.site.register(Introduction)
admin.site.register(Profile)