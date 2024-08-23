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
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VotingChoice, default=0)
    open_to_vote = models.BooleanField(default=True)

    def display_upvotes(self):
        return Vote.objects.filter(post=self.post, vote=1).count()

    def display_downvotes(self):    
        return Vote.objects.filter(post=self.post, vote=-1).count()
    
    def karma_count(self):
        return self.display_upvotes() - self.display_downvotes() 

    def vote_up(self):
        self.vote = 1
        self.save()
        return self
    
    def vote_down(self):
        self.vote = -1
        self.save()
        return self
    
    def revert_vote(self):
        self.vote = 0
        self.save()
        return self

    def __str__(self):
        return f"{self.user} {(self.get_vote_display()).lower()}d '{self.post.title}'"