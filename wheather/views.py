from django.shortcuts import render
from celery_app import debug_task
from .forms import CityCheck
from .tasks import get_weather_task


# Create your views here.


def debug(request):
    ref = debug_task.delay()
    return render(request, 'index.html', {'ref': ref})


def check_weather(request):
    if request.method == 'POST':
        form = CityCheck(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']
            email = form.cleaned_data['email']
            get_weather_task.delay(city, email)
            return render(request, 'weather_form.html', {'form': form})
    else:
        form = CityCheck()
    return render(request, 'weather_form.html', {'form': form})
