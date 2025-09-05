from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
from tweetapp.forms import AddTweetForm

# Create your views here.
def listtweets(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict ={"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweets(request):
    if request.method == "POST":
        tweet_nick = request.POST["nickname"]
        tweet_massage = request.POST["post_massage"]
        models.Tweet.objects.create(nick_name=tweet_nick, massage=tweet_massage)
        return redirect(reverse('tweetapp:listtweets'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    

def addtweetbyform(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["name_input"]
            massege = form.cleaned_data["massage_input"]
            models.Tweet.objects.create(nick_name = nickname, massage = massege)
            return redirect(reverse('tweetapp:listtweets'))
        else:
            return render(request, 'tweetapp/addtweetbyform.html',context={'form':form})
    else:
        form = AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html',context={'form':form})    

        