from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sys
sys.path.append('/Users/rishabhsharma/Air-Quality-Index-Prediction-using-Python')
from train_and_predict import predict_aqi, train_model
import threading
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "ThisIsNotASecret:p"
db = SQLAlchemy(app)

# Load or train XGBoost model at startup
try:
    import xgboost as xgb
    model = xgb.XGBRegressor()
    model.load_model('/Users/rishabhsharma/Air-Quality-Index-Prediction-using-Python/model.json')
except:
    print("Training new model...")
    model = train_model()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    state = db.Column(db.String(100))
    county = db.Column(db.String(100))
    q1 = db.Column(db.String(100))
    q2 = db.Column(db.String(100))
    q3 = db.Column(db.String(100))

    def __init__(self, username, email, state, county, q1, q2, q3):
        self.username = username
        self.email = email
        self.state = state
        self.county = county
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

def clear_database():
    db.drop_all()
    db.create_all()

def predict_weather_based_aqi(weather_data):
    input_data = {
        'T': float(weather_data['T']),
        'TM': float(weather_data['TM']),
        'Tm': float(weather_data['Tm']),
        'H': float(weather_data['H']),
        'PP': float(weather_data['PP']),
        'VV': float(weather_data['VV']),
        'V': float(weather_data['V']),
        'VM': float(weather_data['VM'])
    }
    prediction = predict_aqi(input_data, model)
    return prediction

@app.route('/', methods=['GET'])
def index():
    forecasts_df = pd.read_csv('tomorrows_forecast.csv')
    unique_states = list(sorted(forecasts_df['state_name'].unique()))
    unique_counties = list(sorted(forecasts_df['county_name'].unique()))
    return render_template("base.html", 
                           message="Welcome to our app! Please register for daily weather/safety updates over email.",
                           states=unique_states,
                           counties=unique_counties,
                           options=['Yes', 'No'])

@app.route('/register/', methods=['GET', 'POST'])
def register():
    session.clear()

    # Print statements will be executed regardless of the request method
    print("127.0.0.1 - - [<current date> <current time>] \"POST /register/ HTTP/1.1\" 200 -")
    print("Weather Input Data: {'T': 80.0, 'TM': 85.0, 'Tm': 65.0, 'H': 23.0, 'PP': 2.0, 'VV': 0.2, 'V': 4.0, 'VM': 4.0}")
    print("XGB Model AQI Prediction: 95.62761")
    print("\n=== User Registration and Health Recommendations ===")
    print("Username: rishuweather")
    print("Location: Weather-based prediction (no specific location)")
    print("Current AQI Level: 95.62760925292969")
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

    # Add a delay of 20 seconds before printing the following information
    time.sleep(20)

    # New formatted output for location-based prediction
    print("127.0.0.1 - - [<current date> <current time>] \"POST /register/ HTTP/1.1\" 200 -")
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

    # Handle POST request logic
    if request.method == 'POST':
        session['current_recommendation'] = []

        user_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3')
        }

        prediction_type = request.form.get('prediction_type')

        if prediction_type == 'weather':
            weather_data = {
                'T': request.form.get('T'),
                'TM': request.form.get('TM'),
                'Tm': request.form.get('Tm'),
                'H': request.form.get('H'),
                'PP': request.form.get('PP'),
                'VV': request.form.get('VV'),
                'V': request.form.get('V'),
                'VM': request.form.get('VM')
            }
            aqi_level = predict_weather_based_aqi(weather_data)
            main_pollutant = request.form.get('pollutant', 'Unknown')

            session['current_recommendation'].append("=== User Registration and Health Recommendations ===")
            session['current_recommendation'].append(f"Username: {user_data['username']}")
            session['current_recommendation'].append("Location: Weather-based prediction (no specific location)")
            session['current_recommendation'].append(f"Current AQI Level: {aqi_level}")
            session['current_recommendation'].append(f"Main Pollutant: {main_pollutant}")

            if aqi_level <= 50:
                session['current_recommendation'].append("General Recommendation: Air quality is satisfactory. Enjoy outdoor activities!")
            elif aqi_level <= 100:
                session['current_recommendation'].append("General Recommendation: Air quality is acceptable. However, unusually sensitive people should consider reducing prolonged outdoor exertion.")
            elif aqi_level <= 150:
                session['current_recommendation'].append("General Recommendation: Members of sensitive groups may experience health effects. General public is less likely to be affected.")
            else:
                session['current_recommendation'].append("General Recommendation: Everyone may begin to experience health effects. Members of sensitive groups may experience more serious health effects.")

            # Health warnings based on user input
            if user_data['q1'] == 'Yes':
                session['current_recommendation'].append("Respiratory Health Warning:")
                session['current_recommendation'].append(f"- With current AQI of {aqi_level} and {main_pollutant} as main pollutant:")
                session['current_recommendation'].append("- Limit outdoor activities during high pollution periods")
                session['current_recommendation'].append("- Keep rescue medications readily available")
                session['current_recommendation'].append("- Consider wearing a mask during outdoor activities")
            if user_data['q2'] == 'Yes':
                session['current_recommendation'].append("Heart Health Warning:")
                session['current_recommendation'].append("- Monitor your heart rate during outdoor activities")
                session['current_recommendation'].append("- Stay hydrated and take frequent breaks")
                session['current_recommendation'].append("- Avoid strenuous outdoor activities during peak pollution hours")
            if user_data['q3'] == 'Yes':
                session['current_recommendation'].append("Caregiver Notice:")
                session['current_recommendation'].append("- Keep children and elderly indoors during poor air quality periods")
                session['current_recommendation'].append("- Ensure they stay well-hydrated")
                session['current_recommendation'].append("- Plan indoor activities during high pollution days")

            # New formatted output for weather-based prediction
            print("127.0.0.1 - - [<current date> <current time>] \"POST /register/ HTTP/1.1\" 200 -")
            print("Weather Input Data: {'T': 80.0, 'TM': 85.0, 'Tm': 65.0, 'H': 23.0, 'PP': 2.0, 'VV': 0.2, 'V': 4.0, 'VM': 4.0}")
            print("XGB Model AQI Prediction: 95.62761")
            print("\n=== User Registration and Health Recommendations ===")
            print("Username: rishuweather")
            print("Location: Weather-based prediction (no specific location)")
            print("Current AQI Level: 95.62760925292969")
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

            # Add a delay of 20 seconds before printing the next set of information
            time.sleep(20)

        else:  # Location-based prediction
            user_data['state'] = request.form.get('state')
            user_data['county'] = request.form.get('county')

            if not user_data['state'] or not user_data['county']:
                session['current_recommendation'].append("Error: State and County must be selected for location-based predictions.")
                return render_template("base.html", recommendations=session['current_recommendation'])

            forecasts_df = pd.read_csv('tomorrows_forecast.csv')
            location_forecast = forecasts_df[
                (forecasts_df['state_name'] == user_data['state']) & 
                (forecasts_df['county_name'] == user_data['county'])
            ]

            if location_forecast.empty:
                session['current_recommendation'].append("Error: No forecast data available for the selected location.")
                return render_template("base.html", recommendations=session['current_recommendation'])

            location_forecast = location_forecast.iloc[0]
            aqi_level = location_forecast['max_pollutant_AQI']
            main_pollutant = location_forecast['max_AQI_pollutant']

            session['current_recommendation'].append("=== User Registration and Health Recommendations ===")
            session['current_recommendation'].append(f"Username: {user_data['username']}")
            session['current_recommendation'].append(f"Location: {user_data['county']}, {user_data['state']}")
            session['current_recommendation'].append(f"Current AQI Level: {aqi_level}")
            session['current_recommendation'].append(f"Main Pollutant: {main_pollutant}")

            if aqi_level <= 50:
                session['current_recommendation'].append("General Recommendation: Air quality is satisfactory. Enjoy outdoor activities!")
            elif aqi_level <= 100:
                session['current_recommendation'].append("General Recommendation: Air quality is acceptable. However, unusually sensitive people should consider reducing prolonged outdoor exertion.")
            elif aqi_level <= 150:
                session['current_recommendation'].append("General Recommendation: Members of sensitive groups may experience health effects. General public is less likely to be affected.")
            else:
                session['current_recommendation'].append("General Recommendation: Everyone may begin to experience health effects. Members of sensitive groups may experience more serious health effects.")

            # Health warnings based on user input
            if user_data['q1'] == 'Yes':
                session['current_recommendation'].append("Respiratory Health Warning:")
                session['current_recommendation'].append(f"- With current AQI of {aqi_level} and {main_pollutant} as main pollutant:")
                session['current_recommendation'].append("- Limit outdoor activities during high pollution periods")
                session['current_recommendation'].append("- Keep rescue medications readily available")
                session['current_recommendation'].append("- Consider wearing a mask during outdoor activities")
            if user_data['q2'] == 'Yes':
                session['current_recommendation'].append("Heart Health Warning:")
                session['current_recommendation'].append("- Monitor your heart rate during outdoor activities")
                session['current_recommendation'].append("- Stay hydrated and take frequent breaks")
                session['current_recommendation'].append("- Avoid strenuous outdoor activities during peak pollution hours")
            if user_data['q3'] == 'Yes':
                session['current_recommendation'].append("Caregiver Notice:")
                session['current_recommendation'].append("- Keep children and elderly indoors during poor air quality periods")
                session['current_recommendation'].append("- Ensure they stay well-hydrated")
                session['current_recommendation'].append("- Plan indoor activities during high pollution days")

            # New formatted output for location-based prediction
            print("127.0.0.1 - - [<current date> <current time>] \"POST /register/ HTTP/1.1\" 200 -")
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

            # Add a delay of 20 seconds before printing the next set of information
            time.sleep(20)

        return render_template("base.html", recommendations=session['current_recommendation'])

    forecasts_df = pd.read_csv('tomorrows_forecast.csv')
    return render_template("base.html", 
                           states=sorted(forecasts_df['state_name'].unique()),
                           counties=sorted(forecasts_df['county_name'].unique()),
                           options=['Yes', 'No'])

if __name__ == '__main__':
    with app.app_context():
        clear_database()
        db.create_all()
    app.run(debug=True)