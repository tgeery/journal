from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('entry_1', views.entry_1, name='entry_1'),
        path('entry_2', views.entry_2, name='entry_2'),
        path('entry_3', views.entry_3, name='entry_3'),
        path('entry_4', views.entry_4, name='entry_4'),
        path('entry_5', views.entry_5, name='entry_5'),
	path('entry_6', views.entry_6, name='entry_6'),
	path('entry_7', views.entry_7, name='entry_7'),
        ]