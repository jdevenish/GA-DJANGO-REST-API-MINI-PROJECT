from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet, ProfilePosts,
    SingleProfilePost, PostViewSet
)
router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('posts', PostViewSet, basename='posts')

custom_urlpatterns = [
    url(r'profiles/(?P<profile_pk>\d+)/posts$', ProfilePosts.as_view(), name='profile_posts'),
    url(r'profile/(?P<profile_pk>\d+)/posts/(?P<pk>\d+)$', SingleProfilePost.as_view(), name='single_profile_post')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
