from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list_create(request):
    print('tt')
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({'message': '삭제 완료!'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_comment_list_create(request, article_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article_id).order_by('pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article_id=article_id)
            return Response(serializer.data, status=201)
        
# 댓글 단일 조회/수정/삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_comment_detail_update_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, article_id=article_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': '댓글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
