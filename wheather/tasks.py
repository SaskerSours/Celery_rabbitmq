import os

import requests
from celery import shared_task
from dotenv import load_dotenv

from celery_app import app

# from mailproj.views import send_email_view
load_dotenv()
url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

# querystring = {"q": "London"}

headers = {
    "X-RapidAPI-Key": os.getenv('XRAPIDAPIKEY'),
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


from django.core.mail import send_mail


@shared_task
def get_weather_task(city_name, email_user):
    querystring = {"q": f"{city_name}"}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        send_email_view_task.delay(message=data, email=email_user)
        return data
    else:
        return f"Failed to fetch weather data for {city_name}"


@shared_task
def send_email_view_task(message, email: str):
    subject = 'Greetings from Django'
    messages = str(message)
    from_email = 'horobets.dmitro@gmail.com'
    recipient_list = [email]
    send_mail(subject, messages, from_email, recipient_list, fail_silently=False)
