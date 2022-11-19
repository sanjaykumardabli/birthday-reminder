from datetime import datetime

from utils.util import send_email
from wishes_menu.helper import get_broadcast_data, get_birthday_data

def get_birthdays(birthday_date):   
    birthday_data = get_birthday_data('name', birthday_date)
    return birthday_data

def send_birthday_reminder():
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        birthday_data = get_birthdays(date)
        events = []
        for data in birthday_data:
            events.append(
                {
                    "name": data.name,
                    "d_o_b": data.d_o_b,
                }
            )
        
        context = {
            "events": events,
        }
        recepients = get_broadcast_data()
        send_email(context, recepients)
    
    except Exception as e:
        print("ERROR while sending birthday wishes: " + str(e))
