import streamlit as st
import datetime
import requests

'''
# My particular driver
'''

chosen_date = st.date_input("Pickup date", datetime.date.today())
chosen_time = st.time_input('Set an alarm for', datetime.datetime.now())
st.write('Time and date to pick up', chosen_date, chosen_time)

lat_pick = st.number_input('Insert a pick up latitude', value=40.776676)
long_pick = st.number_input('Insert a pick up longitude', value=-73.971321)
st.write('The current lat and long is ', lat_pick, long_pick)

lat_drop = st.number_input('Insert a drop off latitude', value=40.776680)
long_drop = st.number_input('Insert a drop off longitude', value=-73.971310)
st.write('The drop off lat and long is ', lat_drop, long_drop)

passegenrs = st.slider('Select a number of passengers', 1, 4, 1)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

travel_params = {
    'pickup_datetime':datetime.datetime.combine(chosen_date, chosen_time),
    'pickup_longitude':lat_pick,
    'pickup_latitude':long_pick,
    'dropoff_longitude':long_drop,
    'dropoff_latitude':lat_drop,
    'passenger_count':passegenrs}

response = requests.get(url=url, params=travel_params).json()

if st.button('click to calculate your trip'):
    # print is visible in the server output, not in the page
    st.write('The trip costs $', round(response['fare'], 2))
