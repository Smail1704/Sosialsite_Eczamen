from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import *
from .filters import FollowFilter
from allauth.account.views import SignupView


class AccountSignupView(SignupView):
    template_name = "users/custom_signup.html"
    account_signup_view = AccountSignupView.as_view()


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FollowFilter
    search_fields = ['license_number']


class PostViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostLikeSerializer


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostLikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer


class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentLikeSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StorySerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupSerializer
