# main.py
import api
import weather_info

def main():
    data = api.get_weather_data()       #Fetch weather data from the API

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            forecast_data = api.get_data_by_date(data, date)            #Get forecast data for the specified date
            temperature = weather_info.get_temperature(forecast_data)   #Extract temperature and print it
            print(f"Temperature: {temperature}°C")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            forecast_data = api.get_data_by_date(data, date)            #
            wind_speed = weather_info.get_wind_speed(forecast_data)
            print(f"Wind Speed: {wind_speed} m/s")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            forecast_data = api.get_data_by_date(data, date)
            pressure = weather_info.get_pressure(forecast_data)
            print(f"Pressure: {pressure} hPa")

        elif choice == '0':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
