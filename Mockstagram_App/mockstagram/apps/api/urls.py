from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    SingleProfilePost, PostViewSet
)
router = DefaultRouter()
# See profiles and posts from all users when logged in
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('posts', PostViewSet, basename='posts')

# Interact with a specific profile or post
custom_urlpatterns = [url(r'profile/(?P<profile_pk>\d+)/posts/(?P<pk>\d+)$',
                          SingleProfilePost.as_view(),
                          name='single_profile_post')]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
