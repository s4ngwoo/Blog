from django.db import models
from django.contrib.auth.models import User
# Create your models here.


BRANCH = (
        (0, "Draft"),
        (1, "Publish")
        )

LANGUAGE = (
        (0, "Korean"),
        (1, "English")
        )

class TitleContent(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(null=True, blank=True)
    class Meta:
        abstract = True
    def __str__(self):
        return f"{self.title}"

class HeadImage(models.Model):
    head_image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    class Meta:
        abstract = True
    def get_head_image_url(self):
        return f"{self.head_image}"

class TimeLogger(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class PostCategory(TitleContent, TimeLogger, HeadImage):
    pass

class PostSeries(TitleContent, TimeLogger, HeadImage):
    pass

class PostTag(TitleContent, TimeLogger):
    title = models.CharField(max_length=50, unique=True)

class Post(TitleContent, TimeLogger, HeadImage):
    subtitle = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blog_posts')
    branch = models.IntegerField(choices=BRANCH, default=0)
    language = models.IntegerField(choices=LANGUAGE, default=0)
    category = models.ForeignKey('PostCategory', on_delete=models.PROTECT, related_name='post_category', null=True, blank=True)
    series = models.ForeignKey('PostSeries', on_delete=models.PROTECT, related_name='post_series', null=True, blank=True)
    tag = models.ForeignKey('PostTag', on_delete=models.PROTECT, related_name='post_tag', null=True, blank=True)
    def __str__(self):
        return f"[{self.pk}]:{self.title}"
    def get_absolute_url(self):
        return f"{self.pk}/"


class About(TitleContent, TimeLogger):
    language = models.IntegerField(choices=LANGUAGE, default=0)
