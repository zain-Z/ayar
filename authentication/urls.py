from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path
from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView,\
    VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, \
    RequestPasswordResetEmail, UserListView, UserDetailView, WorkListAPIView, WorkDetailAPIView


urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('register/', RegisterView.as_view(), name="register"),
    path('work', WorkListAPIView.as_view(), name="work"),
    path('work/<int:id>', WorkDetailAPIView.as_view(),
         name="work-partial-id"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),

]
