from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['post', 'vote']

    def validate_vote(self, value):
        if value not in (-1, 1):
            raise serializers.ValidationError("Vote must be either -1 (Downvote) or 1 (Upvote).")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']
        vote_value = validated_data['vote']

        vote, created = Vote.objects.update_or_create(
            user=user, post=post,
            defaults={'vote': vote_value}
        )
        return vote
