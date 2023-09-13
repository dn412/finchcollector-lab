from django.urls import path
from . import views
# this file is how we're going to map our urls to views
# remember in django, views are like our controllers
# the `name='home'` is a kwarg, that gives the route a name. naming routes is optional, but best practices
# later on, we'll see just how useful this is.
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
]