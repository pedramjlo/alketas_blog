from django.db import models

from user_account.models import CustomUser
from blog.models import Post



class Vote(models.Model):
    VotingChoice = (
        (1, "Upvote"),
        (0, "No Vote"),
        (-1, "Downvote")
        )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.PROTECT)
    vote = models.IntegerField(choices=VotingChoice, default=0)

    def display_upvotes(self):
        return Vote.objects.filter(vote=1).count()

    def display_downvotes(self):    
        return Vote.objects.filter(vote=-1).count()

    def get_vote(self, user, value):
        vote, created = Vote.objects.update_or_create(user=user, defaults={'vote': value})
        if not created:
            vote.vote = value
            vote.save()
        return vote
    

    def __str__(self):
        return f"{self.user} {(self.get_vote_display()).lower()}d '{self.post.title}'"