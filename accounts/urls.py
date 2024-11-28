from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),

    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),

    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),

    # パスワードリセット用のURLパターン
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
