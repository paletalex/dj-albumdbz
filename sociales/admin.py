from django.contrib import admin
from .models import Social
# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'link']

admin.site.register(Social, SocialAdmin)