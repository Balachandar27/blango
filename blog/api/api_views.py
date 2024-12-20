# class option 3 
from rest_framework import generics
from blog.models import Post
from blog.api.serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class option 2
# from rest_framework import mixins
# from rest_framework import generics


# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class PostDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
    
#         return self.destroy(request, *args, **kwargs)

# class option 1
# import json
# from http import HTTPStatus

# from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from blog.models import Post
# from blog.app.serializers import PostSerializer
# from django.short

# class PostDetail(APIView):
#     @staticmethod
#     def get_post(pk):
#         return get_object_or_404(Post, pk=pk)

#     def get(self, request, pk, format=None):
#         post = self.get_post(pk)
#         return Response(PostSerializer(post).data)

#     def put(self, request, pk, format=None):
#         post = self.get_post(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_post(pk)
#         post.delete()
#         return Response(status=HTTPStatus.NO_CONTENT)