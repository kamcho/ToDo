from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('create/',CreateTask.as_view(),name='create' ),
    path('', TaskList.as_view(), name='tasks'),
    path('MyTasks/<int:pk>/info/', UpdateTask.as_view(), name='info'),
    path('delete/', DeleteTask.as_view(), name='delete'),

]