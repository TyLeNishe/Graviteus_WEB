from django.urls import path
from . import views
from .views import home, about
from .views import SignUp
from .views import LogIn
from .views import profile, home, update_email, update_username, delete_account
from .views import update_email
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import Shop

urlpatterns = [
    path('', home, name='home'),
    path('SignUp/', SignUp, name='SignUp'),
    path('LogIn/', LogIn, name='LogIn'),
    path('profile/', profile, name='profile'),
    path('update-email/', update_email, name='update_email'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('update_username/', update_username, name='update_username'),
    path('delete-account/', delete_account, name='delete_account'),
    path('shop/', Shop, name='shop'),
    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)