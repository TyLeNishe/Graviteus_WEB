from django.urls import path, include
from .views import home
from .views import register
from .views import my_login
from .views import profile, home, update_email, update_username, delete_account
from .views import update_email
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', my_login, name='login'),
    path('profile/', profile, name='profile'),    
    path('update-email/', update_email, name='update_email'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), 
    path('update_username/', update_username, name='update_username'),
    path('delete-account/', delete_account, name='delete_account'),
    path('social-auth/', include('social_django.urls', namespace='social')), 
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('lor/', views.lor, name='lor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
