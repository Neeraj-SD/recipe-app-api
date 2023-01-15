from django.contrib import admin
from uploader import models



# Register your models here.
@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['upload_file', 'upload_date']
    ordering = ['-upload_date']

