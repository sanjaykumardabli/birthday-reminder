from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from wishes_menu.helper import get_broadcast_data

def send_email(context = {}, recepients='', subject='', from_email='', html_content='', text_content=''):
    try:
        if not (context):
            raise ValueError("birthday_data or from_email is required")

        if not recepients:
            recepients = get_broadcast_emails()
        
        if not subject:
            subject = get_email_subject()
        
        if not html_content:
            html_content = get_html_content()
        
        if not text_content:
            text_content = get_text_content()
        
        if not from_email:
            from_email = settings.EMAIL_HOST_USER

        if context.get('events', None):

            connection = get_connection(host=settings.EMAIL_HOST,  
                                        port=settings.EMAIL_PORT,  
                                        username=settings.EMAIL_HOST_USER,  
                                        password=settings.EMAIL_HOST_PASSWORD,  
                                        use_tls=settings.EMAIL_USE_TLS 
                                        )

            html_content = render_to_string('birthday/day_before_birthday.html', context)
            text_content = strip_tags(html_content)
            email =  EmailMultiAlternatives(subject, text_content, from_email, recepients)
            email.attach_alternative(html_content, "text/html")
            email.send()
            connection.close()
    
    except Exception as e:
        print('ERROR:', e)

    # msg = EmailMultiAlternatives(subject, text_content, from_email, recepients)
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()

def get_text_content():
    text_content = 'This is an important message.'
    return text_content

def get_email_subject():
    subject = 'Birthday Remainder'
    return subject
    
def get_broadcast_emails():
    to = get_broadcast_data('email')
    return to or []

def get_html_content():
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    return html_content