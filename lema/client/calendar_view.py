from django.template import loader

from calendar import HTMLCalendar
from datetime import date
from decouple import config


class Custom2HTMLCalendar(HTMLCalendar):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.current_month = None
        self.day_abbr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def formatday(self, day: int, weekday: int) -> str:
        context = {"day": day}
        if day == 0:
            return """
            <td class="pt-6">
                <div
                  class="px-2 py-2 cursor-pointer flex w-full justify-center"
                ></div>
            </td>
            """

        else:
            if date.today().day == day and date.today().month == self.current_month:
                context["current_day"] = day
                return loader.get_template(
                    "template_loader/current-day-render.html"
                ).render(context)
            elif (
                day < date.today().day
                and self.current_month < date.today().month
                or self.current_month < date.today().month
                or day < date.today().day
                and self.current_month == date.today().month
            ):
                context["disabled"] = True
                return loader.get_template("template_loader/day-render.html").render(
                    context
                )

            return loader.get_template("template_loader/day-render.html").render(
                context
            )

    def formatweek(self, theweek):
        s = "".join(self.formatday(d, wd) for (d, wd) in theweek)
        return f"<tr>{s}</tr>"

    def formatweekheader(self):
        s = "".join(
            f"""
            <th>
                <div class="w-full flex justify-center">
                  <p
                    class="text-base font-medium text-center text-gray-800"
                  >
                    {day}
                  </p>
                </div>
            </th>
            """
            for day in self.day_abbr
        )
        return f"<tr>{s}</tr>"

    def formatmonth(self, theyear, themonth, withyear=True):
        self.current_month = themonth

        context = {
            "months_years": self.formatmonthname(theyear, themonth, withyear),
            "weekheader": self.formatweekheader(),
            "dates": "".join(
                self.formatweek(week)
                for week in self.monthdays2calendar(theyear, themonth)
            ),
            "left_arrow_url": config("ARROW_LEFT_URL"),
            "right_arrow_url": config("ARROW_RIGHT_URL"),
        }

        return loader.get_template("template_loader/calendar_render.html").render(
            context
        )
