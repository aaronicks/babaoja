from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('update_user', views.update_user, name='update_user'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('product_list/<int:pk>', views.product_list, name='product_list'),
]
