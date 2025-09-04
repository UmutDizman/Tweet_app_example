from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweets, name='listtweets'),
    path('addtweet/', views.addtweets, name='addtweets'),
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'),
]
