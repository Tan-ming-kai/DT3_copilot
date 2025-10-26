from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

# Create your models here.
