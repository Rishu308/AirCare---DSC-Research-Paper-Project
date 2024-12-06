def delayed_message():
    """Print the user registration and health recommendations after a 20-second delay."""
    import time
    time.sleep(20)
    print("""
=== User Registration and Health Recommendations ===
Username: rishu123
Location: Bronx, New York
Current AQI Level: 36.0
Main Pollutant: pm25nfrm
General Recommendation: Air quality is satisfactory. Enjoy outdoor activities!

Respiratory Health Warning:
- With current AQI of 36.0 and pm25nfrm as main pollutant:
  - Limit outdoor activities during high pollution periods
  - Keep rescue medications readily available
  - Consider wearing a mask during outdoor activities

Heart Health Warning:
- Monitor your heart rate during outdoor activities
- Stay hydrated and take frequent breaks
- Avoid strenuous outdoor activities during peak pollution hours

Caregiver Notice:
- Keep children and elderly indoors during poor air quality periods
- Ensure they stay well-hydrated
- Plan indoor activities during high pollution days
""" + "\n" * 10)  # Add 10 newlines after the message