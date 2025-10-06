import random
import statistics
from datetime import datetime, timedelta

class WeatherDay:
    def __init__(self, date, temp, humidity, wind):
        self.date = date
        self.temp = temp
        self.humidity = humidity
        self.wind = wind

    def __repr__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | Temp: {self.temp:.1f}°C | Humidity: {self.humidity}% | Wind: {self.wind} km/h"

def generate_weather(days=10):
    data = []
    start_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = start_date + timedelta(days=i)
        temp = random.uniform(-5, 25)
        humidity = random.randint(30, 90)
        wind = random.randint(0, 40)
        data.append(WeatherDay(date, temp, humidity, wind))
    return data

def analyze_weather(data):
    temps = [d.temp for d in data]
    hums = [d.humidity for d in data]
    avg_temp = statistics.mean(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    avg_humidity = statistics.mean(hums)
    return {
        "average_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "average_humidity": avg_humidity
    }

def print_report(data, stats):
    print("=== WEATHER REPORT ===")
    for d in data:
        print(d)
    print("\n=== STATISTICS ===")
    for k, v in stats.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}")

if __name__ == "__main__":
    dataset = generate_weather(15)
    stats = analyze_weather(dataset)
    print_report(dataset, stats)



                                                  
