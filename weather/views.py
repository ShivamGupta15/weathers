
import requests

from django.shortcuts import render






def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=3b99c321473331eabadb163495bbb1dd'
    city='Mumbai'
    print(city)

    r = requests.get(url.format(city)).json()
    print(r)



    city_weather = {
        'city': city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
    }
    print(city_weather['temperature'])

    context={
        'city_weather':city_weather
    }

    return render(request,'weather/weather.html', context)


