from rest_framework import serializers
from .models import PersonalInfo, Language, Country, Wallet


class PersonalInfoSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalInfo
        fields = ['id', 'username', 'phone', 'email', 'job']


class LanguageSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['id', 'language']


class CountrySettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'country']


class WalletSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['id', 'total_balance', 'outstanding', 'available']
