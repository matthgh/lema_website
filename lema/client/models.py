from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings as s
import uuid


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    phone_number = PhoneNumberField()
    notes = models.TextField(max_length=400, default="", blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Eight(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "8:00 - 8:30"

    @property
    def model_id(self):
        return 1


class HalfEight(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "8:30 - 9:00"

    @property
    def model_id(self):
        return 2


class Nine(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "9:00 - 9:30"

    @property
    def model_id(self):
        return 3


class HalfNine(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "9:30 - 10:00"

    @property
    def model_id(self):
        return 4


class Ten(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "10:00 - 10:30"

    @property
    def model_id(self):
        return 5


class HalfTen(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "10:30 - 11:00"

    @property
    def model_id(self):
        return 6


class Eleven(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "11:00 - 11:30"

    @property
    def model_id(self):
        return 7


class HalfEleven(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "11:30 - 12:00"

    @property
    def model_id(self):
        return 8


class Two(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "14:00 - 14:30"

    @property
    def model_id(self):
        return 9


class HalfTwo(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "14:30 - 15:00"

    @property
    def model_id(self):
        return 10


class Three(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "15:00 - 15:30"

    @property
    def model_id(self):
        return 11


class HalfThree(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "15:30 - 16:00"

    @property
    def model_id(self):
        return 12


class Four(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "16:00 - 16:30"

    @property
    def model_id(self):
        return 13


class HalfFour(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "16:30 - 17:00"

    @property
    def model_id(self):
        return 14


class Five(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "17:00 - 17:30"

    @property
    def model_id(self):
        return 15


class HalfFive(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def time(self):
        return "17:30 - 18:00"

    @property
    def model_id(self):
        return 16
