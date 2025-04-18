from django.db import models
from django.contrib.auth.models import User
import base64

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    avatar_url = models.URLField(max_length=255, blank=True, null=True)
    user_stats = models.JSONField(default=dict)  # Better for storing structured data
    is_active = models.BooleanField(default=True)

    def get_avatar_base64(self):
        if self.avatar_binary:
            return base64.b64encode(self.avatar_binary).decode('utf-8')
        return None

    def __str__(self):
        return f"{self.user_name} ({self.user.email})"

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
        ordering = ['-registration_date']