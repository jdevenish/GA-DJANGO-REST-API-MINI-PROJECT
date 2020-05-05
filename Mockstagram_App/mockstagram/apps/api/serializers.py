from rest_framework import serializers
from apps.api.models import Profile, Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # profile = serializers.ReadOnlyField(source='profile.owner.username')

    class Meta:
        model = Post
        fields = ('id',
                  'name',
                  'url',
                  'owner',
                  'description',
                  'profile',
                  'created_at',
                  'updated_at',
                  'is_public',
                  )


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = PostSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Profile
        fields = ('id',
                  'owner',
                  'description',
                  'created_at',
                  'updated_at',
                  'posts',
                  )
