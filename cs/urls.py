from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch', views.fetch, name='fetch'),

    path('fetch_all', views.fetch_all, name='fetch_all'),
    path('all', views.all, name='all'),

]
