from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    title = request.query_params.get('title')
    if title:
        queryset = queryset.filter(title__icontains=title)
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Пост успешно создан")

@api_view(['GET'])
def post_detail(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['DELETE'])
def post_delete(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    post.delete()
    return Response("Пост успешно удален")

@api_view(['PUT', 'PATCH'])
def post_update(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    serializer = PostSerializer(instance=post, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Пост усешно обновлен")

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Комментарий успешно создан")

@api_view(['DELETE'])
def comment_delete(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    comment.delete()
    return Response("Комментарий успешно удален")

@api_view(['PUT', 'PATCH'])
def comment_update(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    serializer = CommentSerializer(instance=comment, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Комментарий усешно обновлен")
