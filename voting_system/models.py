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
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    vote = models.IntegerField(choices=VotingChoice, default=0)

    def display_upvotes(self):
        return Vote.objects.filter(vote=Vote.VotingChoice.UPVOTE).count()

    def display_downvotes(self):    
        return Vote.objects.filter(vote=Vote.VotingChoice.DOWNVOTE).count()

    def get_vote(self, user, value):
        vote, created = Vote.objects.update_or_create(user=user, defaults={'vote': value})
        if not created:
            vote.vote = value
            vote.save()
        return vote