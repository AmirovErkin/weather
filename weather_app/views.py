from django.shortcuts import render

# Create your views here.
import requests
import datetime

def home(request):
    return render(request, 'weather_app/home.html')
def ob_havo_malumotlari(request , city):
    data = datetime.datetime.now()
    kun = data.strftime("%A")
    url = f'http://api.openweathermap.org/data/2.5/weather?appid=855dfb12232b2da4c1d128fc2b574263&q={city}'
    get_url = requests.get(url)
    malumot = get_url.json()
    ob_havo = malumot['weather'][0]['description']
    temperatura = round(malumot['main']['temp'] - 273.15, 2)
    # print(f'The weather {kun} in {city} is {ob_havo} and the temperature is {temperatura}°C')
    return render(request, 'weather_app/index.html', {'kun': kun, 'ob_havo': ob_havo, 'temperatura': temperatura, 'city': city})



