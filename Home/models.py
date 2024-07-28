from django.db import models

# Create your models here.


class Home(models.Model):
    header_title = models.CharField(
        max_length=50, blank=True, verbose_name="Header Title")
    phone = models.CharField(max_length=30, blank=True,
                             verbose_name="Phone Number")
    location = models.CharField(
        max_length=30, blank=True, verbose_name="Location")
    open_worked = models.CharField(
        max_length=20, blank=True, verbose_name="Open Worked")
    our_story = models.TextField(blank=True, verbose_name="Our Story")
    our_slogan_title = models.CharField(
        max_length=120, blank=True, verbose_name="Our Slogan Title")
    our_slogan_left = models.TextField(
        blank=True, verbose_name="Our Slogan Left")
    our_slogan_right = models.TextField(
        blank=True, verbose_name="Our Slogan Right")
    our_team_des = models.CharField(
        max_length=250, blank=True, verbose_name="Meet Our Team Description")

    def __str__(self):
        return "Home Page"
