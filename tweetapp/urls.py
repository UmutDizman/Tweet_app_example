from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweets, name='listtweets'),
    path('addtweet/', views.addtweets, name='addtweets'),
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform/', views.addtweetmodelform, name='addtweetbymodelform'),
    path('singup/',views.SingUpView.as_view(),name='singup'),
    path("deletetweet/<int:id>",views.deletetweet, name='deletetweet'),
]
