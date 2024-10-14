from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from clientes.views import login_view,index_view,home_view,logout_view,register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    # URLs de restablecimiento de contraseña
    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url='/password_reset/done/'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=settings.PASSWORD_RESET_COMPLETE_URL),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),  # No se necesita la redirección aquí
         name='password_reset_complete'),
]
