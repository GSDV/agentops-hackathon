from datetime import date, timedelta

now = date.today()

def format_time(date):
    return date.strftime('%B %d, %Y')

def time_now():
    return format_time(now)