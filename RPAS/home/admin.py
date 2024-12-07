from django.contrib import admin
from .models import *

admin.site.register(User_Profile)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

@admin.register(PDFNotes)
class PDFNotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')