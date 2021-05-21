from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    poster_path = models.TextField(blank=True)
    movie_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100)

class MBTI(models.Model):
    MBTI_CHOICES = [
        ('INTJ', 'INTJ'),
        ('INTP', 'INTP'),
        ('ENTJ', 'ENTJ'),
        ('ENTP', 'ENTP'),
        ('INFJ', 'INFJ'),
        ('INFP', 'INFP'),
        ('ENFJ', 'ENFJ'),
        ('ENFP', 'ENFP'),
        ('ISTJ', 'ISTJ'),
        ('ISFJ', 'ISFJ'),
        ('ESTJ', 'ESTJ'),
        ('ESFJ', 'ESFJ'),
        ('ISTP', 'ISTP'),
        ('ISFP', 'ISFP'),
        ('ESTP', 'ESTP'),
        ('ESFP', 'ESFP'),
    ]
    mbti = models.CharField(max_length=4, choices=MBTI_CHOICES)
    movie = models.ManyToManyField(Movie, related_name='mbti')

    def __str__(self):
        return f'{self.mbti}'