from django.contrib.auth.models import User
from django.db import models
import base64

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.BinaryField(null=True, blank=True)
    avatar_content_type = models.CharField(max_length=50, null=True, blank=True)

    def get_avatar_base64(self):
        if self.avatar:
            return base64.b64encode(self.avatar).decode('utf-8')
        return None
    def __str__(self):
        return self.user.username