from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer


# ==========================================================================
#
#   ProfileViewSet:
#       - Allow a logged in user to GET, UPDATE, & DELETE their profile
#       - Unauthenticated requests will not be processed
# ==========================================================================
class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        print("print:ProfileVIewSet:getQuerySet")
        print("self = ", self)
        return Profile.objects.all().filter(is_public=True)

    # Auth Required???
    def create(self, request):
        profile = Profile.objects.filter(owner=request.user)
        print("print:ProfileVIewSet:create")
        if profile:
            raise ValidationError("A profile already exists for this user")
        return super().create(request)

    # Auth Required
    def destroy(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        print("print:ProfileVIewSet:destroy")
        if not request.user == profile.owner:
            raise PermissionDenied("You do not have the permissions needed to delete this profile")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ==========================================================================
#
#   ProfilePosts:
#       - Allow a logged in user to GET all of the posts linked to their
#         profile / account
#       - Unauthenticated requests will not be processed
# ==========================================================================
class ProfilePosts(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        print("print:ProfilePosts:getQuerySet")
        if self.kwargs.get('profile_pk'):
            profile = Profile.objects.get(pk=self.kwargs['profile_pk'])
            queryset = Post.objects.filter(owner=self.request.user, profile=profile)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ==========================================================================
#
#   SingleProfilePost:
#       - Allow a logged in user to GET a single post from their profile
#       - Unauthenticated requests will not be processed
# ==========================================================================
class SingleProfilePost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        print("print:SingleProfilePost:get_queryset")
        if self.kwargs.get("profile_pk") and self.kwargs.get('pk'):
            profile = Profile.objects.get(pk=self.kwargs['profile_pk'])
            queryset = Post.objects.filter(pk=self.kwargs['pk'], owner=self.request.user, profile=profile)
        return queryset


# ==========================================================================
#
#   PostViewSet:
#       - Allow a logged in user to GET, UPDATE, & DELETE their profile
#       - Unauthenticated requests will not be processed
# ==========================================================================
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        print("print:PostViewSet:get_queryset")
        return Post.objects.all().filter(owner=self.request.user)

    # Login Required
    def create(self, request, *args, **kwargs):
        print("print:PostViewSet:create")
        if request.user.is_anonymous:
            raise PermissionDenied("You need to create an account or login before creating a post")
        return super().create(request, *args, **kwargs)

    # Auth Required
    def destroy(self, request, *args, **kwargs):
        print("print:PostViewSet:destroy")
        post = Post.objects.get(pk=self.kwargs['pk'])
        if not request.user == post.owner:
            raise PermissionDenied("You do not have the permissions needed to delete this post")
        return super().destroy(request, *args, **kwargs)

    # Auth Required
    def update(self, request, *args, **kwargs):
        print("print:PostViewSet:update")
        post = Post.objects.get(pk=self.kwargs['pk'])
        if not request.user == post.owner:
            raise PermissionDenied("You do not have the permissions needed to modify this post")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
