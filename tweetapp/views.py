from django.shortcuts import render,redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm, AddtweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView 

# Create your views here.
def listtweets(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict ={"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(pk=id).delete()
        return redirect("tweetapp:listtweets")




@login_required(login_url='/login')
def addtweets(request):
    if request.method == "POST":
        tweet_massage = request.POST["post_massage"]
        models.Tweet.objects.create(username = request.user, massage=tweet_massage)
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


def addtweetmodelform(request):
    if request.method == "POST":
        form = AddtweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nick_name"]
            massege = form.cleaned_data["massage"]
            models.Tweet.objects.create(nick_name = nickname, massage = massege)
            return redirect(reverse('tweetapp:listtweets'))
        else:
            return render(request, 'tweetapp/addtweetbymodelform.html',context={'form':form})
    else:
        form = AddtweetModelForm()
        return render(request, 'tweetapp/addtweetbymodelform.html',context={'form':form})  

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"

    