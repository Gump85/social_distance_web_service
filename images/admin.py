from django.contrib import admin
from .models import UploadImage


@admin.register(UploadImage)
class ImageAdmin(admin.ModelAdmin):
    """ регистрация модели UploadImage в панели администратора """
    list_display = ['image', 'created', 'coordinates', 'social_activity']
    list_filter = ['created']
