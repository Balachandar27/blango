# class option 3 
from rest_framework import generics, viewsets
from blog.models import Post, Tag
from blango_auth.models import User
from blog.api.serializers import (
    PostSerializer, 
    UserSerializer, 
    PostDetailSerializer,
    TagSerializer,
    )
# from rest_framework import permissions
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from rest_framework.decorators import action
from rest_framework.response import Response

# cahching imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.http import Http404
from blog.api.filters import PostFilterSet

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        page = self.paginate_queryset(tag.posts)
        if page is not None:
            post_serializer = PostSerializer(tag.posts, many=True, context={"request": request})
            return self.get_paginated_response(post_serializer.data)
        post_serializer = PostSerializer(tag.posts, many=True, context={"request": request})
        return Response(post_serializer.data)
    
    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(cache_page(300))
    def get(self, *args, **kwargs):
        return super(UserDetail, self).get(*args, *kwargs)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    filterset_class = PostFilterSet
    ordering_fields = ["published_at", "author", "title", "slug"]
    # filterset_fields = ["author", "tags"]
    # existing attributes and methods omitted

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            # published only
            queryset = self.queryset.filter(published_at__lte=timezone.now())

        elif self.request.user.is_staff:
            # allow all
            queryset = self.queryset

        else:
        # filter for own or
            queryset = self.queryset.filter(Q(published_at__lte=timezone.now()) | Q(author=self.request.user))
        
        time_period_name = self.kwargs.get("period_name")

        if not time_period_name:
            # no further filtering required
            return queryset

        if time_period_name == "new":
            return queryset.filter(published_at__gte=timezone.now() - timedelta(hours=1))
        elif time_period_name == "today":
            return queryset.filter(published_at__date=timezone.now().date(),)
        elif time_period_name == "week":
            return queryset.filter(published_at__gte=timezone.now() - timedelta(days=7))
        else:
            raise Http404(f"Time period {time_period_name} is not valid, should be " f"'new', 'today' or 'week'")

    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @method_decorator(vary_on_cookie)
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = PostSerializer(posts, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)
    
        @method_decorator(cache_page(120))
        @method_decorator(vary_on_headers("Authorization", "Cookie"))
        def list(self, *args, **kwargs):
            return super(PostViewSet, self).list(*args, **kwargs)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


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