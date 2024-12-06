# AirCare - Respiratory Health Recommendation System

## Overview
The AirCare project aims to provide predictions and visualizations of the Air Quality Index (AQI) across 100 counties in the United States. This system not only forecasts AQI but also delivers personalized health recommendations based on the predicted air quality.

## Motivation
Air quality forecasts are crucial for public health, allowing individuals and authorities to take preventive measures. This project leverages historical data and advanced modeling techniques to provide accurate AQI predictions and actionable insights.

## Models Used
### 1. Vector Autoregression (VAR)
- **Description**: VAR is a multivariate time series forecasting model that captures the linear interdependencies among multiple time series. It is particularly useful for modeling the relationships between different pollutants and their effects on AQI.
- **Implementation**: The model was trained using historical data from the Environmental Protection Agency (EPA) and incorporates geospatial effects by including data from neighboring counties.

### 2. XGBoost (Extreme Gradient Boosting)
- **Description**: XGBoost is a powerful machine learning algorithm that is widely used for regression and classification tasks. It is known for its speed and performance, making it suitable for large datasets.
- **Implementation**: The model was trained on features such as temperature, humidity, and pollutant levels to predict PM2.5 concentrations, which are critical for calculating AQI.

## Data Sources
- **EPA Data**: Historical air quality data was obtained from the EPA.
- **OpenWeatherMap API**: Used to gather climate data over the last 11 years for key atmospheric pollutants.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishu308/AirCare---DSC-Research-Paper-Project.git
   cd AirCare---DSC-Research-Paper-Project
   ```

2. Create a conda environment:
   ```bash
   conda create --name aircare-env --file requirements-conda.txt
   conda activate aircare-env
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Training the Model**: To train the XGBoost model, run the following command:
   ```bash
   python train_and_predict.py
   ```

2. **Running the Web Application**: Start the Flask application:
   ```bash
   python flask-app.py
   ```

3. **Access the Frontend**: Open your browser and navigate to:
   ```
   http://localhost:5000/aqi-frontend
   ```

## Features
- **AQI Prediction**: Input various climate details or select popular cities to get AQI predictions.
- **Health Recommendations**: Based on the predicted AQI, receive personalized health recommendations.
- **Data Visualization**: Interactive visualizations to explore historical trends and forecasts.



