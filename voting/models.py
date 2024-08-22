from django.db import models

from blog.models import Post
from user_account.models import CustomUser

class Vote(models.Model):
    VOTE_CHOICES = (
        (1, 'Upvote'),
        (-1, 'Downvote'),
        (0, 'No Vote')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    vote = models.IntegerField(choices=VOTE_CHOICES, default=0)

    class Meta:
        unique_together = ('user', 'post')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



    
    def total_upvote(self):
        return self.vote_set.filter(vote=1).count()
    
    
        
    def display_downvote(self):
        if self.vote_set.filter(vote=-1).sum() <= 0:
            return 0
        self.total_upvote()


    def user_vote(self, user):
        try:
            return self.vote_set.get(user=user).vote
        except self.vote.DoesNotExist:
            return 0
        

    def add_vote(self, user, value):
        vote, created = Vote.objects.update_or_create(
            post=self, user=user,
            defaults={'vote': value}
        )
        return vote