from django.db import models

# Create your models here.
class Message(models.Model):

    message = models.TextField() #formでtext area

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    screen_name = models.CharField(max_length=128)
    follower_count = models.IntegerField()
    follow_count = models.IntegerField()
    descriptionn = models.TextField()
