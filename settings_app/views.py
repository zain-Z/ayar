from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from .serializers import PersonalInfoSettingsSerializer, \
    LanguageSettingsSerializer, CountrySettingsSerializer,\
    WalletSettingsSerializer
from .models import PersonalInfo, Language, Country, Wallet
from .permissions import IsOwner
from rest_framework import permissions


class PersonalInfoListAPIView(ListCreateAPIView):
    serializer_class = PersonalInfoSettingsSerializer
    queryset = PersonalInfo.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PersonalInfoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonalInfoSettingsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = PersonalInfo.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class LanguageListAPIView(ListCreateAPIView):
    serializer_class = LanguageSettingsSerializer
    queryset = Language.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class LanguageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WalletSettingsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Wallet.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CountryListAPIView(ListCreateAPIView):
    serializer_class = CountrySettingsSerializer
    queryset = Country.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CountryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySettingsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Country.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class WalletListAPIView(ListCreateAPIView):
    serializer_class = WalletSettingsSerializer
    queryset = Wallet.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class WalletDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WalletSettingsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Wallet.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
