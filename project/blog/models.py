from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images",blank= True,null= True)
    author = models.CharField(max_length= 100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title