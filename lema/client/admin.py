from django.contrib import admin
from .forms import EightForm

# Register your models here.
from .models import (
    UserInfo,
    Eight,
    HalfEight,
    Nine,
    HalfNine,
    Ten,
    HalfTen,
    Eleven,
    HalfEleven,
    Two,
    HalfTwo,
    Three,
    HalfThree,
    Four,
    HalfFour,
    Five,
    HalfFive,
)

r = [
    HalfEight,
    Nine,
    HalfNine,
    Ten,
    HalfTen,
    Eleven,
    HalfEleven,
    Two,
    HalfTwo,
    Three,
    HalfThree,
    Four,
    HalfFour,
    Five,
    HalfFive,
]

for model in r:
    admin.site.register(model)


admin.site.register(UserInfo)


class EightAdmin(admin.ModelAdmin):
    form = EightForm


admin.site.register(Eight, EightAdmin)
