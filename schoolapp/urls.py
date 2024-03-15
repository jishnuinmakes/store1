from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('details', views.details, name='details'),
    path('get-courses/', views.get_courses, name='get_courses'),
    path('success/', views.success, name='success'),

]
