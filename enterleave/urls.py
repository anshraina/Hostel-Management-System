from django.urls import path
from . import views


urlpatterns = [
 path('entry_exit', views.entry_exit, name='entry_exit'),

]
