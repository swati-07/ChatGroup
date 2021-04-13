from django.urls import path
from . import views
app_name='Chat'
urlpatterns=[
	path('',views.indexview,name='index'),
	path('<str:room_name>/',views.roomview,name='room'),
]