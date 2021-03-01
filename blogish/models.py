from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    profile_picture = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.username



class Blog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField()