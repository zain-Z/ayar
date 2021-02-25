from django.urls import path
from . import views


urlpatterns = [
    path('personalinfo', views.PersonalInfoListAPIView.as_view(), name="personalinfo"),
    path('personalinfo/<int:id>', views.PersonalInfoDetailAPIView.as_view(),
         name="personalinfo-partial-id"),

    path('language', views.LanguageListAPIView.as_view(), name="language"),
    path('language/<int:id>', views.LanguageDetailAPIView.as_view(),
         name="language-partial-id"),

    path('country', views.CountryListAPIView.as_view(), name="country"),
    path('country/<int:id>', views.CountryDetailAPIView.as_view(),
         name="country-partial-id"),

    path('wallet', views.WalletListAPIView.as_view(), name="wallet"),
    path('wallet/<int:id>', views.WalletDetailAPIView.as_view(),
         name="wallet-partial-id"),
]
