from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    city=request.GET.get('city')
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0ea9ff9985cf8944d39c0f53a85d7181"
    data= requests.get(url).json() 
    payload={'city':data['name'],
             'country':data['sys']['country'],
             "lat":data['coord']['lat'],
             "long":data['coord']['lon'],
             'weather':data['weather'][0]['main'],
             'icon': data['weather'][0]['icon'],
             'kel_temperature':data['main']['temp'],
             'cecius_temperature':int(data['main']['temp']-273),
             'min_kel_temperature':data['main']['temp_min'],
             'min_cel_temperature':int(data['main']['temp_min']-273),
             'max_kel_temperature':data['main']['temp_max'],
             'max_cel_temperature':int(data['main']['temp_max']-273),
             'pressure':data['main']['pressure'],
             'humidity':data['main']['humidity'],
             'description':data['weather'][0]['description'],}
    context={'data':payload}
    print(context)

    return render(request,'index.html',context)