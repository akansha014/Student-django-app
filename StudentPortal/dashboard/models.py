from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.date}"

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"


class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.subject}, {self.title}, {self.description}, {self.date}, {self.is_finished}"

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.date}, {self.is_finished}"
