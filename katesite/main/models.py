from django.db import models




class Kate(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField
    images = models.ImageField(upload_to='storage')
