from django.db import models
from django.contrib.auth.models import User

# Models
class Task(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True, auto_now_add=True)
    title = models.CharField(null=True, max_length=350)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title