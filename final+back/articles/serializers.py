from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'username', )

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('user', )

class CommentSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)  # 또는 user.username

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', ]
