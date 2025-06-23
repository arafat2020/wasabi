from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI
from .views import LoginAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('login/', LoginAPI.as_view(), name='login'),
]
