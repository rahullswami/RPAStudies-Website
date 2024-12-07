from django.urls import path
from .views import *

urlpatterns = [
    path('',Base, name='home'),
    path('categories/all/',Category_page, name='category'),
    path('notes/all/',Nots_page,name='notes'),
    path('contacts/',Contact_us,name='contact'),
    path('profile/edit/<int:id>/',Edit_profile,name='edit_profile'),
    path('profile/delete/<int:id>/',Delete_profile,name='delete_profile'),
    path('upload/video/',video_upload,name='video_upload'),
    path('video/edit/<int:id>/',edit_video,name='edit_video'),
    path('delete/video//<int:id>/',delete_video,name='delete_video'),
    path('video/plyaing/<int:id>/', video_detail, name='video_detail'),
    path('upload/notes/', upload_notes, name='upload_notes'),
    path('edit/notes/<int:id>/', update_notes, name='update_notes'),
    path('delete/notes/<int:id>/', delete_notes, name='delete_notes'),
    path('detail/notes/<int:id>/', notes_detail, name='notes_detail'),




]