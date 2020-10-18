from django.urls import path

from . import views

app_name = 'volunteer'
urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.myschedule, name='myschedule'),
    path('post/', views.CreateVolunteerEventView.as_view(), name='createpost'),
    path('events/', views.EventBrowseView.as_view(), name='eventbrowse')
]