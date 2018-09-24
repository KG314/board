from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover


# Create your models here.
class User(AbstractUser):
    pass
    

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='topics', null = True)
    #created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    first_post = models.TextField(default='最初の投稿')

    def __str__(self):
        return self.topic_name


class Post(models.Model):
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    posted_by = models.ForeignKey(User, related_name='posts', null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    image_upload = models.ImageField(upload_to='images', null=True, blank=True)
    image_thumbnail = ImageSpecField(
        source='image_upload',
        processors=[ResizeToCover(150, 150)],
        format='JPEG',
        options={'quality': 60}
    )



