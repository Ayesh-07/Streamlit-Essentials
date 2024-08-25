
# ### 1. **Two-Column Weather Dashboard**
#    - Create a weather dashboard with two columns:
#      - **Left Column**: User input (e.g., location, date).
#      - **Right Column**: Show the weather forecast (temperature, humidity, etc.).
#    - Add an expander for extra weather details (e.g., wind speed, sunrise time).

import streamlit as st
st.set_page_config(layout="wide")
st.title("Weather Dashboard")

sample = {
    "New York": {"temp": 20, "humidity": 65, "wind_speed": 10, "sunrise": "6:00 AM"},
    "London": {"temp": 15, "humidity": 75, "wind_speed": 15, "sunrise": "5:30 AM"},
    "Tokyo": {"temp": 22, "humidity": 60, "wind_speed": 8, "sunrise": "4:45 AM"},
}

column1 ,  column2 = st.columns(2)


with column1:
    st.header("Weather")
    location = st.selectbox("Select Location", list(sample.keys()))

    date = st.date_input("Select Date")

    st.write(f"Location: {location}")
    st.write(f"Date: {date}")

with column2:
    st.subheader(f"Weather Forecast for {location}")

    # Fetching weather details for the selected location
    weather_info = sample[location]
    temp = weather_info["temp"]
    humidity = weather_info["humidity"]

# Displaying the main weather details
    st.metric(label="Temperature (°C)", value=f"{temp}")
    st.metric(label="Humidity (%)", value=f"{humidity}")

    # Expander for additional weather information
    with st.expander("More Weather Details"):
        wind_speed = weather_info["wind_speed"]
        sunrise = weather_info["sunrise"]

        st.write(f"Wind Speed: {wind_speed} km/h")
        st.write(f"Sunrise: {sunrise}")


# -------------------------------------------------------------------------------------------------------------



