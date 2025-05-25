import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your own OpenWeatherMap API key
API_KEY = 'f35b001f997a00df57e082e3bd624f86'



    
def get_weather():
    global results
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data.get("message", "Cannot retrieve weather information"))
            return
        
        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        results = tk.Tk()
        results.geometry('400x300')
        results.title('Weather report')
        results.resizable(True,True)

        label1 = tk.Label(results,text=city,font=('verdana',20,'bold'),fg='blue')
        label1.pack(pady=10,padx=10)


        result = f"Weather:   {weather}\nTemperature:   {temperature}°C\nHumidity:   {humidity}%\nWind Speed:   {wind_speed} m/s"

        weather_result = tk.Label(results,text=result ,font=("Arial", 15),fg='black', justify="center")
        weather_result.pack(pady=20)


        results.mainloop()
        


    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to connect to weather service: {e}")

# GUI setup

app = tk.Tk()
app.title("Weather App")
app.geometry("500x200")
app.resizable(False, False)

tk.Label(app, text="Enter City:", font=("Arial", 17)).pack(pady=20)

city_entry = tk.Entry(app, font=("Arial", 17))
city_entry.pack(pady=20)

tk.Button(app, text="Get Weather report", font=("Arial", 15), bg='blue',fg='white',command=get_weather).pack(pady=12)

app.mainloop()


