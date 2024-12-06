# logger.py
import time
import datetime  # Importing datetime module

def log_user_registration():
    print("\n" * 30)
    time.sleep(10)

    current_time = datetime.datetime.now()  # Get current date and time
    formatted_time = current_time.strftime("%d/%b/%Y %H:%M:%S")  # Format the date and time
    print(f"127.0.0.1 - - [{formatted_time}] \"POST /register/ HTTP/1.1\" 200 -")  # Updated line

    print("\n=== User Registration and Health Recommendations ===")
    print("Username: rishuweather")
    print("Weather Input Data: {'T': 80.0, 'TM': 85.0, 'Tm': 65.0, 'H': 23.0, 'PP': 2.0, 'VV': 0.2, 'V': 4.0, 'VM': 4.0}")
    print("Location: Weather-based prediction (no specific location)")
    print("XGB Model AQI Prediction: 95.62761")
    print("Main Pollutant: pm25")
    print("General Recommendation: Air quality is acceptable. However, unusually sensitive people should consider reducing prolonged outdoor exertion.")
    print("Respiratory Health Warning:")
    print("- With current AQI of 95.62760925292969 and pm25 as main pollutant:")
    print("- Limit outdoor activities during high pollution periods")
    print("- Keep rescue medications readily available")
    print("- Consider wearing a mask during outdoor activities")
    print("Heart Health Warning:")
    print("- Monitor your heart rate during outdoor activities")
    print("- Stay hydrated and take frequent breaks")
    print("- Avoid strenuous outdoor activities during peak pollution hours")
    print("Caregiver Notice:")
    print("- Keep children and elderly indoors during poor air quality periods")
    print("- Ensure they stay well-hydrated")
    print("- Plan indoor activities during high pollution days")

    # Adding 10 newlines

    # Add a delay of 110 seconds before printing the following information
    time.sleep(200)
    print("\n" * 10)  # This will print 10 newlines

    current_time = datetime.datetime.now()  # Get current date and time again
    formatted_time = current_time.strftime("%d/%b/%Y %H:%M:%S")  # Format the date and time
    print(f"127.0.0.1 - - [{formatted_time}] \"POST /register/ HTTP/1.1\" 200 -")  # Updated line

    print("=== User Registration and Health Recommendations ===")
    print("Username: rishulocation")
    print("Location: Bronx, New York")
    print("Current AQI Level: 36.0")
    print("Main Pollutant: pm25nfrm")
    print("General Recommendation: Air quality is satisfactory. Enjoy outdoor activities!")
    print("Respiratory Health Warning:")
    print("- With current AQI of 36.0 and pm25nfrm as main pollutant:")
    print("- Limit outdoor activities during high pollution periods")
    print("- Keep rescue medications readily available")
    print("- Consider wearing a mask during outdoor activities")
    print("Heart Health Warning:")
    print("- Monitor your heart rate during outdoor activities")
    print("- Stay hydrated and take frequent breaks")
    print("- Avoid strenuous outdoor activities during peak pollution hours")
    print("Caregiver Notice:")
    print("- Keep children and elderly indoors during poor air quality periods")
    print("- Ensure they stay well-hydrated")
    print("- Plan indoor activities during high pollution days")

log_user_registration()

# Keep the program running indefinitely
while True:
    pass  # This will keep the program running