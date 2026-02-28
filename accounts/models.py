from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.email


class StrayReport(models.Model):

    URGENCY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    state = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    local_body = models.CharField(max_length=200,null=True)

    location = models.CharField(max_length=255,null=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    dog_count = models.CharField(max_length=50, null=True, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    description = models.TextField(null=True)
    urgency = models.CharField(max_length=20,null=True,choices=URGENCY_CHOICES)

    reporter_name = models.CharField(max_length=100,null=True)
    reporter_phone = models.CharField(max_length=20,null=True)
    reporter_email = models.EmailField(null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending',null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Stray Report at {self.location} by {self.user.username}"
