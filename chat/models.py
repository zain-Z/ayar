from django.db import models
from authentication.models import User
from .validators import validate_file_extension, validate_image_extension


class Offer(models.Model):
    price = models.FloatField(max_length=10, default="")
    description = models.TextField()
    date = models.DateField(editable=True, default="")


class Messages(models.Model):
    upload_files = models.FileField(
        blank=True, null=True, validators=[validate_file_extension, validate_image_extension],
        upload_to='uploaded_files/')
    description = models.TextField()
    offer = models.OneToOneField(
        Offer, related_name='offer', on_delete=models.CASCADE, default="")
    sender_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name} From: {self.sender_name}"

    class Meta:
        ordering = ('timestamp',)


class Friends(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.IntegerField()

    def __str__(self):
        return f"{self.friend}"
