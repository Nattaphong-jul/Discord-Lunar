import calendar
from datetime import datetime

def month_calendar(year=None, month=None):
    # If year or month is not provided, use the current date
    now = datetime.now()
    print(month)
    if not month and not year:
            date = f"{now.day} "
    else:
        date = ""
    year = year or now.year
    month = month or now.month

    # Get the month's name
    month_name = calendar.month_name[month]

    # Create a calendar for the month
    cal = calendar.monthcalendar(year, month)
    # Build a list of formatted weeks
    week_str = []
    for week in cal:
        # Replace zeros (days outside the month) with blank spaces
        week_str.append("  ".join(f"{day:02}" if day != 0 else "  " for day in week))

    # Prepare the header and the formatted weeks as a single string
    header = f"{date}{month_name} {year}"
    week_str = "Mo  Tu  We  Th  Fr  Sa  Su\n" + '\n'.join(week_str)

    return header, week_str

# Example usage
# header, calendar_text = month_calendar(1)
# print(header + '\n' + calendar_text)
