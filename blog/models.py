from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = (
        (0, "Draft"),
        (1, "Publish")
        )

LANGUAGE = (
        (0, "Korean"),
        (1, "English")
        )

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.TextField(null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    language = models.IntegerField(choices=LANGUAGE, default=0)
    post_pk = models.AutoField(primary_key=True)
    head_image = models.ImageField(upload_to = 'images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to = 'files/%y/%m/%d/', blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{self.post_pk}/"

    def get_head_image_url(self):
        return f"{self.head_image}"

class About(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    language = models.IntegerField(choices=LANGUAGE, default=0)

    def __str__(self):
        return self.title
