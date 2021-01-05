from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    role = models.CharField(max_length = 300)
    fb_link = models.CharField(max_length = 300)
    insta_link = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to = "media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length = 255)
    subtitle = models.CharField(max_length = 255)
    button_text = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to ='media/Slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    site = models.CharField(max_length = 500,default="https://www.google.com")

    def __str__(self):
        return self.headline
