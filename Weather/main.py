
def weather():
    import os
    import requests

    city = input("Which city are you located:")
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cbeee001d25c252c35770d4527e6a516&units=metric")

    data = r.json()
    print(data)
    ## This is dictionary in python

    # for weather indormation
    #has id , main:eg'Clouds' , description .
    weather_data = data.get("weather")
    weatherdata = weather_data[0]
    description = weatherdata.get("description")
    ## for main datas 
    # includes, temp , feels_like , temp_min , temp_max, pressure , humidity
    main_data = data.get("main")

    temp = main_data.get("temp")
    feels_like = main_data.get("feels_like")
    temp_min = main_data.get("temp_min")
    temp_max = main_data.get("temp_max")
    pressure = main_data.get("pressure")
    humidity = main_data.get("humidity")



    todays_weather = f"It's {temp} degree celcius , { description } , It feels like {feels_like} degrees, recorded maximum temperature of {temp_max} and minimum temperature of {temp_min} , Humidity is {humidity} percentage"

    return todays_weather
