from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('graviapps.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
