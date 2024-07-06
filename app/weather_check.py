# weather_check.py


import asyncio
import aiohttp
import os
from dotenv import load_dotenv
import streamlit as st # type: ignore

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
OREM_LAT = 40.2969
OREM_LON = -111.6946
WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={OREM_LAT}&lon={OREM_LON}&appid={API_KEY}&units=imperial"

async def fetch_weather(session):
    async with session.get(WEATHER_API_URL) as response:
        return await response.json()

async def check_for_snow():
    async with aiohttp.ClientSession() as session:
        weather_data = await fetch_weather(session)
        weather_condition = weather_data['weather'][0]['main'].lower()
        return 'snow' in weather_condition

def check_for_snow_sync():
    return asyncio.run(check_for_snow())

@st.cache_data(ttl=86400)
def cached_check_for_snow():
    return check_for_snow_sync()

def run_snow_check():
    if cached_check_for_snow():
        st.snow()
