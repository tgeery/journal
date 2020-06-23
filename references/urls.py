from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('entry_1', views.entry_1, name='entry_1'),
        path('entry_2', views.entry_2, name='entry_2')
        ]
