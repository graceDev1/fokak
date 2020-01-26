from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.ImageField(upload_to='image_uri', blank=True)
