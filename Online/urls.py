from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='signup'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile-detail'),

    path('category/', FollowViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', FollowViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),

    path('carmake/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='carmake-list'),
    path('carmake/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='carmake-detail'),

    path('model/',PostLikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='model-list'),
    path('model/<int:pk>/', PostLikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='model-detail'),

    path('car/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('car/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car-detail'),

    path('bet/', CommentLikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='bet-list'),
    path('bet/<int:pk>/', CommentLikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bet-detail'),

    path('comment/', StoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comment/<int:pk>/', StoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),

    path('bet/', GroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='bet-list'),
    path('bet/<int:pk>/', GroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='bet-detail'),
]