from django.urls import path

from . import views

app_name = 'volunteer'
urlpatterns = [
    path('volunteer/events/', views.EventBrowseView.as_view(), name='eventbrowse'),
    path('', views.login, name='login'),
    path('volunteer/', views.index, name='index'),
    path('volunteer/schedule/', views.myschedule, name='myschedule'),
    path('volunteer/post/', views.CreateVolunteerEventView.as_view(), name='createpost'),
    path('volunteer/signup/<pk>', views.signup, name='signup'),
    path('volunteer/unregister/<pk>', views.unregister, name='unregister'),
    path('volunteer/events/<pk>', views.DetailView.as_view(), name='detail'),
    path('volunteer/myevents/', views.myevents, name='myevents'),
    path('volunteer/myevents/<pk>', views.EventDetailView.as_view(), name='detailmyevent'),
    path('volunteer/delete/<pk>', views.delete, name='delete'),

    # path('volunteer/eventfinder/', views.eventfinder, name='eventfinder')
]