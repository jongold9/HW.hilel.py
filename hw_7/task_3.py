import requests
from datetime import datetime

def get_weather_forecast(city, days=5):
    api_key = "f9ada9efec6a3934dad5f30068fdcbb8"
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    return data

def write_forecast_to_file(city, days, forecast):
    current_date = datetime.now().strftime("%d-%m-%Y")
    filename = f"{current_date}-{city}-{days}-days-weather-forecast.txt"
    
    with open(filename, 'w') as file:
        file.write("Дата Температура вдень Температура вночі\n")
        for day in forecast['list']:
            date = datetime.fromtimestamp(day['dt']).strftime("%d-%m-%Y")
            day_temp = day['temp']['day']
            night_temp = day['temp']['night']
            file.write(f"{date} {day_temp} {night_temp}\n")

def main():
    city = input("Введіть назву міста: ")
    days = int(input("Введіть кількість днів для прогнозу: "))
    
    weather_forecast = get_weather_forecast(city, days)
    write_forecast_to_file(city, days, weather_forecast)
    
    print(f"Прогноз погоди для {city} на наступні {days} днів записано у файл.")

if __name__ == "__main__":
    main()
