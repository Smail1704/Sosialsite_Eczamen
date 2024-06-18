from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    website = models.URLField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followers_set', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='following_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='liked_posts')
    hashtag = models.CharField(max_length=55)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='liked_comments')


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images/')
    video = models.FileField(upload_to='story_videos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    members = models.ManyToManyField(UserProfile, related_name='groups')
    join_key = models.CharField(max_length=10, unique=True)
