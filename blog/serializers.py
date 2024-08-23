from rest_framework import serializers

from .models import Post



class FeedSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author_username', 'title', 'body', 'created_at', 'upvotes', 'downvotes',)

    def get_upvotes(self, obj):
        return obj.votes.filter(vote=1).count()

    def get_downvotes(self, obj):
        return obj.votes.filter(vote=-1).count()


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body', 'created_at',)



class GetPostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author_username', 'title', 'body', 'created_at', 'upvotes', 'downvotes',)

    def get_upvotes(self, obj):
        return obj.votes.filter(vote=1).count()

    def get_downvotes(self, obj):
        return obj.votes.filter(vote=-1).count()
    


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('author_username', 'title', 'body', 'created_at', 'category', 'upvotes', 'downvotes',)

    def get_upvotes(self, obj):
        return obj.votes.filter(vote=1).count()

    def get_downvotes(self, obj):
        return obj.votes.filter(vote=-1).count()