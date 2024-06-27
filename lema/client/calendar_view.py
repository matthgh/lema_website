import calendar
from calendar import HTMLCalendar


class CustomHTMLCalendar(HTMLCalendar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day_abbr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def formatday(self, day, weekday):
        if day == 0:
            return "<button><time>&nbsp;</time></button>"
        else:
            return f"<button><time>{day}</time></button>"

    def formatweek(self, theweek):
        s = "".join(self.formatday(d, wd) for (d, wd) in theweek)
        return f"{s}"

    def formatweekheader(self):
        s = "".join(f"<span>{day}</span>" for day in self.day_abbr)
        return f"{s}"

    def formatmonthname(self, theyear, themonth, withyear=True):
        month_name = calendar.month_name[themonth]
        if withyear:
            return f'<div>{month_name} <span class="year">{theyear}</span></div>'
        else:
            return f"<div>{month_name}</div>"

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<div class="month">')
        a("\n")
        a("<a href='' class='nav'><i class='fas fa-angle-left'></i></a>")
        a("\n")
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a("\n")
        a("<a href='' class='nav'><i class='fas fa-angle-right'></i></a>")
        a("\n")
        a("</div>")
        a("\n")
        a("<div class='days'>")
        a("\n")
        a(self.formatweekheader())
        a("\n")
        a("</div>")
        a("\n")
        a("<div class='dates'>")
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a("\n")
        a("</div>")
        a("\n")
        return "".join(v)
