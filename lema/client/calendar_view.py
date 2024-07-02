import calendar
from calendar import HTMLCalendar
from datetime import date

from django.template import loader


class CustomHTMLCalendar(HTMLCalendar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day_abbr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.current_month = None

    def formatday(self, day, weekday):
        context = {"day": day}
        if day == 0:
            return "<span></span>"
        else:
            if date.today().day == day and date.today().month == self.current_month:
                return f"<button class='today'><time>{day}</time></button>"
            return loader.get_template("template_loader/day_render.html").render(
                context
            )

    def formatweek(self, theweek):
        s = "".join(self.formatday(d, wd) for (d, wd) in theweek)
        return f"{s}"

    def formatweekheader(self):
        s = "".join(f"<span>{day}</span>" for day in self.day_abbr)
        return f"{s}"

    def formatmonthname(self, theyear, themonth, withyear=True):
        month_name = calendar.month_name[themonth]
        if withyear:
            return f'<div>{month_name}<span class="year">{theyear}</span></div>'
        else:
            return f"<div>{month_name}</div>"

    def formatmonth(self, theyear, themonth, withyear=True):
        self.current_month = themonth

        context = {
            "months_years": self.formatmonthname(theyear, themonth, withyear=withyear),
            "weekheader": self.formatweekheader(),
            "dates": "".join(
                self.formatweek(week)
                for week in self.monthdays2calendar(theyear, themonth)
            ),
        }

        return loader.get_template("template_loader/calendar_render.html").render(
            context
        )
