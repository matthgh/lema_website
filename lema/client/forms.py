from django import forms
from .models import (
    Eight,
    Eleven,
    Five,
    Four,
    HalfEight,
    HalfEleven,
    HalfFive,
    HalfFour,
    HalfNine,
    HalfTen,
    HalfThree,
    HalfTwo,
    Nine,
    Ten,
    Three,
    Two,
    UserInfo,
)
from django.conf import settings
from django.core.exceptions import ValidationError


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["phone_number"].required = False

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]

        if first_name == "" or first_name.isdigit():
            raise ValidationError("Inserici un nome valido!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]

        if last_name == "" or last_name.isdigit():
            raise ValidationError("Inserici un cognome valido!")
        return last_name


class EightForm(forms.ModelForm):

    class Meta:
        model = Eight
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Eight.objects.filter(date=date).count()
        print(users)

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfEightForm(forms.ModelForm):

    class Meta:
        model = HalfEight
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfEight.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class NineForm(forms.ModelForm):

    class Meta:
        model = Nine
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Nine.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfNineForm(forms.ModelForm):

    class Meta:
        model = HalfNine
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfNine.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class TenForm(forms.ModelForm):

    class Meta:
        model = Ten
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Ten.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfTenForm(forms.ModelForm):

    class Meta:
        model = HalfTen
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfTen.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class ElevenForm(forms.ModelForm):

    class Meta:
        model = Eleven
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Eleven.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfElevenForm(forms.ModelForm):

    class Meta:
        model = HalfEleven
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfEleven.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class TwoForm(forms.ModelForm):

    class Meta:
        model = Two
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Two.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfTwoForm(forms.ModelForm):

    class Meta:
        model = HalfTwo
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfTwo.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class ThreeForm(forms.ModelForm):

    class Meta:
        model = Three
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Three.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfThreeForm(forms.ModelForm):

    class Meta:
        model = HalfThree
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfThree.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class FourForm(forms.ModelForm):

    class Meta:
        model = Four
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Four.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfFourForm(forms.ModelForm):

    class Meta:
        model = HalfFour()
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfFour.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class FiveForm(forms.ModelForm):

    class Meta:
        model = Five
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = Five.objects.filter(date=date).count()

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")


class HalfFiveForm(forms.ModelForm):

    class Meta:
        model = HalfFive
        fields = [
            "user_info",
            "date",
        ]

    def clean(self):
        super().clean()
        date = self.cleaned_data.get("date")

        users = HalfFive.objects.filter(date=date).count()
        print(users)

        if users > settings.MAX_USERS:
            raise ValidationError("Maximum number of users exceeded.")
