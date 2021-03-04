
from rest_framework import serializers
from .models import User, Blog, Comment

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many=True,
        read_only=True 
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 
        'firstname', 'lastname', 'description', 'profile_picture', 'blogs')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'user', 'text')


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'user', 'title', 'image', 'body', 'comments')
