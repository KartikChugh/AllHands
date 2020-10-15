from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('volunteer/', views.index, name='index'),
    path('volunteer/schedule/', views.myschedule, name='myschedule'),
    path('volunteer/post/', views.createpost, name='createpost')
]