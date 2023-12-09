from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
