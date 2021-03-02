from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django_countries.fields import CountryField
from django_countries.serializers import CountryFieldMixin


class RegisterSerializer(CountryFieldMixin, serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    job = serializers.CharField(max_length=255)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['id',
                  'language',
                  'user_type',
                  'username',
                  'country',
                  'country_code',
                  'phone',
                  'email',
                  'job',
                  'skills',
                  'profile_image',
                  'background_image',
                  'about_me',
                  'work_title',
                  'work_description',
                  'work_url',
                  'work_date',
                  'work_skills',
                  'upload_work_files',
                  'password',
                  'confirm_password']

    def validate(self, attrs):

        username = attrs.get('username', '')
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')
        work_title = attrs.get('work_title', '')
        work_description = attrs.get('work_description', '')
        work_url = attrs.get('work_url', '')
        work_date = attrs.get('work_date', '')
        work_skills = attrs.get('work_skills', '')
        upload_work_files = attrs.get('upload_work_files', '')

        if (work_url or work_date or upload_work_files) and not \
                (work_title and work_description and work_skills):
            raise serializers.ValidationError(
                "Please fill all required work fields\
                     ( title, description, skills ).")

        if password and not confirm_password:
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if password != confirm_password:
            raise serializers.ValidationError("Those passwords don't match.")

        if not username.isalpha():
            raise serializers.ValidationError(
                self.default_error_messages)

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'user_type', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user_type = attrs.get('user_type', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(
            email=email, password=password, user_type=user_type)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'id': user.id,
            'email': user.email,
            'user_type': user.user_type,
            'tokens': user.tokens
        }

        return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    confirm_password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'confirm_password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            if password and not confirm_password:
                raise serializers.ValidationError("Please enter a password and "
                                                  "confirm it.")
            if password != confirm_password:
                raise serializers.ValidationError(
                    "Those passwords don't match.")

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
