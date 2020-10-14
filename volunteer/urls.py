from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.myschedule, name='myschedule'),
    path('post/', views.createpost, name='createpost')
]