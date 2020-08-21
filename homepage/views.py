from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from homepage.models import Joke
from homepage.forms import AddJokeForm

def index(request):
    my_jokes = Joke.objects.all()
    return render(request, "index.html", {"jokes": my_jokes})

def jokes_votes(request, post_id):
    joke = get_object_or_404(Joke, id='post_id')
    total_likes = joke.total_likes()
    return render(request, "index.html", {"total_likes": total_likes})

def process_vote(request, pk):
    joke = Joke.objects.get(id=pk) 
    joke.upvote = joke.upvote + 1
    joke.save()
    return HttpResponseRedirect(reverse("homepage"))

def process_unvote(request, pk):
    joke = Joke.objects.get(id=pk) 
    joke.upvote = joke.upvote - 1
    joke.save()
    return HttpResponseRedirect(reverse("homepage"))

def boast_view(request):
    jokes = Joke.objects.filter(joke_type=False).order_by('-time')
    return render(request, "boast_view.html", {"jokes": jokes})

def roast_view(request):
    jokes = Joke.objects.filter(joke_type=True).order_by('-time')
    return render(request, "roast_view.html", {"jokes": jokes})

def sorted_jokes(request):
    jokes = Joke.objects.all()#order_by()
    jokes = list(jokes)
    jokes = sorted(jokes, key=lambda t:t.total_likes, reverse=True)
    return render(request, "sorted.html", {"jokes": jokes})
    
def add_joke(request):
    if request.method == "POST":
        form = AddJokeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Joke.objects.create(
                body = data.get("body"),
                joke_type = data.get("joke_type"),    
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddJokeForm()
    return render(request, "add_joke.html", {"form": form})

