from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout")
]
