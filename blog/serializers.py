from rest_framework import serializers

from .models import Post



class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at',)



class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at',)



class GetPostSerializer(serializers.ModelSerializer):

    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)
    user_vote = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'upvotes', 'downvotes', 'user_vote',)


    def get_user_vote(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            vote = obj.vote_set.filter(user=user).first()
            if vote:
                return vote.vote
        return 0