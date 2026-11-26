from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending' ,choices=[('pending', 'pending'), ('in_progress', 'in_progress'), ('completed', 'completed')])
    priority = models.CharField(max_length=10, default='medium',choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')])
    due_date = models.DateTimeField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)