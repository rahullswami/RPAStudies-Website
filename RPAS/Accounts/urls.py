from django.urls import path, include
from .views import login_page, register_page, logout_page

urlpatterns = [
    path('login/page/', login_page, name='login_page'),
    path('register/page/', register_page, name='register_page'),
    path('logout/page',logout_page, name='logout_page')
]