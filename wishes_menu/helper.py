from .models import EmailBroadcast, Birthday
from datetime import datetime

def get_broadcast_data(field='email'):
    to_emails = EmailBroadcast.objects.all().values_list(field, flat=True)
    return to_emails

def get_birthday_data(field='d_o_b', start_date = ''):
    if not start_date:
        start_date = datetime.datetime.now()

    if type(start_date) == str:
        end_date = datetime.strptime(f"{start_date} 23:59:00.00", '%Y-%m-%d %H:%M:%S.%f')
        start_date = datetime.strptime(f"{start_date} 00:00:00.00", '%Y-%m-%d %H:%M:%S.%f')

    if start_date and end_date:
        birthday_data = Birthday.objects.filter(d_o_b__range = [start_date, end_date])
    else:
        birthday_data = Birthday.objects.all().values_list(field, flat=True)
    return birthday_data