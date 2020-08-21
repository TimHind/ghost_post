from django.db import models
from django.db import IntegrityError
#from django.contrib.auth.models import User
#from django.utils import timezone

class Joke(models.Model):
    JOKE_CHOICES = [
        ('Roast', 'Roast'),
        ('Boast', 'Boast')
    ]
    #TIMEZONE='America/Indianapolis'
    body = models.CharField(max_length=280)
    joke_type = models.BooleanField()
    #upvote = models.IntegerField()
    #downvote = models.IntegerField()
    #votes = models.ManyToManyField(User, related_name="joke_like")
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    @property
    def total_likes(self):
        return self.upvote + self.downvote

    class Meta:
        ordering = ['-time',]

    def __str__(self):
        return self.body
