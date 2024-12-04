from django.shortcuts import render, HttpResponse
import requests
import datetime


def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Addis Ababa'

    api_key = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Define the parameters for the request (e.g., temperature in Celsius)
    PARAMS = {'units': 'metric'}
    
    # Make the API request
    response = requests.get(url, params=PARAMS)
    
    # If the response status is OK, parse the JSON, else return an error message
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    else:
        description = "Error retrieving weather data"
        icon = "unknown"
        temp = "N/A"

    # Get the current date
    day = datetime.date.today()

    # Render the template with the weather data
    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day
    })
