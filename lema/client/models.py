from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.conf import settings as s


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    phone_number = PhoneNumberField(region="IT")
    notes = models.TextField(max_length=400, default="")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Eight(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    class Meta:
        verbose_name = "otto"

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfEight(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Nine(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfNine(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Ten(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfTen(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Eleven(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfEleven(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Two(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfTwo(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Three(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfThree(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Four(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfFour(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class Five(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")


class HalfFive(models.Model):
    user_info = models.ManyToManyField(UserInfo)
    date = models.DateField()

    def clean(self):
        super().clean()
        if self.user_info.count() > s.MAX_USERS:
            raise ValidationError("You cannot assign more than 4 users.")
