from datetime import date, timedelta

now = date.today()

def format_time(date):
    return date.strftime('%B %d, %Y')

def time_now():
    return format_time(now)

def time_one_week_ago():
    seven_days_ago = now - timedelta(days=7)
    return format_time(seven_days_ago)
