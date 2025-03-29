from django.db import models
from django.contrib.auth.models import User
import base64

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.BinaryField(null=True, blank=True)
    avatar_content_type = models.CharField(max_length=50, null=True, blank=True)

    def get_avatar_base64(self):
        if self.avatar:
            if isinstance(self.avatar, str):  # Если это строка, преобразуем в байты
                return base64.b64encode(self.avatar.encode('utf-8')).decode('utf-8')
            return base64.b64encode(self.avatar).decode('utf-8')  # Если это байты, кодируем напрямую
        return None

    def __str__(self):
        return self.user.username