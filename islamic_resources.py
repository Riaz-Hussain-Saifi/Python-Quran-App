import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
import pytz
import math
import time
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
import base64
import random

# Set page configuration
st.set_page_config(
    page_title="Islamic Resources Hub",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with beautiful animations and responsive design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu&family=Scheherazade+New&display=swap');

    * {
        transition: all 0.3s ease;
    }
    
    .main-header {
        font-size: 2.8rem;
        color: #046307;
        text-align: center;
        padding: 1.8rem 0;
        border-bottom: 3px solid #046307;
        margin-bottom: 2rem;
        font-family: 'Amiri', serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.15);
        animation: fadeIn 1.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .section-header {
        color: #046307;
        padding-left: 0.8rem;
        border-left: 5px solid #046307;
        margin: 1.8rem 0 1.2rem 0;
        animation: slideRight 0.8s ease-in-out;
    }
    
    @keyframes slideRight {
        0% { opacity: 0; transform: translateX(-20px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    .card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 1.8rem;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #046307;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeUp 0.8s ease-in-out;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 16px rgba(0,0,0,0.2);
    }
    
    @keyframes fadeUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .arabic-text {
        font-family: 'Scheherazade New', 'Amiri', serif;
        font-size: 1.8rem;
        direction: rtl;
        text-align: right;
        line-height: 2.8rem;
        padding: 1.2rem;
        background-color: #f5f5f5;
        border-radius: 8px;
        margin: 1.2rem 0;
        border-right: 4px solid #046307;
        animation: fadeIn 1s ease-in-out;
    }
    
    .urdu-text {
        font-family: 'Noto Nastaliq Urdu', serif;
        font-size: 1.6rem;
        direction: rtl;
        text-align: right;
        line-height: 2.5rem;
        padding: 1.2rem;
        background-color: #e8f4f8;
        border-radius: 8px;
        margin: 1.2rem 0;
        border-right: 4px solid #17a2b8;
        animation: fadeIn 1s ease-in-out;
    }
    
    .translation-text {
        font-style: italic;
        padding: 0.8rem 1.2rem;
        background-color: #e9ecef;
        border-radius: 8px;
        margin-bottom: 1.2rem;
        animation: fadeIn 1s ease-in-out;
    }
    
    .info-box {
        background-color: #e8f4f8;
        border-left: 5px solid #17a2b8;
        padding: 1.2rem;
        margin: 1.2rem 0;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        animation: fadeIn 1s ease-in-out;
    }
    
    .stApp {
        background-color: #f9f9f9;
    }
    
    div[data-testid="stSidebar"] {
        background-color: #f0f0f0;
        border-right: 1px solid #e0e0e0;
    }
    
    .highlight {
        background-color: #fffacd;
        padding: 0.3rem;
        border-radius: 4px;
    }
    
    .footer {
        text-align: center;
        padding: 1.5rem;
        font-size: 0.9rem;
        color: #555;
        border-top: 2px solid #e0e0e0;
        margin-top: 2.5rem;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    .prayer-time {
        font-size: 1.3rem;
        font-weight: bold;
        color: #046307;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.8; }
        100% { opacity: 1; }
    }
    
    .hero-section {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("https://img4.goodfon.com/wallpaper/nbig/1/91/mechet-islam-chernyi-fon.jpg");
        background-size: cover;
        background-position: center;
        color: white;
        padding: 4.5rem 2.5rem;
        border-radius: 15px;
        margin-bottom: 2.5rem;
        text-align: center;
        animation: scaleUp 1.2s ease-in-out;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    @keyframes scaleUp {
        0% { transform: scale(0.95); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .hero-title {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.6);
        animation: slideDown 1.2s ease-in-out;
    }
    
    @keyframes slideDown {
        0% { opacity: 0; transform: translateY(-30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .hero-subtitle {
        font-size: 1.7rem;
        margin-bottom: 2.5rem;
        font-weight: 300;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
        animation: slideDown 1.5s ease-in-out;
    }
    
    .hero-button {
        background-color: #046307;
        color: white;
        border: none;
        padding: 0.9rem 1.8rem;
        font-size: 1.2rem;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 0.7rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        animation: fadeUp 1.8s ease-in-out;
    }
    
    .hero-button:hover {
        background-color: #034e05;
        transform: translateY(-3px);
        box-shadow: 0 7px 20px rgba(0,0,0,0.3);
    }
    
    /* Progress bar for Durood counter */
    .durood-progress {
        background-color: #e9ecef;
        border-radius: 50px;
        height: 20px;
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .durood-progress-bar {
        background: linear-gradient(90deg, #046307, #08a80c);
        height: 100%;
        border-radius: 50px;
        transition: width 0.5s ease-in-out;
        box-shadow: 0 0 10px rgba(4, 99, 7, 0.5);
    }
    
    .name-card {
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeUp 0.8s ease-in-out;
    }
    
    .name-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    
    .name-number {
        background-color: #046307;
        color: white;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 15px;
        float: left;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2);
    }
    
    .audio-player {
        width: 100%;
        margin-top: 15px;
        border-radius: 50px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .audio-player audio {
        width: 100%;
        border-radius: 8px;
    }
    
    /* Naat-specific styles */
    .naat-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        background: linear-gradient(145deg, #f8f9fa, #ffffff);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        animation: fadeUp 0.8s ease-in-out;
    }
    
    .naat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        border-left: 5px solid #046307;
    }
    
    .naat-title {
        color: #046307;
        font-size: 1.4rem;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .naat-reciter {
        color: #666;
        font-style: italic;
        margin-bottom: 15px;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
        background-color: #f5f5f5;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #046307;
    }
    
    /* Button styling */
    div[data-testid="stButton"] button {
        border-radius: 50px;
        font-weight: 500;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.2rem;
        }
        .arabic-text {
            font-size: 1.6rem;
        }
        .hero-title {
            font-size: 2.8rem;
        }
        .hero-subtitle {
            font-size: 1.4rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Define a loading animation function
def loading_animation():
    with st.spinner("Loading..."):
        time.sleep(0.5)

# Function to get user's location
def get_user_location():
    try:
        response = requests.get('https://ipinfo.io/json', timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Split coordinates string into latitude and longitude
            coords = data.get('loc', '0,0').split(',')
            location = {
                'city': data.get('city', 'Unknown'),
                'country': data.get('country', 'Unknown'),
                'latitude': float(coords[0]),
                'longitude': float(coords[1])
            }
            return location
        else:
            return {
                'city': 'Islamabad',
                'country': 'PK',
                'latitude': 33.6844,
                'longitude': 73.0479
            }
    except Exception as e:
        return {
            'city': 'Islamabad',
            'country': 'PK',
            'latitude': 33.6844,
            'longitude': 73.0479
        }

# Define API endpoints and functions
def get_quran_editions():
    try:
        response = requests.get("http://api.alquran.cloud/v1/edition", timeout=5)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # If API fails, return sample data
            return [
                {"identifier": "quran-uthmani", "language": "ar", "name": "Quran Uthmani", "englishName": "Quran Uthmani", "format": "text"},
                {"identifier": "en.asad", "language": "en", "name": "Muhammad Asad", "englishName": "Muhammad Asad", "format": "text"},
                {"identifier": "ur.jalandhry", "language": "ur", "name": "Jalandhry", "englishName": "Jalandhry (Urdu)", "format": "text"},
                {"identifier": "ur.ahmedali", "language": "ur", "name": "Ahmed Ali", "englishName": "Ahmed Ali (Urdu)", "format": "text"},
                {"identifier": "ar.alafasy", "language": "ar", "name": "Alafasy", "englishName": "Alafasy", "format": "audio"}
            ]
    except Exception as e:
        # Return sample data if API call fails
        return [
            {"identifier": "quran-uthmani", "language": "ar", "name": "Quran Uthmani", "englishName": "Quran Uthmani", "format": "text"},
            {"identifier": "en.asad", "language": "en", "name": "Muhammad Asad", "englishName": "Muhammad Asad", "format": "text"},
            {"identifier": "ur.jalandhry", "language": "ur", "name": "Jalandhry", "englishName": "Jalandhry (Urdu)", "format": "text"},
            {"identifier": "ur.ahmedali", "language": "ur", "name": "Ahmed Ali", "englishName": "Ahmed Ali (Urdu)", "format": "text"},
            {"identifier": "ar.alafasy", "language": "ar", "name": "Alafasy", "englishName": "Alafasy", "format": "audio"}
        ]

def get_quran_surahs():
    try:
        response = requests.get("http://api.alquran.cloud/v1/surah", timeout=5)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # Return sample data for first few surahs
            return [
                {"number": 1, "name": "الفاتحة", "englishName": "Al-Fatiha", "englishNameTranslation": "The Opening", "numberOfAyahs": 7, "revelationType": "Meccan"},
                {"number": 2, "name": "البقرة", "englishName": "Al-Baqara", "englishNameTranslation": "The Cow", "numberOfAyahs": 286, "revelationType": "Medinan"},
                {"number": 3, "name": "آل عمران", "englishName": "Aal-Imran", "englishNameTranslation": "The Family of Imran", "numberOfAyahs": 200, "revelationType": "Medinan"},
                {"number": 4, "name": "النساء", "englishName": "An-Nisa", "englishNameTranslation": "The Women", "numberOfAyahs": 176, "revelationType": "Medinan"},
                {"number": 5, "name": "المائدة", "englishName": "Al-Maida", "englishNameTranslation": "The Table Spread", "numberOfAyahs": 120, "revelationType": "Medinan"}
            ]
    except Exception as e:
        # Return sample data for first few surahs
        return [
            {"number": 1, "name": "الفاتحة", "englishName": "Al-Fatiha", "englishNameTranslation": "The Opening", "numberOfAyahs": 7, "revelationType": "Meccan"},
            {"number": 2, "name": "البقرة", "englishName": "Al-Baqara", "englishNameTranslation": "The Cow", "numberOfAyahs": 286, "revelationType": "Medinan"},
            {"number": 3, "name": "آل عمران", "englishName": "Aal-Imran", "englishNameTranslation": "The Family of Imran", "numberOfAyahs": 200, "revelationType": "Medinan"},
            {"number": 4, "name": "النساء", "englishName": "An-Nisa", "englishNameTranslation": "The Women", "numberOfAyahs": 176, "revelationType": "Medinan"},
            {"number": 5, "name": "المائدة", "englishName": "Al-Maida", "englishNameTranslation": "The Table Spread", "numberOfAyahs": 120, "revelationType": "Medinan"}
        ]

def get_juz(juz_number, edition="quran-uthmani"):
    try:
        url = f"http://api.alquran.cloud/v1/juz/{juz_number}/{edition}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # Return sample juz data 
            return {
                "number": juz_number,
                "ayahs": [
                    {
                        "number": 1,
                        "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                        "numberInSurah": 1,
                        "juz": juz_number,
                        "surah": {
                            "number": 1,
                            "name": "الفاتحة",
                            "englishName": "Al-Fatiha",
                            "englishNameTranslation": "The Opening"
                        }
                    },
                    {
                        "number": 2,
                        "text": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
                        "numberInSurah": 2,
                        "juz": juz_number,
                        "surah": {
                            "number": 1,
                            "name": "الفاتحة",
                            "englishName": "Al-Fatiha",
                            "englishNameTranslation": "The Opening"
                        }
                    }
                ]
            }
    except Exception as e:
        # Return sample juz data
        return {
            "number": juz_number,
            "ayahs": [
                {
                    "number": 1,
                    "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                    "numberInSurah": 1,
                    "juz": juz_number,
                    "surah": {
                        "number": 1,
                        "name": "الفاتحة",
                        "englishName": "Al-Fatiha",
                        "englishNameTranslation": "The Opening"
                    }
                },
                {
                    "number": 2,
                    "text": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
                    "numberInSurah": 2,
                    "juz": juz_number,
                    "surah": {
                        "number": 1,
                        "name": "الفاتحة",
                        "englishName": "Al-Fatiha",
                        "englishNameTranslation": "The Opening"
                    }
                }
            ]
        }

def get_surah(surah_number, edition="en.asad"):
    try:
        url = f"http://api.alquran.cloud/v1/surah/{surah_number}/{edition}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # Return sample data for Al-Fatiha
            if surah_number == 1:
                return {
                    "number": 1,
                    "name": "الفاتحة",
                    "englishName": "Al-Fatiha",
                    "englishNameTranslation": "The Opening",
                    "revelationType": "Meccan",
                    "numberOfAyahs": 7,
                    "ayahs": [
                        {"number": 1, "text": "In the name of Allah, the Entirely Merciful, the Especially Merciful.", "numberInSurah": 1, "juz": 1, "page": 1},
                        {"number": 2, "text": "[All] praise is [due] to Allah, Lord of the worlds -", "numberInSurah": 2, "juz": 1, "page": 1},
                        {"number": 3, "text": "The Entirely Merciful, the Especially Merciful,", "numberInSurah": 3, "juz": 1, "page": 1},
                        {"number": 4, "text": "Sovereign of the Day of Recompense.", "numberInSurah": 4, "juz": 1, "page": 1},
                        {"number": 5, "text": "It is You we worship and You we ask for help.", "numberInSurah": 5, "juz": 1, "page": 1},
                        {"number": 6, "text": "Guide us to the straight path -", "numberInSurah": 6, "juz": 1, "page": 1},
                        {"number": 7, "text": "The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.", "numberInSurah": 7, "juz": 1, "page": 1}
                    ]
                }
            return None
    except Exception as e:
        # Return sample data for Al-Fatiha
        if surah_number == 1:
            return {
                "number": 1,
                "name": "الفاتحة",
                "englishName": "Al-Fatiha",
                "englishNameTranslation": "The Opening",
                "revelationType": "Meccan",
                "numberOfAyahs": 7,
                "ayahs": [
                    {"number": 1, "text": "In the name of Allah, the Entirely Merciful, the Especially Merciful.", "numberInSurah": 1, "juz": 1, "page": 1},
                    {"number": 2, "text": "[All] praise is [due] to Allah, Lord of the worlds -", "numberInSurah": 2, "juz": 1, "page": 1},
                    {"number": 3, "text": "The Entirely Merciful, the Especially Merciful,", "numberInSurah": 3, "juz": 1, "page": 1},
                    {"number": 4, "text": "Sovereign of the Day of Recompense.", "numberInSurah": 4, "juz": 1, "page": 1},
                    {"number": 5, "text": "It is You we worship and You we ask for help.", "numberInSurah": 5, "juz": 1, "page": 1},
                    {"number": 6, "text": "Guide us to the straight path -", "numberInSurah": 6, "juz": 1, "page": 1},
                    {"number": 7, "text": "The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.", "numberInSurah": 7, "juz": 1, "page": 1}
                ]
            }
        return None

def get_ayah(ayah_number, edition="en.asad"):
    try:
        url = f"http://api.alquran.cloud/v1/ayah/{ayah_number}/{edition}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # Fallback to sample data
            if edition == "quran-uthmani":
                return {
                    "number": ayah_number,
                    "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                    "numberInSurah": 1,
                    "juz": 1,
                    "surah": {
                        "number": 1,
                        "name": "الفاتحة",
                        "englishName": "Al-Fatiha",
                        "englishNameTranslation": "The Opening"
                    }
                }
            elif edition == "en.asad":
                return {
                    "number": ayah_number,
                    "text": "In the name of Allah, the Most Gracious, the Most Merciful",
                    "numberInSurah": 1,
                    "juz": 1,
                    "surah": {
                        "number": 1,
                        "name": "الفاتحة",
                        "englishName": "Al-Fatiha",
                        "englishNameTranslation": "The Opening"
                    }
                }
            elif edition == "ur.jalandhry":
                return {
                    "number": ayah_number,
                    "text": "اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے",
                    "numberInSurah": 1,
                    "juz": 1,
                    "surah": {
                        "number": 1,
                        "name": "الفاتحة",
                        "englishName": "Al-Fatiha",
                        "englishNameTranslation": "The Opening"
                    }
                }
            return None
    except Exception as e:
        # Return sample data as fallback
        return {
            "number": ayah_number,
            "text": "In the name of Allah, the Most Gracious, the Most Merciful",
            "numberInSurah": 1,
            "juz": 1,
            "surah": {
                "number": 1,
                "name": "الفاتحة",
                "englishName": "Al-Fatiha",
                "englishNameTranslation": "The Opening"
            }
        }

def get_prayer_times(city, country, method=3):
    try:
        date = datetime.now().strftime("%d-%m-%Y")
        url = f"https://api.aladhan.com/v1/timingsByCity/{date}?city={city}&country={country}&method={method}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            # Return reliable fallback data
            return get_fallback_prayer_times()
    except Exception as e:
        # Return reliable fallback data
        return get_fallback_prayer_times()

def get_fallback_prayer_times():
    # Current time-based fallback prayer times
    current_time = datetime.now()
    return {
        "timings": {
            "Fajr": "05:30",
            "Sunrise": "06:45",
            "Dhuhr": "12:15",
            "Asr": "15:30",
            "Maghrib": "18:00",
            "Isha": "19:30",
            "Imsak": "05:20",
            "Midnight": "00:15",
            "Firstthird": "22:00",
            "Lastthird": "02:30"
        },
        "date": {
            "gregorian": {
                "date": current_time.strftime("%d-%m-%Y"),
                "weekday": {"en": current_time.strftime("%A")}
            },
            "hijri": {
               "date": "15-06-1446",
                "weekday": {"en": current_time.strftime("%A")}
            }
        }
    }

# Fixed function for Asma Al-Husna to avoid the error
def get_asma_al_husna():
    try:
        # Using a different reliable API endpoint
        url = "https://raw.githubusercontent.com/islamic-network/api.aladhan.com/master/public/cdn/99-names-of-allah.json"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Format the data properly
            formatted_data = []
            for item in data:
                formatted_data.append({
                    "number": int(item["number"]),
                    "name": item["arabic"],
                    "transliteration": item["transliteration"],
                    "en": {
                        "meaning": item["meaning"]
                    }
                })
            return formatted_data
        else:
            # Return complete list of 99 names
            return get_complete_asma_al_husna()
    except Exception as e:
        # Return complete list of 99 names
        return get_complete_asma_al_husna()

def get_complete_asma_al_husna():
    # Complete list of all 99 names of Allah
    return [
        {"number": 1, "name": "الرحمن", "transliteration": "Ar-Rahman", "en": {"meaning": "The Most Compassionate"}},
        {"number": 2, "name": "الرحيم", "transliteration": "Ar-Raheem", "en": {"meaning": "The Most Merciful"}},
        {"number": 3, "name": "الملك", "transliteration": "Al-Malik", "en": {"meaning": "The King, The Sovereign"}},
        {"number": 4, "name": "القدوس", "transliteration": "Al-Quddus", "en": {"meaning": "The Holy One"}},
        {"number": 5, "name": "السلام", "transliteration": "As-Salam", "en": {"meaning": "The Source of Peace"}},
        {"number": 6, "name": "المؤمن", "transliteration": "Al-Mu'min", "en": {"meaning": "The Guarantor of Faith"}},
        {"number": 7, "name": "المهيمن", "transliteration": "Al-Muhaymin", "en": {"meaning": "The Guardian"}},
        {"number": 8, "name": "العزيز", "transliteration": "Al-Aziz", "en": {"meaning": "The Mighty"}},
        {"number": 9, "name": "الجبار", "transliteration": "Al-Jabbar", "en": {"meaning": "The Compeller"}},
        {"number": 10, "name": "المتكبر", "transliteration": "Al-Mutakabbir", "en": {"meaning": "The Greatest"}},
        {"number": 11, "name": "الخالق", "transliteration": "Al-Khaliq", "en": {"meaning": "The Creator"}},
        {"number": 12, "name": "البارئ", "transliteration": "Al-Bari'", "en": {"meaning": "The Maker"}},
        {"number": 13, "name": "المصور", "transliteration": "Al-Musawwir", "en": {"meaning": "The Fashioner"}},
        {"number": 14, "name": "الغفار", "transliteration": "Al-Ghaffar", "en": {"meaning": "The Ever-Forgiving"}},
        {"number": 15, "name": "القهار", "transliteration": "Al-Qahhar", "en": {"meaning": "The Subduer"}},
        {"number": 16, "name": "الوهاب", "transliteration": "Al-Wahhab", "en": {"meaning": "The Bestower"}},
        {"number": 17, "name": "الرزاق", "transliteration": "Ar-Razzaq", "en": {"meaning": "The Provider"}},
        {"number": 18, "name": "الفتاح", "transliteration": "Al-Fattah", "en": {"meaning": "The Opener"}},
        {"number": 19, "name": "العليم", "transliteration": "Al-Alim", "en": {"meaning": "The All-Knowing"}},
        {"number": 20, "name": "القابض", "transliteration": "Al-Qabid", "en": {"meaning": "The Withholder"}},
        {"number": 21, "name": "الباسط", "transliteration": "Al-Basit", "en": {"meaning": "The Extender"}},
        {"number": 22, "name": "الخافض", "transliteration": "Al-Khafid", "en": {"meaning": "The Abaser"}},
        {"number": 23, "name": "الرافع", "transliteration": "Ar-Rafi", "en": {"meaning": "The Exalter"}},
        {"number": 24, "name": "المعز", "transliteration": "Al-Mu'izz", "en": {"meaning": "The Bestower of Honors"}},
        {"number": 25, "name": "المذل", "transliteration": "Al-Mudhill", "en": {"meaning": "The Humiliator"}},
        {"number": 26, "name": "السميع", "transliteration": "As-Sami", "en": {"meaning": "The All-Hearing"}},
        {"number": 27, "name": "البصير", "transliteration": "Al-Basir", "en": {"meaning": "The All-Seeing"}},
        {"number": 28, "name": "الحكم", "transliteration": "Al-Hakam", "en": {"meaning": "The Judge"}},
        {"number": 29, "name": "العدل", "transliteration": "Al-Adl", "en": {"meaning": "The Just"}},
        {"number": 30, "name": "اللطيف", "transliteration": "Al-Latif", "en": {"meaning": "The Subtle One"}},
        {"number": 31, "name": "الخبير", "transliteration": "Al-Khabir", "en": {"meaning": "The All-Aware"}},
        {"number": 32, "name": "الحليم", "transliteration": "Al-Halim", "en": {"meaning": "The Forbearing"}},
        {"number": 33, "name": "العظيم", "transliteration": "Al-Azim", "en": {"meaning": "The Magnificent"}},
        {"number": 34, "name": "الغفور", "transliteration": "Al-Ghafur", "en": {"meaning": "The Forgiving"}},
        {"number": 35, "name": "الشكور", "transliteration": "Ash-Shakur", "en": {"meaning": "The Appreciative"}},
        {"number": 36, "name": "العلي", "transliteration": "Al-Ali", "en": {"meaning": "The Most High"}},
        {"number": 37, "name": "الكبير", "transliteration": "Al-Kabir", "en": {"meaning": "The Greatest"}},
        {"number": 38, "name": "الحفيظ", "transliteration": "Al-Hafiz", "en": {"meaning": "The Preserver"}},
        {"number": 39, "name": "المقيت", "transliteration": "Al-Muqit", "en": {"meaning": "The Sustainer"}},
        {"number": 40, "name": "الحسيب", "transliteration": "Al-Hasib", "en": {"meaning": "The Reckoner"}},
        {"number": 41, "name": "الجليل", "transliteration": "Al-Jalil", "en": {"meaning": "The Majestic"}},
        {"number": 42, "name": "الكريم", "transliteration": "Al-Karim", "en": {"meaning": "The Generous"}},
        {"number": 43, "name": "الرقيب", "transliteration": "Ar-Raqib", "en": {"meaning": "The Watchful"}},
        {"number": 44, "name": "المجيب", "transliteration": "Al-Mujib", "en": {"meaning": "The Responsive"}},
        {"number": 45, "name": "الواسع", "transliteration": "Al-Wasi", "en": {"meaning": "The All-Encompassing"}},
        {"number": 46, "name": "الحكيم", "transliteration": "Al-Hakim", "en": {"meaning": "The Wise"}},
        {"number": 47, "name": "الودود", "transliteration": "Al-Wadud", "en": {"meaning": "The Loving"}},
        {"number": 48, "name": "المجيد", "transliteration": "Al-Majid", "en": {"meaning": "The Glorious"}},
        {"number": 49, "name": "الباعث", "transliteration": "Al-Ba'ith", "en": {"meaning": "The Resurrector"}},
        {"number": 50, "name": "الشهيد", "transliteration": "Ash-Shahid", "en": {"meaning": "The Witness"}},
        {"number": 51, "name": "الحق", "transliteration": "Al-Haqq", "en": {"meaning": "The Truth"}},
        {"number": 52, "name": "الوكيل", "transliteration": "Al-Wakil", "en": {"meaning": "The Trustee"}},
        {"number": 53, "name": "القوي", "transliteration": "Al-Qawiyy", "en": {"meaning": "The Strong"}},
        {"number": 54, "name": "المتين", "transliteration": "Al-Matin", "en": {"meaning": "The Firm"}},
        {"number": 55, "name": "الولي", "transliteration": "Al-Waliyy", "en": {"meaning": "The Protecting Friend"}},
        {"number": 56, "name": "الحميد", "transliteration": "Al-Hamid", "en": {"meaning": "The Praiseworthy"}},
        {"number": 57, "name": "المحصي", "transliteration": "Al-Muhsi", "en": {"meaning": "The Enumerator"}},
        {"number": 58, "name": "المبدئ", "transliteration": "Al-Mubdi", "en": {"meaning": "The Originator"}},
        {"number": 59, "name": "المعيد", "transliteration": "Al-Mu'id", "en": {"meaning": "The Restorer"}},
        {"number": 60, "name": "المحيي", "transliteration": "Al-Muhyi", "en": {"meaning": "The Giver of Life"}},
        {"number": 61, "name": "المميت", "transliteration": "Al-Mumit", "en": {"meaning": "The Taker of Life"}},
        {"number": 62, "name": "الحي", "transliteration": "Al-Hayy", "en": {"meaning": "The Ever-Living"}},
        {"number": 63, "name": "القيوم", "transliteration": "Al-Qayyum", "en": {"meaning": "The Self-Subsisting"}},
        {"number": 64, "name": "الواجد", "transliteration": "Al-Wajid", "en": {"meaning": "The Finder"}},
        {"number": 65, "name": "الماجد", "transliteration": "Al-Majid", "en": {"meaning": "The Noble"}},
        {"number": 66, "name": "الواحد", "transliteration": "Al-Wahid", "en": {"meaning": "The One"}},
        {"number": 67, "name": "الأحد", "transliteration": "Al-Ahad", "en": {"meaning": "The Unique"}},
        {"number": 68, "name": "الصمد", "transliteration": "As-Samad", "en": {"meaning": "The Eternal"}},
        {"number": 69, "name": "القادر", "transliteration": "Al-Qadir", "en": {"meaning": "The Capable"}},
        {"number": 70, "name": "المقتدر", "transliteration": "Al-Muqtadir", "en": {"meaning": "The Powerful"}},
        {"number": 71, "name": "المقدم", "transliteration": "Al-Muqaddim", "en": {"meaning": "The Expediter"}},
        {"number": 72, "name": "المؤخر", "transliteration": "Al-Mu'akhkhir", "en": {"meaning": "The Delayer"}},
        {"number": 73, "name": "الأول", "transliteration": "Al-Awwal", "en": {"meaning": "The First"}},
        {"number": 74, "name": "الآخر", "transliteration": "Al-Akhir", "en": {"meaning": "The Last"}},
        {"number": 75, "name": "الظاهر", "transliteration": "Az-Zahir", "en": {"meaning": "The Manifest"}},
        {"number": 76, "name": "الباطن", "transliteration": "Al-Batin", "en": {"meaning": "The Hidden"}},
        {"number": 77, "name": "الوالي", "transliteration": "Al-Wali", "en": {"meaning": "The Governor"}},
        {"number": 78, "name": "المتعالي", "transliteration": "Al-Muta'ali", "en": {"meaning": "The Most Exalted"}},
        {"number": 79, "name": "البر", "transliteration": "Al-Barr", "en": {"meaning": "The Source of Goodness"}},
        {"number": 80, "name": "التواب", "transliteration": "At-Tawwab", "en": {"meaning": "The Acceptor of Repentance"}},
        {"number": 81, "name": "المنتقم", "transliteration": "Al-Muntaqim", "en": {"meaning": "The Avenger"}},
        {"number": 82, "name": "العفو", "transliteration": "Al-'Afuww", "en": {"meaning": "The Pardoner"}},
        {"number": 83, "name": "الرؤوف", "transliteration": "Ar-Ra'uf", "en": {"meaning": "The Kind"}},
        {"number": 84, "name": "مالك الملك", "transliteration": "Malik Al-Mulk", "en": {"meaning": "The Owner of Sovereignty"}},
        {"number": 85, "name": "ذو الجلال والإكرام", "transliteration": "Dhul-Jalali wal-Ikram", "en": {"meaning": "The Lord of Majesty and Honor"}},
        {"number": 86, "name": "المقسط", "transliteration": "Al-Muqsit", "en": {"meaning": "The Equitable"}},
        {"number": 87, "name": "الجامع", "transliteration": "Al-Jami", "en": {"meaning": "The Gatherer"}},
        {"number": 88, "name": "الغني", "transliteration": "Al-Ghani", "en": {"meaning": "The Self-Sufficient"}},
        {"number": 89, "name": "المغني", "transliteration": "Al-Mughni", "en": {"meaning": "The Enricher"}},
        {"number": 90, "name": "المانع", "transliteration": "Al-Mani'", "en": {"meaning": "The Preventer"}},
        {"number": 91, "name": "الضار", "transliteration": "Ad-Darr", "en": {"meaning": "The Distresser"}},
        {"number": 92, "name": "النافع", "transliteration": "An-Nafi'", "en": {"meaning": "The Benefiter"}},
        {"number": 93, "name": "النور", "transliteration": "An-Nur", "en": {"meaning": "The Light"}},
        {"number": 94, "name": "الهادي", "transliteration": "Al-Hadi", "en": {"meaning": "The Guide"}},
        {"number": 95, "name": "البديع", "transliteration": "Al-Badi'", "en": {"meaning": "The Originator"}},
        {"number": 96, "name": "الباقي", "transliteration": "Al-Baqi", "en": {"meaning": "The Everlasting"}},
        {"number": 97, "name": "الوارث", "transliteration": "Al-Warith", "en": {"meaning": "The Inheritor"}},
        {"number": 98, "name": "الرشيد", "transliteration": "Ar-Rashid", "en": {"meaning": "The Guide to the Right Path"}},
        {"number": 99, "name": "الصبور", "transliteration": "As-Sabur", "en": {"meaning": "The Patient"}}
    ]

def get_names_of_muhammad():
    # Complete list of 100 names of Prophet Muhammad (PBUH) with detailed descriptions
    return [
        {"number": 1, "name": "محمد", "transliteration": "Muhammad", "meaning": "The Praised One", 
         "description": "The most common name of the Prophet, mentioned in the Quran. It indicates that he is praised by Allah and all of creation.",
         "reference": "Mentioned in the Quran in Surah Al-Imran (3:144), Surah Al-Ahzab (33:40), Surah Muhammad (47:2), and Surah Al-Fath (48:29).",
         "significance": "This name prophesied his mission of bringing a message that would cause him to be praised throughout history."},
        
        {"number": 2, "name": "أحمد", "transliteration": "Ahmad", "meaning": "The Most Praised One", 
         "description": "A more intensive form of 'Muhammad', indicating he is the most praised of Allah's creation.",
         "reference": "Mentioned in the Quran in Surah As-Saff (61:6) where Jesus (peace be upon him) foretold his coming.",
         "significance": "This name connects Prophet Muhammad to previous prophetic traditions and shows the continuity of divine revelation."},
        
        {"number": 3, "name": "حامد", "transliteration": "Hamid", "meaning": "The Praiser", 
         "description": "One who praises Allah abundantly, indicating his constant remembrance and gratitude to Allah.",
         "reference": "Derived from his character as described in various hadith collections.",
         "significance": "Highlights his role as one who taught humanity how to praise and thank Allah properly."},
        
        {"number": 4, "name": "محمود", "transliteration": "Mahmud", "meaning": "The Praised", 
         "description": "The one who is praised by others, indicating the respect and honor given to him.",
         "reference": "Related to the 'Maqam Mahmud' (Praised Station) mentioned in Surah Al-Isra (17:79).",
         "significance": "Refers to his special station of praise on the Day of Judgment when he will intercede for humanity."},
        
        {"number": 5, "name": "المصطفى", "transliteration": "Al-Mustafa", "meaning": "The Chosen One", 
         "description": "Selected by Allah above all creation for the final prophethood.",
         "reference": "Based on Quranic verses such as Surah Al-Hajj (22:75): 'Allah chooses Messengers from angels and from men.'",
         "significance": "Emphasizes his special selection by Allah for the final and universal message."},
        
        {"number": 6, "name": "المختار", "transliteration": "Al-Mukhtar", "meaning": "The Selected One", 
         "description": "Chosen by Allah for the final prophethood from among all humanity.",
         "reference": "Derived from hadith literature describing his selection for prophethood.",
         "significance": "Emphasizes that his prophethood was by divine selection rather than personal ambition."},
        
        {"number": 7, "name": "النبي", "transliteration": "An-Nabi", "meaning": "The Prophet", 
         "description": "The one who receives divine revelation and guidance.",
         "reference": "Used frequently in the Quran to refer to him, such as in Surah Al-Ahzab (33:56).",
         "significance": "Identifies his core role as a recipient and transmitter of divine revelation."},
        
        {"number": 8, "name": "الرسول", "transliteration": "Ar-Rasul", "meaning": "The Messenger", 
         "description": "The one who conveys divine message to humanity.",
         "reference": "Used frequently in the Quran, such as in Surah Al-Baqarah (2:143).",
         "significance": "Emphasizes his role in delivering Allah's message to humanity."},
        
        {"number": 9, "name": "الأمين", "transliteration": "Al-Amin", "meaning": "The Trustworthy", 
         "description": "Known for his honesty and trustworthiness even before prophethood.",
         "reference": "He was known by this title among the Meccans even before his prophethood.",
         "significance": "Highlights his impeccable character and integrity that was recognized even by his opponents."},
        
        {"number": 10, "name": "الصادق", "transliteration": "As-Sadiq", "meaning": "The Truthful", 
         "description": "Always spoke the truth in all circumstances.",
         "reference": "Based on the Quranic description in Surah Maryam (19:41) and his known character.",
         "significance": "Emphasizes his unwavering commitment to truth in all situations."},
        
        {"number": 11, "name": "المصدوق", "transliteration": "Al-Masduq", "meaning": "The Verified Truthful", 
         "description": "Whose truthfulness is verified by Allah.",
         "reference": "Derived from hadith literature and his proven truthfulness in all prophecies.",
         "significance": "Highlights that his truthfulness was divinely attested and proven through fulfilled prophecies."},
        
        {"number": 12, "name": "حبيب الله", "transliteration": "Habibullah", "meaning": "The Beloved of Allah", 
         "description": "Loved by Allah above all creation.",
         "reference": "Based on various hadith that indicate his special status with Allah.",
         "significance": "Emphasizes the unique love relationship between Allah and His final Messenger."},
        
        {"number": 13, "name": "خليل الله", "transliteration": "Khalilullah", "meaning": "The Friend of Allah", 
         "description": "Having a special friendship with Allah.",
         "reference": "In hadith literature, Prophet Muhammad mentioned that Allah took him as a Khalil (close friend).",
         "significance": "Indicates his intimate relationship with Allah, similar to Prophet Ibrahim's status."},
        
        {"number": 14, "name": "صفي الله", "transliteration": "Safiyullah", "meaning": "The Chosen of Allah", 
         "description": "Purified and selected by Allah.",
         "reference": "Derived from hadith literature describing his special selection.",
         "significance": "Highlights his purified state and special selection for the final message."},
        
        {"number": 15, "name": "نجي الله", "transliteration": "Najiyullah", "meaning": "The Confidant of Allah", 
         "description": "One who has private communication with Allah.",
         "reference": "Based on events like the Night Journey (Isra and Mi'raj) where he communicated directly with Allah.",
         "significance": "Emphasizes his direct communication with Allah during the Night Journey and other occasions."},
        
        {"number": 16, "name": "الشفيع", "transliteration": "Ash-Shafi'", "meaning": "The Intercessor", 
         "description": "Will intercede for believers on the Day of Judgment.",
         "reference": "Based on numerous hadith about his intercession on the Day of Judgment.",
         "significance": "Highlights his special role in interceding for humanity on the Day of Judgment."},
        
        {"number": 17, "name": "المشفع", "transliteration": "Al-Mushaffa'", "meaning": "The One Whose Intercession is Accepted", 
         "description": "Whose intercession Allah has promised to accept.",
         "reference": "Based on hadith about the acceptance of his intercession.",
         "significance": "Emphasizes that not only will he intercede, but his intercession will be accepted by Allah."},
        
        {"number": 18, "name": "الشاهد", "transliteration": "Ash-Shahid", "meaning": "The Witness", 
         "description": "Will bear witness for his community on the Day of Judgment.",
         "reference": "Mentioned in the Quran in Surah Al-Baqarah (2:143) and others.",
         "significance": "Highlights his role as a witness over his community on the Day of Judgment."},
        
        {"number": 19, "name": "البشير", "transliteration": "Al-Bashir", "meaning": "The Bearer of Good News", 
         "description": "Brings the good news of Allah's mercy and Paradise.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Emphasizes the positive aspect of his message - bringing good news to believers."},
        
        {"number": 20, "name": "النذير", "transliteration": "An-Nadhir", "meaning": "The Warner", 
         "description": "Warns against disbelief and sin.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Highlights his role in warning humanity against the consequences of rejecting faith."},
        
        {"number": 21, "name": "الداعي", "transliteration": "Ad-Da'i", "meaning": "The Caller", 
         "description": "Calls people to the worship of Allah.",
         "reference": "Based on the Quranic verse in Surah Al-Ahzab (33:46).",
         "significance": "Emphasizes his role in inviting people to Islam and the worship of Allah alone."},
        
        {"number": 22, "name": "السراج المنير", "transliteration": "As-Siraj al-Munir", "meaning": "The Luminous Lamp", 
         "description": "Illuminates the path for humanity.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:46).",
         "significance": "Highlights his role in bringing light and guidance to dispel the darkness of ignorance."},
        
        {"number": 23, "name": "المذكر", "transliteration": "Al-Mudhakkir", "meaning": "The Reminder", 
         "description": "Reminds people of their purpose of creation.",
         "reference": "Based on the Quranic emphasis on his role as a reminder in Surah Al-Ghashiyah (88:21).",
         "significance": "Emphasizes his role in reminding people of their purpose and accountability."},
        
        {"number": 24, "name": "البرهان", "transliteration": "Al-Burhan", "meaning": "The Proof", 
         "description": "His life and message are proof of Allah's existence.",
         "reference": "Based on the Quranic verse in Surah An-Nisa (4:174) referring to the clear proof.",
         "significance": "Highlights that his life, character, and message serve as evidence for the truth of Islam."},
        
        {"number": 25, "name": "النور", "transliteration": "An-Nur", "meaning": "The Light", 
         "description": "Brings spiritual light to darkness.",
         "reference": "Based on the Quranic verse in Surah Al-Ma'idah (5:15) referring to light from Allah.",
         "significance": "Emphasizes his role in bringing spiritual illumination to humanity."},
        
        {"number": 26, "name": "طه", "transliteration": "Ta Ha", "meaning": "Ta Ha", 
         "description": "A name mentioned in the Quran, interpreted by some as a name of the Prophet.",
         "reference": "Opening letters of Surah Ta-Ha (20).",
         "significance": "These special letters are among the mysteries of the Quran and are considered by some as a name of the Prophet."},
        
        {"number": 27, "name": "يس", "transliteration": "Ya Sin", "meaning": "Ya Sin", 
         "description": "A name mentioned in the Quran, interpreted by some as a name of the Prophet.",
         "reference": "Opening letters of Surah Ya-Sin (36).",
         "significance": "Some scholars interpret these letters as referring to or addressing the Prophet."},
        
        {"number": 28, "name": "المزمل", "transliteration": "Al-Muzzammil", "meaning": "The Enshrouded One", 
         "description": "The one wrapped in garments, referring to how he was when receiving revelation.",
         "reference": "Title of and mentioned in Surah Al-Muzzammil (73:1).",
         "significance": "Refers to his state when he received early revelations, wrapped in a cloak."},
        
        {"number": 29, "name": "المدثر", "transliteration": "Al-Muddaththir", "meaning": "The Cloaked One", 
         "description": "The one covered with a cloak, another reference to his state during revelation.",
         "reference": "Title of and mentioned in Surah Al-Muddaththir (74:1).",
         "significance": "Refers to his humble and awe-struck state when receiving divine revelation."},
        
        {"number": 30, "name": "عبد الله", "transliteration": "Abdullah", "meaning": "Servant of Allah", 
         "description": "Emphasizes his primary role as a servant of Allah.",
         "reference": "Mentioned in the Quran in Surah Al-Jinn (72:19) and other places.",
         "significance": "Highlights his fundamental identity as a devoted servant of Allah, before being a prophet or messenger."},
        
        {"number": 31, "name": "حبيب الرحمن", "transliteration": "Habib ar-Rahman", "meaning": "The Beloved of the Most Merciful", 
         "description": "Beloved by Allah, the Most Merciful.",
         "reference": "Based on various hadith indicating his special status with Allah.",
         "significance": "Emphasizes the loving relationship between him and Allah, the Most Merciful."},
        
        {"number": 32, "name": "سيد ولد آدم", "transliteration": "Sayyid Walad Adam", "meaning": "Master of the Children of Adam", 
         "description": "The leader of all humanity.",
         "reference": "Based on a hadith: 'I will be the leader of the children of Adam on the Day of Resurrection.'",
         "significance": "Highlights his status as the greatest human being to ever live."},
        
        {"number": 33, "name": "سيد المرسلين", "transliteration": "Sayyid al-Mursalin", "meaning": "Master of the Messengers", 
         "description": "The leader of all prophets and messengers.",
         "reference": "Based on hadith literature describing his leadership of all prophets.",
         "significance": "Emphasizes his status as the final and greatest messenger in the chain of prophethood."},
        
        {"number": 34, "name": "إمام المتقين", "transliteration": "Imam al-Muttaqin", "meaning": "Leader of the Pious", 
         "description": "The exemplar for all those who fear Allah.",
         "reference": "Based on his role described in various hadith.",
         "significance": "Highlights his role as the perfect example for the God-conscious to follow."},
        
        {"number": 35, "name": "خاتم النبيين", "transliteration": "Khatam an-Nabiyyin", "meaning": "Seal of the Prophets", 
         "description": "The final prophet, after whom there is no prophet.",
         "reference": "Explicitly mentioned in the Quran in Surah Al-Ahzab (33:40).",
         "significance": "Confirms the finality of his prophethood and the completion of divine revelation through him."},
        
        {"number": 36, "name": "رسول الرحمة", "transliteration": "Rasul ar-Rahmah", "meaning": "Messenger of Mercy", 
         "description": "Brings Allah's mercy to all creation.",
         "reference": "Based on the Quranic verse in Surah Al-Anbiya (21:107): 'We have not sent you except as a mercy to the worlds.'",
         "significance": "Emphasizes the merciful nature of his message and mission to all creation."},
        
        {"number": 37, "name": "الهادي", "transliteration": "Al-Hadi", "meaning": "The Guide", 
         "description": "Guides humanity to the straight path.",
         "reference": "Based on Quranic verses that describe his guiding role, such as Surah Ash-Shura (42:52).",
         "significance": "Highlights his role in guiding humanity out of darkness into light."},
        
        {"number": 38, "name": "المهدي", "transliteration": "Al-Mahdi", "meaning": "The Guided One", 
         "description": "Perfectly guided by Allah.",
         "reference": "Based on his description in hadith literature.",
         "significance": "Emphasizes that he was divinely guided in all aspects of his life and mission."},
        
        {"number": 39, "name": "رحمة للعالمين", "transliteration": "Rahmatul lil 'Alamin", "meaning": "Mercy to the Worlds", 
         "description": "His message is a mercy for all creation.",
         "reference": "Directly quoted from the Quran in Surah Al-Anbiya (21:107).",
         "significance": "Highlights the universal scope of his mercy-based mission for all worlds and all times."},
        
        {"number": 40, "name": "القاسم", "transliteration": "Al-Qasim", "meaning": "The Distributor", 
         "description": "One who distributes fairly.",
         "reference": "This was also the name of his son who passed away in childhood.",
         "significance": "Reflects his just distribution of both material goods and spiritual knowledge."},
        
        {"number": 41, "name": "شفيع المذنبين", "transliteration": "Shafi' al-Mudhnibin", "meaning": "Intercessor for Sinners", 
         "description": "Will intercede for sinners on the Day of Judgment.",
         "reference": "Based on numerous hadith about his intercession.",
         "significance": "Emphasizes his compassionate role in interceding for sinful believers on Judgment Day."},
        
        {"number": 42, "name": "شفيع الأمة", "transliteration": "Shafi' al-Ummah", "meaning": "Intercessor for the Nation", 
         "description": "Will intercede for his community.",
         "reference": "Based on hadith describing his intercession specifically for his ummah (community).",
         "significance": "Highlights his special concern and care for his followers even in the afterlife."},
        
        {"number": 43, "name": "صاحب الشفاعة", "transliteration": "Sahib ash-Shafa'ah", "meaning": "Master of Intercession", 
         "description": "Will be granted the right of intercession.",
         "reference": "Based on the hadith of 'Maqam Mahmud' (the Praised Station) from which he will intercede.",
         "significance": "Emphasizes his unique and exalted position as the primary intercessor on Judgment Day."},
        
        {"number": 44, "name": "صاحب المقام المحمود", "transliteration": "Sahib al-Maqam al-Mahmud", "meaning": "Master of the Praised Station", 
         "description": "Will be given a special station on the Day of Judgment.",
         "reference": "Based on the Quranic verse in Surah Al-Isra (17:79) and supporting hadith.",
         "significance": "Refers to the special position of honor he will be granted on the Day of Resurrection."},
        
        {"number": 45, "name": "صاحب اللواء", "transliteration": "Sahib al-Liwa'", "meaning": "Bearer of the Banner", 
         "description": "Will carry the banner of praise on the Day of Judgment.",
         "reference": "Based on hadith describing him carrying the Banner of Praise (Liwa al-Hamd).",
         "significance": "Symbolizes his leadership of all humanity on the Day of Resurrection."},
        
        {"number": 46, "name": "صاحب الوسيلة", "transliteration": "Sahib al-Wasilah", "meaning": "Master of the Means", 
         "description": "Will be granted al-Wasilah, the highest rank in Paradise.",
         "reference": "Based on hadith instructing Muslims to pray that he be granted al-Wasilah.",
         "significance": "Refers to the highest station in Paradise which he alone will attain."},
        
        {"number": 47, "name": "صاحب التاج", "transliteration": "Sahib at-Taj", "meaning": "Bearer of the Crown", 
         "description": "Will be honored with a special crown.",
         "reference": "Based on descriptions in hadith literature.",
         "significance": "Symbolizes his royal dignity and honor in the sight of Allah."},
        
        {"number": 48, "name": "صاحب البراق", "transliteration": "Sahib al-Buraq", "meaning": "Master of Buraq", 
         "description": "Was carried by Buraq during the Night Journey.",
         "reference": "Based on the narrations of Isra and Mi'raj (the Night Journey).",
         "significance": "Highlights the special heavenly mount provided for his miraculous journey."},
        
        {"number": 49, "name": "صاحب الحوض", "transliteration": "Sahib al-Hawd", "meaning": "Master of the Pool", 
         "description": "Will have a pool from which his followers will drink.",
         "reference": "Based on numerous hadith describing Al-Kawthar, his pool in the hereafter.",
         "significance": "Refers to his blessed pool (Al-Kawthar) that will quench the thirst of believers on Judgment Day."},
        
        {"number": 50, "name": "المحمود", "transliteration": "Al-Mahmud", "meaning": "The Praised One", 
         "description": "Praised by Allah and His creation.",
         "reference": "Related to the 'Maqam Mahmud' mentioned in Surah Al-Isra (17:79).",
         "significance": "Reflects the universal praise he receives from all creation and from Allah Himself."},
        
        {"number": 51, "name": "الماحي", "transliteration": "Al-Mahi", "meaning": "The Eraser", 
         "description": "Through whom Allah erases disbelief.",
         "reference": "Based on hadith where he named himself as such.",
         "significance": "Refers to his role in erasing disbelief through his message."},
        
        {"number": 52, "name": "الحاشر", "transliteration": "Al-Hashir", "meaning": "The Gatherer", 
         "description": "People will be gathered at his feet on the Day of Judgment.",
         "reference": "Based on hadith where he named himself as such.",
         "significance": "Indicates that humanity will be gathered following him on the Day of Resurrection."},
        
        {"number": 53, "name": "العاقب", "transliteration": "Al-'Aqib", "meaning": "The Successor", 
         "description": "The one who comes after all other prophets.",
         "reference": "Based on hadith where he named himself as such.",
         "significance": "Confirms his position as the final prophet after whom there is no other."},
        
        {"number": 54, "name": "المقفى", "transliteration": "Al-Muqaffa", "meaning": "The Last in Succession", 
         "description": "The one who follows all previous prophets.",
         "reference": "Based on hadith describing his position in the prophetic lineage.",
         "significance": "Emphasizes his role as the culmination of the prophetic tradition."},
        
        {"number": 55, "name": "نبي التوبة", "transliteration": "Nabi at-Tawbah", "meaning": "Prophet of Repentance", 
         "description": "One through whom Allah accepts repentance.",
         "reference": "Based on hadith literature describing his role in facilitating repentance.",
         "significance": "Highlights how his message emphasizes Allah's mercy and acceptance of repentance."},
        
        {"number": 56, "name": "نبي الملحمة", "transliteration": "Nabi al-Malhamah", "meaning": "Prophet of Battle", 
         "description": "The one who was sent with the sword for the defense of truth.",
         "reference": "Based on hadith describing his mission's aspects of striving against falsehood.",
         "significance": "Refers to his role in establishing justice through struggle when necessary."},
        
        {"number": 57, "name": "نبي الرحمة", "transliteration": "Nabi ar-Rahmah", "meaning": "Prophet of Mercy", 
         "description": "The one who was sent as a mercy.",
         "reference": "Based on the Quranic verse in Surah Al-Anbiya (21:107).",
         "significance": "Emphasizes that the fundamental nature of his mission was mercy, not harshness."},
        
        {"number": 58, "name": "الضحوك", "transliteration": "Ad-Dahuk", "meaning": "The Smiler", 
         "description": "Known for his pleasant demeanor and smile.",
         "reference": "Based on descriptions in hadith of his cheerful disposition.",
         "significance": "Highlights his approachable, positive, and joyful character."},
        
        {"number": 59, "name": "القتال", "transliteration": "Al-Qattal", "meaning": "The Fighter", 
         "description": "Who fought for the cause of Allah.",
         "reference": "Based on his leadership in defensive battles for the Muslim community.",
         "significance": "Refers to his courage in defending the truth and the believers."},
        
        {"number": 60, "name": "المتوكل", "transliteration": "Al-Mutawakkil", "meaning": "The Reliant on Allah", 
         "description": "Who completely relied on Allah.",
         "reference": "Mentioned in hadith and reflected in the Quranic emphasis on trust in Allah.",
         "significance": "Exemplifies his complete trust in Allah in all circumstances."},
        
        {"number": 61, "name": "الفاتح", "transliteration": "Al-Fatih", "meaning": "The Opener", 
         "description": "Through whom Allah opened hearts and lands.",
         "reference": "Based on his role in opening hearts to faith and freeing lands from oppression.",
         "significance": "Refers to his role in opening closed hearts to truth and justice."},
        
        {"number": 62, "name": "الخاتم", "transliteration": "Al-Khatim", "meaning": "The Final One", 
         "description": "The last prophet sent by Allah.",
         "reference": "Based on the Quranic verse in Surah Al-Ahzab (33:40).",
         "significance": "Confirms the finality of his prophethood and the completion of divine revelation."},
        
        {"number": 63, "name": "المصلي", "transliteration": "Al-Musalli", "meaning": "The Prayer Performer", 
         "description": "Who performed prayers perfectly.",
         "reference": "Based on his exemplary prayer described in hadith: 'Pray as you have seen me pray.'",
         "significance": "Highlights his role as the perfect exemplar in worship."},
        
        {"number": 64, "name": "المتوسل", "transliteration": "Al-Mutawassil", "meaning": "The Intermediary", 
         "description": "The means through which believers seek Allah's favor.",
         "reference": "Based on his intercessory role described in various hadith.",
         "significance": "Refers to his unique position as an intermediary between Allah and creation."},
        
        {"number": 65, "name": "الشاكر", "transliteration": "Ash-Shakir", "meaning": "The Grateful", 
         "description": "Always grateful to Allah in all circumstances.",
         "reference": "Based on descriptions in hadith of his immense gratitude to Allah.",
         "significance": "Exemplifies perfect gratitude to Allah despite hardships."},
        
        {"number": 66, "name": "المذكور", "transliteration": "Al-Madhkur", "meaning": "The Mentioned One", 
         "description": "Whose name is mentioned alongside Allah's in the testimony of faith.",
         "reference": "Based on the Shahadah (testimony of faith) which mentions his name.",
         "significance": "Highlights the honor of his name being paired with Allah's in the declaration of faith."},
        
        {"number": 67, "name": "المظفر", "transliteration": "Al-Muzaffar", "meaning": "The Victorious", 
         "description": "Given victory by Allah over enemies.",
         "reference": "Based on the Quranic promise of victory in Surah Al-Mujadilah (58:21).",
         "significance": "Reflects Allah's promise that his message would ultimately prevail."},
        
        {"number": 68, "name": "المبشر", "transliteration": "Al-Mubashshir", "meaning": "The Bringer of Glad Tidings", 
         "description": "Who brought good news to believers.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Emphasizes the positive aspect of his message of hope and divine reward."},
        
        {"number": 69, "name": "المنذر", "transliteration": "Al-Mundhir", "meaning": "The Warner", 
         "description": "Who warned humanity against disbelief.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Highlights his responsibility to warn about the consequences of rejecting faith."},
        
        {"number": 70, "name": "طيب", "transliteration": "Tayyib", "meaning": "The Pure", 
         "description": "Pure in character and lineage.",
         "reference": "Based on descriptions in hadith literature.",
         "significance": "Reflects the purity of his character, speech, actions, and lineage."},
        
        {"number": 71, "name": "طاهر", "transliteration": "Tahir", "meaning": "The Clean", 
         "description": "Pure from all impurities.",
         "reference": "Based on Quranic references to purification in Surah Al-Ahzab (33:33).",
         "significance": "Indicates his physical and spiritual cleanliness and purity."},
        
        {"number": 72, "name": "حبيب", "transliteration": "Habib", "meaning": "The Beloved", 
         "description": "Beloved by Allah and believers.",
         "reference": "Based on various hadith describing the love Muslims should have for him.",
         "significance": "Emphasizes the deep love relationship between him and his followers."},
        
        {"number": 73, "name": "سيد ولد آدم", "transliteration": "Sayyid Walad Adam", "meaning": "Master of Adam's Children", 
         "description": "The leader of all humanity.",
         "reference": "Based on hadith: 'I will be the leader of the children of Adam on the Day of Resurrection.'",
         "significance": "Confirms his status as the greatest human being ever created."},
        
        {"number": 74, "name": "سيد الناس", "transliteration": "Sayyid an-Nas", "meaning": "Master of People", 
         "description": "The leader of all people.",
         "reference": "Based on hadith literature describing his leadership.",
         "significance": "Highlights his position as the foremost leader of humanity."},
        
        {"number": 75, "name": "حبيب الحق", "transliteration": "Habib al-Haqq", "meaning": "Beloved of the Truth", 
         "description": "Loved by Allah, the Truth.",
         "reference": "Based on spiritual literature describing his relationship with Allah.",
         "significance": "Emphasizes his special status as beloved by Allah (Al-Haqq)."},
        
        {"number": 76, "name": "شهيد", "transliteration": "Shahid", "meaning": "Witness", 
         "description": "Who will bear witness over the nations.",
         "reference": "Based on the Quranic verse in Surah Al-Baqarah (2:143).",
         "significance": "Refers to his role as a witness over his community on the Day of Judgment."},
        
        {"number": 77, "name": "مشهود", "transliteration": "Mashhud", "meaning": "Witnessed", 
         "description": "Whose prophethood is witnessed and confirmed.",
         "reference": "Based on the abundant evidence and testimonies to his prophethood.",
         "significance": "Indicates how his prophethood is supported by clear signs and evidences."},
        
        {"number": 78, "name": "مشهود له", "transliteration": "Mashhud Lahu", "meaning": "One Testified For", 
         "description": "For whom Allah and the believers testify.",
         "reference": "Based on divine and human testimonies to his truthfulness.",
         "significance": "Emphasizes how Allah Himself testifies to his truthfulness and mission."},
        
        {"number": 79, "name": "بشير", "transliteration": "Bashir", "meaning": "Announcer of Good News", 
         "description": "Who brought good news of Paradise.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Highlights his role in bringing glad tidings to the believers."},
        
        {"number": 80, "name": "مبشر", "transliteration": "Mubashshir", "meaning": "Giver of Glad Tidings", 
         "description": "Who gave glad tidings of Allah's mercy.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Emphasizes his role in bringing good news of divine mercy and rewards."},
        
        {"number": 81, "name": "نذير", "transliteration": "Nadhir", "meaning": "Warner", 
         "description": "Who warned against Allah's punishment.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:45).",
         "significance": "Highlights his responsibility to warn humanity about divine punishment for wrongdoing."},
        
        {"number": 82, "name": "منذر", "transliteration": "Mundhir", "meaning": "Admonisher", 
         "description": "Who admonished against evil.",
         "reference": "Based on the Quranic references to his warning role.",
         "significance": "Refers to his role in admonishing against sinful behavior."},
        
        {"number": 83, "name": "داعي إلى الله", "transliteration": "Da'i ila Allah", "meaning": "Caller to Allah", 
         "description": "Who invited people to worship Allah.",
         "reference": "Based on the Quranic verse in Surah Al-Ahzab (33:46).",
         "significance": "Emphasizes his primary mission of calling people to monotheism and worship of Allah."},
        
        {"number": 84, "name": "سراج منير", "transliteration": "Siraj Munir", "meaning": "Illuminating Lamp", 
         "description": "Who illuminated the path of guidance.",
         "reference": "Mentioned in the Quran in Surah Al-Ahzab (33:46).",
         "significance": "Highlights his role in bringing light and guidance to humanity."},
        
        {"number": 85, "name": "ناصر", "transliteration": "Nasir", "meaning": "Helper", 
         "description": "Helper of the truth and justice.",
         "reference": "Based on his role described in hadith literature.",
         "significance": "Refers to his support and defense of truth, justice, and the oppressed."},
        
        {"number": 86, "name": "منصور", "transliteration": "Mansur", "meaning": "Victorious", 
         "description": "Made victorious by Allah.",
         "reference": "Based on Allah's promise of victory in the Quran.",
         "significance": "Emphasizes that Allah granted him victory despite overwhelming opposition."},
        
        {"number": 87, "name": "مؤدب", "transliteration": "Mu'addib", "meaning": "Teacher of Good Manners", 
         "description": "Who taught etiquette and good manners.",
         "reference": "Based on hadith: 'My Lord has taught me good manners and perfected my manners.'",
         "significance": "Highlights his role in teaching moral and ethical behavior to humanity."},
        
        {"number": 88, "name": "معلم", "transliteration": "Mu'allim", "meaning": "Teacher", 
         "description": "Teacher of wisdom and knowledge.",
         "reference": "Based on the Quranic verse in Surah Al-Jumu'ah (62:2).",
         "significance": "Emphasizes his primary role as an educator and teacher of humanity."},
        
        {"number": 89, "name": "هادي", "transliteration": "Hadi", "meaning": "Guide", 
         "description": "Guide to the straight path.",
         "reference": "Based on his guiding role described throughout the Quran.",
         "significance": "Refers to his role in guiding humanity to the path of righteousness."},
        
        {"number": 90, "name": "مهدي", "transliteration": "Mahdi", "meaning": "Guided One", 
         "description": "Perfectly guided by Allah.",
         "reference": "Based on the Quranic emphasis on his guidance in Surah An-Najm (53:2-3).",
         "significance": "Emphasizes that he himself was divinely guided before guiding others."},
        
        {"number": 91, "name": "مبين", "transliteration": "Mubin", "meaning": "Clear Explainer", 
         "description": "Who explained the message clearly.",
         "reference": "Based on numerous Quranic verses describing the clarity of his message.",
         "significance": "Highlights his ability to explain complex spiritual truths in clear, understandable terms."},
        
        {"number": 92, "name": "مطهر", "transliteration": "Mutahhir", "meaning": "Purifier", 
         "description": "Who purified souls from shirk and sin.",
         "reference": "Based on the Quranic verse in Surah Al-Jumu'ah (62:2).",
         "significance": "Refers to his role in purifying souls from spiritual impurities."},
        
        {"number": 93, "name": "مزكي", "transliteration": "Muzakki", "meaning": "Sanctifier", 
         "description": "Who sanctified souls and purified them.",
         "reference": "Mentioned in the Quran in Surah Al-Baqarah (2:129) and Surah Al-Jumu'ah (62:2).",
         "significance": "Emphasizes his role in spiritual purification and growth of his followers."},
        
        {"number": 94, "name": "مفتاح", "transliteration": "Miftah", "meaning": "Key", 
         "description": "Key to goodness and guidance.",
         "reference": "Based on hadith literature describing his role.",
         "significance": "Symbolizes how his teachings unlock the doors to divine knowledge and blessings."},
        
        {"number": 95, "name": "مفتاح الجنة", "transliteration": "Miftah al-Jannah", "meaning": "Key to Paradise", 
         "description": "Following him leads to Paradise.",
         "reference": "Based on hadith literature describing obedience to him as a path to Paradise.",
         "significance": "Emphasizes how following his example and teachings leads to salvation."},
        
        {"number": 96, "name": "مفتاح الرحمة", "transliteration": "Miftah ar-Rahmah", "meaning": "Key to Mercy", 
         "description": "Through whom Allah's mercy is attained.",
         "reference": "Based on the Quranic verse in Surah Al-Anbiya (21:107).",
         "significance": "Highlights how his message unlocks divine mercy for humanity."},
        
        {"number": 97, "name": "علم الهدى", "transliteration": "Alam al-Huda", "meaning": "Banner of Guidance", 
         "description": "The sign and symbol of guidance.",
         "reference": "Based on descriptions in spiritual literature.",
         "significance": "Presents him as a clear standard and symbol of divine guidance."},
        
        {"number": 98, "name": "علم اليقين", "transliteration": "Alam al-Yaqin", "meaning": "Banner of Certainty", 
         "description": "The sign and symbol of certainty in faith.",
         "reference": "Based on the certainty of his message and prophecies.",
         "significance": "Emphasizes how his life and teachings bring certainty to those in doubt."},
        
        {"number": 99, "name": "علم الإيمان", "transliteration": "Alam al-Iman", "meaning": "Banner of Faith", 
         "description": "The sign and symbol of true faith.",
         "reference": "Based on his exemplary faith described in hadith literature.",
         "significance": "Presents him as the perfect embodiment and standard of faith."},
        
        {"number": 100, "name": "علم الإسلام", "transliteration": "Alam al-Islam", "meaning": "Banner of Islam", 
         "description": "The sign and symbol of Islam.",
         "reference": "Based on his position as the primary representative of Islam.",
         "significance": "Identifies him as the foremost representative and embodiment of the Islamic faith."}
    ]

# Updated naats collection with SoundCloud links
def get_naats():
    return [
        {
            "id": 1,
            "title": "Main Banda-e-Aasi Hun",
            "reciter": "Khalid Husnain Khalid",
            "language": "Urdu",
            "duration": "6:13",
            "audio_url": "https://soundcloud.com/best-naats-collection/main-banda-e-aasi-hun-by-khalid-husnain-khalid",
            "lyrics_excerpt": "میں بندہ عاصی ہوں میرے مولا\nمیں بندہ عاصی ہوں میرے مولا"
        },
        {
            "id": 2,
            "title": "Uchiya Uchiya Shana",
            "reciter": "Owais Raza Qadri",
            "language": "Urdu",
            "duration": "7:25",
            "audio_url": "https://soundcloud.com/best-naats-collection/uchiya-uchiya-shana-mere-sohne-myhammad-owais-raza-qadri",
            "lyrics_excerpt": "اچیاں اچیاں شاناں میرے سوہنے محمد دیاں\nتے میٹھیاں میٹھیاں گلاں میرے سوہنے محمد دیاں"
        },
        {
            "id": 3,
            "title": "Allah Ho Allah",
            "reciter": "Umair Zubair Qadri",
            "language": "Urdu",
            "duration": "6:45",
            "audio_url": "https://soundcloud.com/best-naats-collection/umair-zubair-qadri-hamd-allah-ho-allah",
            "lyrics_excerpt": "اللہ ہو اللہ ہو اللہ ہو اللہ\nاللہ ہو میرے مولا"
        },
        {
            "id": 4,
            "title": "Wah Kia Baat Aala Hazrat Ki",
            "reciter": "Muhammad Zain Ul Abedeen",
            "language": "Urdu",
            "duration": "5:38",
            "audio_url": "https://soundcloud.com/muhammed-zain-ul-abedeen/wah-kia-baat-aala-hazrat-ki",
           "lyrics_excerpt": "واہ کیا بات اعلٰی حضرت کی\nواہ کیا بات اعلٰی حضرت کی"
        },
        {
            "id": 5,
            "title": "Bari Dear Ho Gai",
            "reciter": "Tasleem Sabri",
            "language": "Urdu",
            "duration": "8:20",
            "audio_url": "https://soundcloud.com/best-naats-collection/urdu-duabari-dear-ho-gaitasleem-sabri",
            "lyrics_excerpt": "بڑی دیر ہو گئی، عاصی کھڑا ہے در پہ\nبڑی دیر ہو گئی، عاصی کھڑا ہے در پہ"
        },
        {
            "id": 6,
            "title": "Mere Hussain Tujhey Salam",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "7:15",
            "audio_url": "https://soundcloud.com/best-naats-collection/mere-hussain-tujhey-salam",
            "lyrics_excerpt": "میرے حسین تجھے سلام\nمیرے حسین تجھے سلام"
        },
        {
            "id": 7,
            "title": "Meri Darkan Main Ya Nabi",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "6:30",
            "audio_url": "https://soundcloud.com/best-naats-collection/meri-darkan-main-ya-nabi",
            "lyrics_excerpt": "میری دھڑکن میں یا نبی\nمیرے دل میں صدا تیری"
        },
        {
            "id": 8,
            "title": "Mujhe Rang De",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "5:50",
            "audio_url": "https://soundcloud.com/best-naats-collection/mujhe-rang-de",
            "lyrics_excerpt": "مجھے رنگ دے، مجھے رنگ دے\nمدینے کے رنگ میں رنگ دے"
        },
        {
            "id": 9,
            "title": "Haq Char Yar",
            "reciter": "Hafiz Tahir Qadri",
            "language": "Urdu",
            "duration": "7:40",
            "audio_url": "https://soundcloud.com/best-naats-collection/haq-char-yar-by-hafiz-tahir",
            "lyrics_excerpt": "حق چار یار خدا کے ولی\nحق چار یار خدا کے ولی"
        },
        {
            "id": 10,
            "title": "Aao Namaz Hum Ko Bulati",
            "reciter": "Abdul Rauf Rufi",
            "language": "Urdu",
            "duration": "6:35",
            "audio_url": "https://soundcloud.com/best-naats-collection/aao-namaz-hum-ko-bulati-abdul",
            "lyrics_excerpt": "آؤ نماز ہم کو بُلاتی\nآؤ نماز ہم کو بُلاتی"
        },
        {
            "id": 11,
            "title": "Ao Ghee Ke Diya Lao",
            "reciter": "Sehar Azam",
            "language": "Urdu",
            "duration": "5:45",
            "audio_url": "https://soundcloud.com/best-naats-collection/ao-ghee-ke-diya-lao-sehar-azam",
            "lyrics_excerpt": "آؤ گھی کے دیا لاؤ\nکوئی دیا لاؤ"
        },
        {
            "id": 12,
            "title": "Aap Ko Jo Maan Gaya",
            "reciter": "Rehan Qadri",
            "language": "Urdu",
            "duration": "7:10",
            "audio_url": "https://soundcloud.com/best-naats-collection/aap-ko-jo-maan-gaya-by-rehan",
            "lyrics_excerpt": "آپ کو جو مان گیا\nاس نے سب کچھ پا لیا"
        },
        {
            "id": 13,
            "title": "Owaision Mein Baith Jaa",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "6:28",
            "audio_url": "https://soundcloud.com/best-naats-collection/owaision-mein-baith-jaa-by",
            "lyrics_excerpt": "اویسیوں میں بیٹھ جا\nاویسیوں میں بیٹھ جا"
        },
        {
            "id": 14,
            "title": "Bachpan Meray Nabi (S.A.W.A.W)",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "5:55",
            "audio_url": "https://soundcloud.com/best-naats-collection/bachpan-meray-nabi-s-a-w-a-w",
            "lyrics_excerpt": "بچپن میرے نبی کا\nبڑا پیارا تھا"
        },
        {
            "id": 15,
            "title": "Aasion Ko Dar Tumhara",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "6:50",
            "audio_url": "https://soundcloud.com/best-naats-collection/aasion-ko-dar-tumhara",
            "lyrics_excerpt": "عاصیوں کو در تمہارا\nعاصیوں کو در تمہارا"
        },
        {
            "id": 16,
            "title": "Hamd - Sagheer Ahmed Naqshbandi",
            "reciter": "Sagheer Ahmed Naqshbandi",
            "language": "Urdu",
            "duration": "7:25",
            "audio_url": "https://soundcloud.com/best-naats-collection/sagheer-ahmed-naqshbandi-hamd",
            "lyrics_excerpt": "اے میرے مالک و مولا\nتیرا شکر ہے تیرا شکر"
        },
        {
            "id": 17,
            "title": "Har Lehza Hai Momin",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "5:40",
            "audio_url": "https://soundcloud.com/best-naats-collection/har-lehza-hai-momin",
            "lyrics_excerpt": "ہر لحظہ ہے مومن تیری نظر کا طلبگار\nہر لحظہ ہے مومن تیری نظر کا طلبگار"
        },
        {
            "id": 18,
            "title": "Ya Shafi Al Wara Salam",
            "reciter": "Various",
            "language": "Arabic",
            "duration": "6:15",
            "audio_url": "https://soundcloud.com/best-naats-collection/ya-shafi-al-wara-salam-arabic",
            "lyrics_excerpt": "یا شافع الورا سلام\nیا شافع الورا سلام"
        },
        {
            "id": 19,
            "title": "Allah Hoo Allah Hoo",
            "reciter": "Various",
            "language": "Urdu/Arabic",
            "duration": "8:05",
            "audio_url": "https://soundcloud.com/best-naats-collection/allah-hoo-allah-hoo-dil-pawey",
            "lyrics_excerpt": "اللہ ہو اللہ ہو\nاللہ ہو اللہ ہو"
        },
        {
            "id": 20,
            "title": "Aaiyan Thandiyan Hawanwan",
            "reciter": "Various",
            "language": "Punjabi",
            "duration": "6:30",
            "audio_url": "https://soundcloud.com/best-naats-collection/aaiyan-thandiyan-hawanwan-made",
            "lyrics_excerpt": "آئیاں ٹھنڈیاں ہواواں\nمدینے دی چلیاں"
        },
        {
            "id": 21,
            "title": "Ae Rasool-e-Ameen",
            "reciter": "Syed Fasihuddin Soharwardi",
            "language": "Urdu",
            "duration": "7:15",
            "audio_url": "https://soundcloud.com/best-naats-collection/ae-rasool-e-ameen-by-syed",
            "lyrics_excerpt": "اے رسول امین\nتم پہ کروڑوں درود"
        },
        {
            "id": 22,
            "title": "Album 2010",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "6:45",
            "audio_url": "https://soundcloud.com/best-naats-collection/album-2010",
            "lyrics_excerpt": "محمد کا دم قدم ہے\nہر رنج و غم میں مرہم ہے"
        },
        {
            "id": 23,
            "title": "Mera Koi Nahi Hai Tere Siva",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "5:50",
            "audio_url": "https://soundcloud.com/best-naats-collection/mera-koi-nahi-hai-tere-siva",
            "lyrics_excerpt": "میرا کوئی نہیں ہے تیرے سوا\nمیرا کوئی نہیں ہے تیرے سوا"
        },
        {
            "id": 24,
            "title": "Har Haal Main Allah Hai",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "7:20",
            "audio_url": "https://soundcloud.com/best-naats-collection/har-haal-main-allah-hai-allah",
            "lyrics_excerpt": "ہر حال میں اللہ ہے\nاللہ ہر حال میں"
        },
        {
            "id": 25,
            "title": "Tu Raheem Wi Ae Tu Kareem",
            "reciter": "Various",
            "language": "Punjabi",
            "duration": "6:10",
            "audio_url": "https://soundcloud.com/best-naats-collection/tu-raheem-wi-ae-tu-kareem",
            "lyrics_excerpt": "تو رحیم وی اے تو کریم وی اے\nتو رحیم وی اے تو کریم وی اے"
        },
        {
            "id": 26,
            "title": "Darood Sharif",
            "reciter": "Sami Yousuf",
            "language": "Arabic",
            "duration": "4:35",
            "audio_url": "https://soundcloud.com/muneeb-farazz/darood-sharif-by-sami-yousuf",
            "lyrics_excerpt": "اللهم صل على محمد وعلى آل محمد كما صليت على إبراهيم وعلى آل إبراهيم"
        },
        {
            "id": 27,
            "title": "Amia Hi Amia",
            "reciter": "Various",
            "language": "Urdu",
            "duration": "5:20",
            "audio_url": "https://soundcloud.com/muneeb-farazz/amia-hi-amia",
            "lyrics_excerpt": "آمیا ہی آمیا\nآمیا ہی آمیا"
        },
        {
            "id": 28,
            "title": "Background Nasheed",
            "reciter": "Various",
            "language": "Arabic",
            "duration": "3:45",
            "audio_url": "https://soundcloud.com/islamiaudiolibrary/background-nasheed-no-19",
            "lyrics_excerpt": "سبحان الله، الحمد لله، الله أكبر"
        },
        {
            "id": 29,
            "title": "Main Banda E Aasi Hoon",
            "reciter": "Muhammad Ali Imran",
            "language": "Urdu",
            "duration": "6:25",
            "audio_url": "https://soundcloud.com/muhammad-ali-imran-451515811/main_banda_e_aasi_hoon",
            "lyrics_excerpt": "میں بندہ عاصی ہوں میرے مولا\nمیں بندہ عاصی ہوں میرے مولا"
        }
    ]

# Extended collection of duas
def get_duas():
    return [
        {
            "id": 1,
            "title": "Dua for Beginning a Meal",
            "arabic": "بِسْمِ اللهِ",
            "transliteration": "Bismillah",
            "translation": "In the name of Allah",
            "urdu": "اللہ کے نام سے",
            "reference": "Abu Dawud"
        },
        {
            "id": 2,
            "title": "Dua After Completing a Meal",
            "arabic": "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
            "transliteration": "Alhamdu lillahil-ladhi at'amani hadha, wa razaqanihi min ghayri hawlin minni wa la quwwatin",
            "translation": "Praise is to Allah Who has fed me this and provided it for me without any might or power on my part",
            "urdu": "تمام تعریفیں اللہ کے لیے ہیں جس نے مجھے یہ کھلایا اور بغیر میری طاقت اور قوت کے مجھے یہ رزق دیا",
            "reference": "Abu Dawud, Tirmidhi"
        },
        {
            "id": 3,
            "title": "Dua Before Entering the Bathroom",
            "arabic": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ",
            "transliteration": "Allahumma inni a'udhu bika minal-khubthi wal-khaba'ith",
            "translation": "O Allah, I seek refuge in You from the male and female unclean spirits",
            "urdu": "اے اللہ میں تیری پناہ چاہتا ہوں خبیث (شیطان) اور خبیثہ (شیطانی) سے",
            "reference": "Bukhari, Muslim"
        },
        {
            "id": 4,
            "title": "Dua When Leaving the Bathroom",
            "arabic": "غُفْرَانَكَ",
            "transliteration": "Ghufranaka",
            "translation": "I ask You (Allah) for forgiveness",
            "urdu": "میں آپ سے معافی مانگتا ہوں",
            "reference": "Abu Dawud, Tirmidhi, Ibn Majah"
        },
        {
            "id": 5,
            "title": "Dua When Waking Up",
            "arabic": "الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ",
            "transliteration": "Alhamdu lillahil-ladhi ahyana ba'da ma amatana, wa ilayhin-nushur",
            "translation": "Praise is to Allah Who gives us life after He has caused us to die and to Him is the return",
            "urdu": "تمام تعریف اللہ کے لیے ہے جس نے ہمیں زندگی دی اسکے بعد کہ ہمیں موت دی تھی اور اسی کی طرف پلٹنا ہے",
            "reference": "Bukhari"
        },
        {
            "id": 6,
            "title": "Dua Before Sleeping",
            "arabic": "بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا",
            "transliteration": "Bismika Allahumma amutu wa ahya",
            "translation": "In Your name, O Allah, I die and I live",
            "urdu": "اے اللہ، تیرے نام سے میں مرتا ہوں اور جیتا ہوں",
            "reference": "Bukhari"
        },
        {
            "id": 7,
            "title": "Dua for Protection",
            "arabic": "بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ",
            "transliteration": "Bismillahil-ladhi la yadurru ma'as-mihi shay'un fil-ardi wa la fis-sama'i, wa huwas-Sami'ul-'Alim",
            "translation": "In the name of Allah, with Whose name nothing can harm on earth or in the heaven, and He is the All-Hearing, the All-Knowing",
            "urdu": "اللہ کے نام سے جس کے نام کے ساتھ زمین اور آسمان میں کوئی چیز نقصان نہیں پہنچا سکتی اور وہ سننے والا، جاننے والا ہے",
            "reference": "Abu Dawud, Tirmidhi"
        },
        {
            "id": 8,
            "title": "Dua for Anxiety and Sorrow",
            "arabic": "اللَّهُمَّ إِنِّي عَبْدُكَ، ابْنُ عَبْدِكَ، ابْنُ أَمَتِكَ، نَاصِيَتِي بِيَدِكَ، مَاضٍ فِيَّ حُكْمُكَ، عَدْلٌ فِيَّ قَضَاؤُكَ، أَسْأَلُكَ بِكُلِّ اسْمٍ هُوَ لَكَ، سَمَّيْتَ بِهِ نَفْسَكَ، أَوْ أَنْزَلْتَهُ فِي كِتَابِكَ، أَوْ عَلَّمْتَهُ أَحَداً مِنْ خَلْقِكَ، أَوِ اسْتَأْثَرْتَ بِهِ فِي عِلْمِ الْغَيْبِ عِنْدَكَ، أَنْ تَجْعَلَ الْقُرْآنَ رَبِيعَ قَلْبِي، وَنُورَ صَدْرِي، وَجَلَاءَ حُزْنِي، وَذَهَابَ هَمِّي",
            "transliteration": "Allahumma inni 'abduka, ibnu 'abdika, ibnu amatika, nasiyati biyadika, madin fiyya hukmuka, 'adlun fiyya qada'uka, as'aluka bikulli ismin huwa laka, sammayta bihi nafsaka, aw anzaltahu fi kitabika, aw 'allamtahu ahadan min khalqika, aw ista'tharta bihi fi 'ilmil-ghaybi 'indaka, an taj'alal-Qur'ana rabi'a qalbi, wa nura sadri, wa jala'a huzni, wa dhahaba hammi",
            "translation": "O Allah, I am Your slave, the son of Your slave, the son of Your female slave. My forelock is in Your Hand. Your judgment over me is assured, and Your decreeing concerning me is just. I ask You by every name which is Yours, by which You named Yourself, or which You revealed in Your Book, or which You taught to any of Your creation, or which You have preserved in the knowledge of the unseen with You, that You make the Quran the spring of my heart, and the light of my chest, and the removal of my sadness, and the departure of my anxiety",
            "urdu": "اے اللہ! میں تیرا بندہ ہوں، تیرے بندے کا بیٹا، تیری بندی کا بیٹا۔ میری پیشانی تیرے ہاتھ میں ہے۔ میرے بارے میں تیرا فیصلہ جاری ہے، میرے بارے میں تیرا فیصلہ عدل ہے۔ میں تجھ سے تیرے ہر اس نام کے واسطے سے سوال کرتا ہوں جو تیرا ہے، جس سے تو نے اپنے آپ کو پکارا، یا جسے تو نے اپنی کتاب میں نازل کیا، یا جسے تو نے اپنی مخلوق میں سے کسی کو سکھایا، یا جسے تو نے اپنے پاس غیب کے علم میں رکھا ہے، کہ تو قرآن کو میرے دل کی بہار، میرے سینے کا نور، میرے غم کو دور کرنے والا اور میری پریشانی کو ختم کرنے والا بنا دے",
            "reference": "Ahmad"
        },
        {
            "id": 9,
            "title": "Dua for Entering the Mosque",
            "arabic": "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
            "transliteration": "Allahumma iftah li abwaba rahmatika",
            "translation": "O Allah, open for me the gates of Your mercy",
            "urdu": "اے اللہ میرے لیے اپنی رحمت کے دروازے کھول دے",
            "reference": "Muslim"
        },
        {
            "id": 10,
            "title": "Dua for Leaving the Mosque",
            "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
            "transliteration": "Allahumma inni as'aluka min fadlika",
            "translation": "O Allah, I ask You for Your bounty",
            "urdu": "اے اللہ میں تجھ سے تیرا فضل مانگتا ہوں",
            "reference": "Muslim"
        },
        {
            "id": 11,
            "title": "Dua for Seeking Knowledge",
            "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا، وَرِزْقًا طَيِّبًا، وَعَمَلًا مُتَقَبَّلًا",
            "transliteration": "Allahumma inni as'aluka 'ilman nafi'an, wa rizqan tayyiban, wa 'amalan mutaqabbalan",
            "translation": "O Allah, I ask You for knowledge that is beneficial, provision that is good, and deeds that are acceptable",
            "urdu": "اے اللہ! میں تجھ سے فائدہ مند علم، پاکیزہ رزق اور قبول عمل کا سوال کرتا ہوں",
            "reference": "Ibn Majah"
        },
        {
            "id": 12,
            "title": "Dua for Parents",
            "arabic": "رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
            "transliteration": "Rabbi irhamhuma kama rabbayani sagheera",
            "translation": "My Lord, have mercy upon them as they brought me up [when I was] small",
            "urdu": "اے میرے رب! ان پر رحم فرما جیسا کہ انہوں نے مجھے بچپن میں پالا",
            "reference": "Quran 17:24"
        },
        {
            "id": 13,
            "title": "Dua for Traveling",
            "arabic": "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ",
            "transliteration": "Subhanal-ladhi sakhkhara lana hadha wa ma kunna lahu muqrinin, wa inna ila Rabbina lamunqalibun",
            "translation": "Glorified is He Who has subjected this to us, and we could never have it (by our efforts). And verily, to Our Lord we indeed are to return!",
            "urdu": "پاک ہے وہ جس نے ہمارے لیے اس (سواری) کو مسخر کیا حالانکہ ہم اس کے قابو میں لانے والے نہ تھے اور یقیناً ہم اپنے رب کی طرف پلٹنے والے ہیں",
            "reference": "Quran 43:13-14"
        },
        {
            "id": 14,
            "title": "Dua for Returning from Travel",
            "arabic": "آيِبُونَ، تَائِبُونَ، عَابِدُونَ، لِرَبِّنَا حَامِدُونَ",
            "transliteration": "Ayibuna, ta'ibuna, 'abiduna, li-Rabbina hamidun",
            "translation": "We return, repent, worship and praise our Lord",
            "urdu": "ہم واپس آنے والے، توبہ کرنے والے، عبادت کرنے والے اور اپنے رب کی حمد کرنے والے ہیں",
            "reference": "Muslim"
        },
        {
            "id": 15,
            "title": "Dua for Rain",
            "arabic": "اللَّهُمَّ أَغِثْنَا، اللَّهُمَّ أَغِثْنَا، اللَّهُمَّ أَغِثْنَا",
            "transliteration": "Allahumma aghithna, Allahumma aghithna, Allahumma aghithna",
            "translation": "O Allah, send us rain. O Allah, send us rain. O Allah, send us rain",
            "urdu": "اے اللہ ہم پر بارش برسا، اے اللہ ہم پر بارش برسا، اے اللہ ہم پر بارش برسا",
            "reference": "Bukhari"
        }
    ]

# Expanded collection of Durood Shareef
def get_durood_shareef():
    return [
        {
            "id": 1,
            "title": "Durood Ibrahim",
           "arabic": "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ إِنَّكَ حَمِيدٌ مَجِيدٌ اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ إِنَّكَ حَمِيدٌ مَجِيدٌ",
            "transliteration": "Allahumma salli 'ala Muhammadin wa 'ala aali Muhammadin kama sallayta 'ala Ibrahima wa 'ala aali Ibrahima innaka Hamidum Majid. Allahumma barik 'ala Muhammadin wa 'ala aali Muhammadin kama barakta 'ala Ibrahima wa 'ala aali Ibrahima innaka Hamidum Majid",
            "translation": "O Allah, send prayers upon Muhammad and the followers of Muhammad, just as You sent prayers upon Ibrahim and upon the followers of Ibrahim. Verily, You are full of praise and majesty. O Allah, send blessings upon Muhammad and upon the family of Muhammad, just as You sent blessings upon Ibrahim and upon the family of Ibrahim. Verily, You are full of praise and majesty.",
            "urdu": "اے اللہ! درود بھیج محمد پر اور آل محمد پر جیسے تو نے درود بھیجا ابراہیم پر اور آل ابراہیم پر۔ بیشک تو تعریف والا بزرگی والا ہے۔ اے اللہ! برکت نازل فرما محمد پر اور آل محمد پر جیسے تو نے برکت نازل فرمائی ابراہیم پر اور آل ابراہیم پر۔ بیشک تو تعریف والا بزرگی والا ہے۔",
            "virtues": "This is the Durood that Muslims recite in their prayers (Salah). It is reported in numerous hadith that the Prophet Muhammad ﷺ taught this Durood to his companions when they asked how to send blessings upon him."
        },
        {
            "id": 2,
            "title": "Durood-e-Taj",
            "arabic": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ صَاحِبِ التَّاجِ وَالْمِعْرَاجِ وَالْبُرَاقِ وَالْعَلَمِ صَاحِبِ الْقَضِيبِ وَالنَّاقَةِ وَالْحَرَمِ صَاحِبِ الْحِلِّ وَالْحَرَمِ وَزَمْزَمَ وَالْعَلَمِ دَافِعِ الْبَلَاءِ وَالْوَبَاءِ وَالْقَحْطِ وَالْمَرَضِ وَالْأَلَمِ",
            "transliteration": "Allahumma salli 'ala sayyidina Muhammadin sahibit taji wal mi'raji wal buraqi wal 'alam, sahibil qadeebi wan naqati wal haram, sahibil hilli wal haram wa zamzam wal 'alam, dafi'il bala'i wal waba'i wal qahti wal maradi wal alam",
            "translation": "O Allah, send Your blessings upon our Master Muhammad, the possessor of the crown and the ascension and the buraq and the standard, the repeller of affliction and disease and drought and illness and pain.",
            "urdu": "اے اللہ! رحمت نازل فرما ہمارے سردار محمد پر، تاج اور معراج اور براق اور نشان والے، قضیب اور ناقہ اور حرم والے، حل اور حرم اور زمزم اور نشان والے، بلا اور وبا اور قحط اور مرض اور درد کو دفع کرنے والے پر۔",
            "virtues": "This Durood mentions many attributes and blessings of Prophet Muhammad ﷺ. It is highly regarded in the Sufi tradition and is said to bring relief from afflictions and difficulties."
        },
        {
            "id": 3,
            "title": "Durood-e-Tunajjina",
            "arabic": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ صَلَاةً تُنْجِينَا بِهَا مِنْ جَمِيعِ الْأَهْوَالِ وَالْآفَاتِ وَتَقْضِي لَنَا بِهَا جَمِيعَ الْحَاجَاتِ وَتُطَهِّرُنَا بِهَا مِنْ جَمِيعِ السَّيِّئَاتِ وَتَرْفَعُنَا بِهَا عِنْدَكَ أَعْلَى الدَّرَجَاتِ وَتُبَلِّغُنَا بِهَا أَقْصَى الْغَايَاتِ مِنْ جَمِيعِ الْخَيْرَاتِ فِي الْحَيَاةِ وَبَعْدَ الْمَمَاتِ",
            "transliteration": "Allahumma salli 'ala sayyidina Muhammadin salatan tunjina biha min jami'il ahwali wal afat, wa taqdi lana biha jami'al hajat, wa tutahhiruna biha min jami'is sayyi'at, wa tarfa'una biha 'indaka a'lad darajat, wa tuballighuna biha aqsal ghayat min jami'il khayrat fil hayati wa ba'dal mamat",
            "translation": "O Allah, bestow Your blessings upon our Master Muhammad, a blessing by which You deliver us from all anxieties and calamities, and satisfy all our needs, and cleanse us by it from all sins, and raise us by it to the highest degrees, and cause us to reach by it the furthest goals of all good in this life and after death.",
            "urdu": "اے اللہ! ہمارے سردار محمد پر ایسا درود بھیج جس کے ذریعے ہمیں تمام ہولناکیوں اور آفتوں سے نجات ملے اور ہماری تمام حاجتیں پوری ہوں اور ہمیں تمام گناہوں سے پاک کرے اور ہمیں تیرے ہاں اعلیٰ درجات تک پہنچائے اور ہمیں زندگی میں اور موت کے بعد تمام خیرات کی انتہا تک پہنچا دے۔",
            "virtues": "This Durood is known for seeking protection from calamities and fulfillment of needs. Many scholars mention that reciting this Durood regularly brings relief from difficulties and helps in attaining one's goals."
        },
        {
            "id": 4,
            "title": "Durood-e-Shafi",
            "arabic": "اَللّٰهُمَّ صَلِّ عَلٰى سَيِّدِنَا مُحَمَّدٍ طِبِّ الْقُلُوْبِ وَ دَوَآئِهَا وَ عَافِيَةِ الْاَبْدَانِ وَ شِفَآئِهَا وَ نُوْرِ الْاَبْصَارِ وَ ضِيَآئِهَا وَ عَلٰى اٰلِهٖ وَ صَحْبِهٖ وَ سَلِّمْ",
            "transliteration": "Allahumma salli 'ala sayyidina Muhammadin tibbil qulubi wa dawa'iha, wa 'afiyatil abdani wa shifa'iha, wa nuril absari wa diya'iha, wa 'ala alihi wa sahbihi wa sallim",
            "translation": "O Allah, bestow Your blessings upon our master Muhammad, the medicine for hearts and their cure, the good health of bodies and their healing, the light of eyes and their illumination, and upon his family and companions, and grant them peace.",
            "urdu": "اے اللہ! ہمارے سردار محمد پر درود بھیج، جو دلوں کی دوا اور شفا ہیں، جسموں کی عافیت اور شفا ہیں، آنکھوں کا نور اور روشنی ہیں، اور ان کی آل اور صحابہ پر، اور انہیں سلامتی عطا فرما۔",
            "virtues": "This Durood is especially beneficial for seeking cure from illnesses and diseases. Many people recite it for physical and spiritual healing."
        },
        {
            "id": 5,
            "title": "Durood-e-Nariya",
            "arabic": "اللَّهُمَّ صَلِّ صَلاَةً كَامِلَةً وَسَلِّمْ سَلاَمًا تَامًّا عَلَى سَيِّدِنَا مُحَمَّدٍ الَّذِي تَنْحَلُّ بِهِ الْعُقَدُ وَتَنْفَرِجُ بِهِ الْكُرَبُ وَتُقْضَى بِهِ الْحَوَائِجُ وَتُنَالُ بِهِ الرَّغَائِبُ وَحُسْنُ الْخَوَاتِمِ وَيُسْتَسْقَى الْغَمَامُ بِوَجْهِهِ الْكَرِيمِ وَعَلَى آلِهِ وَصَحْبِهِ فِي كُلِّ لَمْحَةٍ وَنَفَسٍ بِعَدَدِ كُلِّ مَعْلُومٍ لَكَ",
            "transliteration": "Allahumma salli salatan kamilatan wa sallim salaman tamman 'ala sayyidina Muhammadin alladhi tanhallu bihil 'uqadu wa tanfariju bihil kurabu wa tuqda bihil hawa'iju wa tunalu bihir ragha'ibu wa husnul khawatimi wa yustasqal ghamamu bi wajhihil karimi wa 'ala alihi wa sahbihi fi kulli lamhatin wa nafasin bi 'adadi kulli ma'lumin laka",
            "translation": "O Allah, convey complete blessings and perfect peace upon our Master Muhammad, by whom the knots are untied, by whom the difficulties are relieved, by whom the needs are fulfilled, by whom the desires are obtained, and (by whom) there are good endings, and by whose noble face the clouds are asked for rain, and upon his family and companions in every glance and breath, as many times as all that is known to You.",
            "urdu": "اے اللہ، ہمارے سردار محمد پر مکمل درود اور پورا سلام بھیج، جن کے وسیلے سے گرہیں کھلتی ہیں، مشکلات دور ہوتی ہیں، حاجتیں پوری ہوتی ہیں، خواہشیں حاصل ہوتی ہیں، اور حسن خاتمہ ہوتا ہے، اور جن کے کریم چہرے کے واسطے سے بادلوں سے بارش طلب کی جاتی ہے، اور ان کی آل اور صحابہ پر ہر لمحے اور سانس میں، اس تعداد میں جو تمہارے علم میں ہے۔",
            "virtues": "This Durood is particularly powerful for solving difficult problems and fulfilling important needs. Many have experienced its blessings in times of hardship."
        },
        {
            "id": 6,
            "title": "Durood-e-Qadri",
            "arabic": "اَللّٰهُمَّ صَلِّ عَلٰى حَبِيْبِكَ سَيِّدِنَا مُحَمَّدِنِ الْمُصْطَفٰى وَ عَلٰى اٰلِهٖ وَ اَصْحَابِهٖ وَ بَارِكْ وَ سَلِّمْ عَدَدَ مَا فِيْ عِلْمِ اللّٰهِ صَلَاةً دَائِمَةً بِدَوَامِ مُلْكِ اللّٰهِ",
            "transliteration": "Allahumma salli 'ala habibika sayyidina Muhammadini-l-Mustafa wa 'ala alihi wa ashabihi wa barik wa sallim 'adada ma fi 'ilmillahi salatan da'imatan bi dawami mulkillah",
            "translation": "O Allah, send blessings upon Your beloved, our Master Muhammad, the Chosen One, and upon his family and companions, and bestow blessings and peace (upon them) as many as the knowledge of Allah, with blessings lasting as long as the kingdom of Allah.",
            "urdu": "اے اللہ، اپنے محبوب، ہمارے سردار محمد مصطفی، اور ان کی آل اور اصحاب پر درود بھیج، اور برکت اور سلامتی نازل فرما، اس تعداد میں جو اللہ کے علم میں ہے، ایسا درود جو اللہ کی بادشاہی کی دوام کے ساتھ دائم رہے۔",
            "virtues": "This Durood is associated with Shaykh Abdul Qadir Jilani and is recited by many in the Qadri Sufi order. It is said to bring great spiritual elevation."
        },
        {
            "id": 7,
            "title": "Salawat-e-Fatih",
            "arabic": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ الْفَاتِحِ لِمَا أُغْلِقَ وَالْخَاتِمِ لِمَا سَبَقَ نَاصِرِ الْحَقِّ بِالْحَقِّ وَالْهَادِي إِلَى صِرَاطِكَ الْمُسْتَقِيمِ وَعَلَى آلِهِ حَقَّ قَدْرِهِ وَمِقْدَارِهِ الْعَظِيمِ",
            "transliteration": "Allahumma salli 'ala sayyidina Muhammadin-il-fatihi lima ughliqa wal-khatimi lima sabaqa nasir-il-haqqi bil-haqqi wal-hadi ila siratik-al-mustaqim wa 'ala alihi haqqa qadrihi wa miqdarihi-il-'azim",
            "translation": "O Allah, send blessings upon our Master Muhammad, the opener of what was closed, and the seal of what had preceded, the helper of the Truth by the Truth, the guide to Your straight path, and upon his family, according to his great rank and grandeur.",
            "urdu": "اے اللہ! ہمارے سردار محمد پر درود بھیج، جو بند کی ہوئی چیزوں کو کھولنے والے، پچھلی چیزوں پر مہر لگانے والے، حق کے ساتھ حق کی مدد کرنے والے، تیرے سیدھے راستے کی طرف راہنمائی کرنے والے، اور ان کی آل پر، ان کے عظیم مرتبے اور مقدار کے مطابق۔",
            "virtues": "This Durood is widely recited in the Tijaniyya Sufi order. Shaykh Ahmad Tijani said that this Durood has immense spiritual benefits and rewards."
        }
    ]

def get_quran_audio_list():
    # List of reciters and their editions in the Quran API with Pakistani translations
    return [
        {"id": "ar.alafasy", "name": "Mishary Rashid Alafasy", "language": "Arabic"},
        {"id": "ar.abdulbasitmurattal", "name": "Abdul Basit Murattal", "language": "Arabic"},
        {"id": "ar.abdurrahmaansudais", "name": "Abdurrahmaan As-Sudais", "language": "Arabic"},
        {"id": "ar.mahermuaiqly", "name": "Maher Al Muaiqly", "language": "Arabic"},
        {"id": "ur.khanabubakar", "name": "Moulana Abu Bakr Chisti (Urdu)", "language": "Urdu"},
        {"id": "ur.muhammajunagarhvi", "name": "Muhammad Junagarhvi (Urdu)", "language": "Urdu"},
        {"id": "ur.muhammajunagarhvi", "name": "Muhammad Junagarhvi (Urdu)", "language": "Urdu"},
        {"id": "ur.khanzakariyya", "name": "Khan Zakariyya (Urdu)", "language": "Urdu"},
        {"id": "ur.maulanamahmudhasan", "name": "Maulana Mahmud Hasan (Urdu)", "language": "Urdu"},
        {"id": "ur.rashidmehmoodridai", "name": "Rashid Mehmood Ridai (Urdu)", "language": "Urdu"}
    ]

# Function to add YouTube live naats iframe
def add_youtube_live():
    st.markdown("<h3>Live Naats Streaming</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
            <iframe 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
                src="https://www.youtube.com/embed/8NUOU1UG5Zg?si=elnVqN-zxqKGPYfX'    
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                referrerpolicy="strict-origin-when-cross-origin" 
                allowfullscreen>
            </iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown("<h1 class='main-header'>Islamic Resources Hub</h1>", unsafe_allow_html=True)

# Get user's location for auto-detection features
user_location = get_user_location()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📚 Juz Browser",
        "🎧 Listen to Quran",
        "🕋 Prayer Times",
        "🤲 Duas Collection",
        "📿 Durood Shareef",
        "🎵 Naats Collection",
        "📋 Asma Al-Husna",
        "📒 Names of Muhammad ﷺ"
    ]
)

# Developer info
with st.sidebar.expander("About Developer"):
    st.markdown("""
    <div class="info-box">
        <h3 style="margin-top:0">Developed by: Riaz Hussain Saifi</h3>
        <p>This application provides a comprehensive collection of Islamic resources including Quran browsing, 
        prayer times, Naats, Duas, and more.</p>
        <p>For more information or custom development, please contact the developer.</p>
        <p><a href="https://www.linkedin.com/in/riaz-hussain-saifi" target="_blank">Connect on LinkedIn</a></p>
    </div>
    """, unsafe_allow_html=True)

# Page content based on navigation
if page == "🏠 Home":
    # Hero section with animation effects
    st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Explore Islamic Resources</h1>
    <p class="hero-subtitle">Your comprehensive platform for Quran, Prayer Times, Naats, Duas, and more</p>
    <div>
        <a href="#" onclick="document.querySelectorAll('[data-testid=\'stSidebar\'] [role=\'radio\']')[1].click(); return false;" class="hero-button">Browse Quran</a>
        <a href="#" onclick="document.querySelectorAll('[data-testid=\'stSidebar\'] [role=\'radio\']')[6].click(); return false;" class="hero-button">Listen to Naats</a>
    </div>
</div>
""", unsafe_allow_html=True)
    
    # Dashboard layout
    st.markdown("<h2 class='section-header'>Welcome to Islamic Resources Hub</h2>", unsafe_allow_html=True)
    
    # Create three columns for the dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">📚 Quran</h3>
            <p>Access the Holy Quran in multiple languages and translations.</p>
            <ul>
                <li>Browse by Juz (Para)</li>
                <li>Multiple translations including Urdu</li>
                <li>Listen to beautiful recitations</li>
                <li>Read complete surahs and juz</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">🕋 Prayer Times</h3>
            <p>Get accurate prayer times for your location with multiple calculation methods.</p>
            <ul>
                <li>Automatic location detection</li>
                <li>Multiple calculation methods</li>
                <li>Daily prayer schedule</li>
                <li>Visual prayer timeline</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">🎵 Naats Collection</h3>
            <p>Listen to beautiful Naats in praise of Prophet Muhammad ﷺ.</p>
            <ul>
                <li>Various renowned reciters</li>
                <li>Different languages</li>
                <li>High-quality audio</li>
                <li>Lyrics in Urdu and English</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">📿 Durood Shareef</h3>
            <p>Collection of Durood Shareef with Arabic text, transliteration, and translation.</p>
            <ul>
                <li>Multiple Durood variants</li>
                <li>Virtues and benefits</li>
                <li>Urdu translation</li>
                <li>Daily counter for tracking recitations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">🤲 Duas Collection</h3>
            <p>Comprehensive collection of daily duas with translations and references.</p>
            <ul>
                <li>Categorized duas</li>
                <li>Arabic with Urdu translation</li>
                <li>Source references</li>
                <li>Searchable database</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3 style="color: #046307;">📋 Divine Names</h3>
            <p>The 99 Names of Allah and Names of Prophet Muhammad ﷺ.</p>
            <ul>
                <li>Complete numbered lists</li>
                <li>Arabic text with meanings</li>
                <li>Detailed explanations</li>
                <li>Multiple view options</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Current date and prayer time info
    st.markdown("<h2 class='section-header'>Today's Overview</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Current date and prayer times based on user's location
        loading_animation()
        prayer_data = get_prayer_times(user_location['city'], user_location['country'])
        
        if prayer_data:
            st.markdown("""
            <div class="info-box">
                <h3 style="margin-top:0">Prayer Times for {}</h3>
                <p><strong>Fajr:</strong> <span class="prayer-time">{}</span></p>
                <p><strong>Sunrise:</strong> <span class="prayer-time">{}</span></p>
                <p><strong>Dhuhr:</strong> <span class="prayer-time">{}</span></p>
                <p><strong>Asr:</strong> <span class="prayer-time">{}</span></p>
                <p><strong>Maghrib:</strong> <span class="prayer-time">{}</span></p>
                <p><strong>Isha:</strong> <span class="prayer-time">{}</span></p>
            </div>
            """.format(
                user_location['city'],
                prayer_data['timings']['Fajr'],
                prayer_data['timings']['Sunrise'],
                prayer_data['timings']['Dhuhr'],
                prayer_data['timings']['Asr'],
                prayer_data['timings']['Maghrib'],
                prayer_data['timings']['Isha']
            ), unsafe_allow_html=True)
    
    with col2:
        # Quick Dua of the day - randomly pick one
        duas = get_duas()
        dua_of_the_day = random.choice(duas)
        
        st.markdown(f"""
        <div class="info-box">
            <h3 style="margin-top:0">Dua of the Day</h3>
            <h4>{dua_of_the_day['title']}</h4>
            <div class="arabic-text">{dua_of_the_day['arabic']}</div>
            <div class="urdu-text">{dua_of_the_day['urdu']}</div>
            <p><strong>Transliteration:</strong> {dua_of_the_day['transliteration']}</p>
            <p><strong>Translation:</strong> {dua_of_the_day['translation']}</p>
            <p><strong>Reference:</strong> {dua_of_the_day['reference']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Featured Naat
    st.markdown("<h2 class='section-header'>Featured Naat</h2>", unsafe_allow_html=True)
    
    # Get a random naat from the collection
    naats = get_naats()
    featured_naat = random.choice(naats)
    
    st.markdown(f"""
    <div class="naat-card">
        <h3 class="naat-title">{featured_naat['title']}</h3>
        <p class="naat-reciter">Recited by: {featured_naat['reciter']} | Language: {featured_naat['language']} | Duration: {featured_naat['duration']}</p>
        <div class="urdu-text" style="background-color: #f5f5f5; margin-bottom: 15px;">{featured_naat['lyrics_excerpt']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Embed SoundCloud player for the featured naat
    st.components.v1.iframe(
        src=f"https://w.soundcloud.com/player/?url={featured_naat['audio_url']}&color=%23046307&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false",
        height=120,
        scrolling=False
    )
    
    # Add live YouTube naats
    add_youtube_live()
    
    # Featured Ayah
    st.markdown("<h2 class='section-header'>Verse of the Day</h2>", unsafe_allow_html=True)
    
    # Generate a random ayah number
    random_ayah_num = random.randint(1, 6236)
    
    # Get the ayah in Arabic and English
    try:
        loading_animation()
        ayah_arabic = get_ayah(random_ayah_num, "quran-uthmani")
        ayah_english = get_ayah(random_ayah_num, "en.asad")
        ayah_urdu = get_ayah(random_ayah_num, "ur.jalandhry")
        
        if ayah_arabic and ayah_english and ayah_urdu:
            st.markdown(f"""
            <div class="card">
                <h4>Surah {ayah_arabic['surah']['englishName']} ({ayah_arabic['surah']['number']}), Verse {ayah_arabic['numberInSurah']}</h4>
                <div class="arabic-text">{ayah_arabic['text']}</div>
                <div class="urdu-text">{ayah_urdu['text']}</div>
                <div class="translation-text">{ayah_english['text']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback to a well-known verse if API fails
            st.markdown("""
            <div class="card">
                <h4>Surah Al-Fatiha (1), Verse 1-7</h4>
                <div class="arabic-text">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ﴿١﴾ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ﴿٢﴾ الرَّحْمَٰنِ الرَّحِيمِ ﴿٣﴾ مَالِكِ يَوْمِ الدِّينِ ﴿٤﴾ إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ ﴿٥﴾ اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ ﴿٦﴾ صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ ﴿٧﴾</div>
                <div class="urdu-text">اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے ﴿١﴾ تمام تعریفیں اللہ کے لیے ہیں جو تمام جہانوں کا پالنے والا ہے ﴿٢﴾ بڑا مہربان نہایت رحم والا ﴿٣﴾ انصاف کے دن کا مالک ﴿٤﴾ ہم صرف تیری ہی عبادت کرتے ہیں اور صرف تجھی سے مدد مانگتے ہیں ﴿٥﴾ ہمیں سیدھے راستے کی ہدایت دے ﴿٦﴾ ان لوگوں کے راستے کی جن پر تو نے انعام کیا، نہ ان کی جن پر غضب ہوا اور نہ گمراہوں کی ﴿٧﴾</div>
                <div class="translation-text">In the name of Allah, the Entirely Merciful, the Especially Merciful. All praise is due to Allah, Lord of the worlds - The Entirely Merciful, the Especially Merciful, Sovereign of the Day of Recompense. It is You we worship and You we ask for help. Guide us to the straight path - The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.</div>
            </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error fetching verse of the day: {e}")
        # Fallback to a well-known verse
        st.markdown("""
        <div class="card">
            <h4>Surah Al-Fatiha (1), Verse 1-7</h4>
            <div class="arabic-text">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ﴿١﴾ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ﴿٢﴾ الرَّحْمَٰنِ الرَّحِيمِ ﴿٣﴾ مَالِكِ يَوْمِ الدِّينِ ﴿٤﴾ إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ ﴿٥﴾ اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ ﴿٦﴾ صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ ﴿٧﴾</div>
            <div class="urdu-text">اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے ﴿١﴾ تمام تعریفیں اللہ کے لیے ہیں جو تمام جہانوں کا پالنے والا ہے ﴿٢﴾ بڑا مہربان نہایت رحم والا ﴿٣﴾ انصاف کے دن کا مالک ﴿٤﴾ ہم صرف تیری ہی عبادت کرتے ہیں اور صرف تجھی سے مدد مانگتے ہیں ﴿٥﴾ ہمیں سیدھے راستے کی ہدایت دے ﴿٦﴾ ان لوگوں کے راستے کی جن پر تو نے انعام کیا، نہ ان کی جن پر غضب ہوا اور نہ گمراہوں کی ﴿٧﴾</div>
            <div class="translation-text">In the name of Allah, the Entirely Merciful, the Especially Merciful. All praise is due to Allah, Lord of the worlds - The Entirely Merciful, the Especially Merciful, Sovereign of the Day of Recompense. It is You we worship and You we ask for help. Guide us to the straight path - The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.</div>
        </div>
        """, unsafe_allow_html=True)

elif page == "📚 Juz Browser":
    st.markdown("<h2 class='section-header'>Juz Browser</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>The Holy Quran is divided into 30 Juz (parts) of approximately equal length. This makes it easier to read the Quran over the course of a month, particularly during Ramadan.</p>
        <p>Each Juz contains portions of different Surahs, and the division helps in systematic reading and memorization of the Quran.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a grid for Juz selection with beautiful cards and animations
    st.markdown("<h3>Select a Juz to Read</h3>", unsafe_allow_html=True)
    
    # Create columns for the grid with animation effect
    cols = 5
    rows = 6
    
    for i in range(rows):
        row_cols = st.columns(cols)
        for j in range(cols):
            juz_number = i * cols + j + 1
            if juz_number <= 30:
                with row_cols[j]:
                    st.markdown(f"""
                    <div class="name-card" style="text-align: center; cursor: pointer; min-height: 80px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <h3 style="margin: 0; color: #046307;">Juz {juz_number}</h3>
                        <p style="margin: 5px 0 0 0; font-size: 0.8rem;">Para {juz_number}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Read Juz {juz_number}", key=f"juz_{juz_number}", use_container_width=True):
                        st.session_state.selected_juz = juz_number
    
    # Display selected juz
    if 'selected_juz' in st.session_state:
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Get editions for display
        loading_animation()
        editions = get_quran_editions()
        text_editions = [edition for edition in editions if edition.get("format") == "text"]
        audio_editions = [edition for edition in editions if edition.get("format") == "audio"]
        
        # Create options for dropdown
        edition_options = []
        for edition in text_editions:
            edition_options.append({
                "label": f"{edition.get('name')} ({edition.get('language')})",
                "value": edition.get('identifier')
            })
        
        audio_options = []
        for edition in audio_editions:
            audio_options.append({
                "label": f"{edition.get('name')} ({edition.get('language')})",
                "value": edition.get('identifier')
            })
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"<h3>Selected Juz: {st.session_state.selected_juz}</h3>", unsafe_allow_html=True)
        
        with col2:
            # Default to Urdu translation if available
            default_index = 0
            for i, opt in enumerate(edition_options):
                if "ur." in opt["value"]:
                    default_index = i
                    break
            
            selected_edition = st.selectbox(
                "Select Translation",
                options=[opt["value"] for opt in edition_options],
                format_func=lambda x: next((opt["label"] for opt in edition_options if opt["value"] == x), x),
                index=default_index
            )
        
        with col3:
            if audio_options:
                selected_audio = st.selectbox(
                    "Select Audio Recitation",
                    options=[opt["value"] for opt in audio_options],
                    format_func=lambda x: next((opt["label"] for opt in audio_options if opt["value"] == x), x),
                    index=0
                )
            else:
                selected_audio = None
                st.info("Audio recitations not available")
        
        # Get the juz content
        loading_animation()
        juz_data = get_juz(st.session_state.selected_juz, selected_edition)
        arabic_juz = get_juz(st.session_state.selected_juz, "quran-uthmani")
        
        if juz_data and arabic_juz:
            # Display juz information
            st.markdown(f"""
            <div class="info-box">
                <h3 style="margin-top:0">Juz {st.session_state.selected_juz} (Para {st.session_state.selected_juz})</h3>
                <p><strong>Number of Verses:</strong> {len(juz_data.get('ayahs', []))}</p>
                <p><strong>Surahs Included:</strong> {", ".join(set([f"{ayah['surah']['englishName']} ({ayah['surah']['number']})" for ayah in juz_data.get('ayahs', [])]))}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # View mode selection with nice toggle animation
            view_mode = st.radio("View Mode", ["By Surah", "All Verses"], horizontal=True)
            
            if view_mode == "By Surah":
                # Group ayahs by surah
                surahs_in_juz = {}
                for ayah in juz_data.get('ayahs', []):
                    surah_num = ayah['surah']['number']
                    if surah_num not in surahs_in_juz:
                        surahs_in_juz[surah_num] = {
                            'name': ayah['surah']['englishName'],
                            'translation': ayah['surah']['englishNameTranslation'],
                            'ayahs': []
                        }
                    surahs_in_juz[surah_num]['ayahs'].append(ayah)
                
                # Display each surah in an expander with animations
                for surah_num in sorted(surahs_in_juz.keys()):
                    with st.expander(f"Surah {surah_num}: {surahs_in_juz[surah_num]['name']} ({surahs_in_juz[surah_num]['translation']})"):
                        # Get Arabic ayahs for this surah
                        arabic_ayahs = [ayah for ayah in arabic_juz.get('ayahs', []) if ayah['surah']['number'] == surah_num]
                        
                        # Display Bismillah if not Surah 9
                        if surah_num != 9:
                            st.markdown('<div class="arabic-text">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>', unsafe_allow_html=True)
                        
                        # Create tabs for different view options
                        tab1, tab2 = st.tabs(["Verse by Verse", "Complete Text"])
                        
                        with tab1:
                            # Display verses with Arabic and translation
                            for ayah, ar_ayah in zip(surahs_in_juz[surah_num]['ayahs'], arabic_ayahs):
                                st.markdown(f"""
                                <div class="card" style="animation: fadeIn 0.5s ease-in-out;">
                                    <div class="arabic-text">{ar_ayah['text']} ﴿{ayah['numberInSurah']}﴾</div>
                                    <div class="translation-text">{ayah['text']} ({ayah['numberInSurah']})</div>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        with tab2:
                            # Display all Arabic text together
                            st.markdown('<div class="arabic-text">', unsafe_allow_html=True)
                            for ar_ayah in arabic_ayahs:
                                st.markdown(f"{ar_ayah['text']} ﴿{ar_ayah['numberInSurah']}﴾ ", unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Display all translation text together
                            st.markdown('<div class="translation-text">', unsafe_allow_html=True)
                            for ayah in surahs_in_juz[surah_num]['ayahs']:
                                st.markdown(f"{ayah['text']} ({ayah['numberInSurah']}) ", unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Audio for surah sections in juz
                        if selected_audio:
                            try:
                                # Get the surah number and extract first ayah of this surah in this juz
                                surah_number = surah_num
                                st.markdown("<h4>Listen to this Surah section:</h4>", unsafe_allow_html=True)
                                st.audio(f"https://cdn.islamic.network/quran/audio/128/{selected_audio}/{surah_number}.mp3", format="audio/mp3")
                            except:
                                st.error("Audio not available for this section")
            else:
                # Display all verses sequentially
                current_surah = None
                
                for ayah, ar_ayah in zip(juz_data.get('ayahs', []), arabic_juz.get('ayahs', [])):
                    # Display surah header when surah changes
                    if current_surah != ayah['surah']['number']:
                        current_surah = ayah['surah']['number']
                        st.markdown(f"""
                        <h4 style="margin-top: 20px; color: #046307; animation: fadeIn 0.8s ease-in-out;">Surah {current_surah}: {ayah['surah']['englishName']} ({ayah['surah']['englishNameTranslation']})</h4>
                        """, unsafe_allow_html=True)
                        
                        # Display Bismillah if not Surah 9
                        if current_surah != 9:
                            st.markdown('<div class="arabic-text">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>', unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="card" style="animation: fadeIn 0.5s ease-in-out;">
                        <div class="arabic-text">{ar_ayah['text']} ﴿{ayah['numberInSurah']}﴾</div>
                        <div class="translation-text">{ayah['text']} ({ayah['numberInSurah']})</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Audio for entire juz
                if selected_audio:
                    st.warning("Full Juz audio is not available in single audio. Please use 'By Surah' view for audio recitation.")
        else:
            st.error("Error loading Juz data. Please try a different Juz or edition.")

elif page == "🎧 Listen to Quran":
    st.markdown("<h2 class='section-header'>Listen to Quran</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>Listen to beautiful recitations of the Holy Quran by renowned reciters. Select a Surah and reciter to begin listening.</p>
        <p>The audio is streamed directly from Islamic Network's CDN and is available in high quality.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get list of Surahs and reciters
    loading_animation()
    surahs = get_quran_surahs()
    reciters = get_quran_audio_list()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Select Surah
        surah_options = []
        for surah in surahs:
            surah_options.append({
                "label": f"{surah.get('number')}. {surah.get('englishName')} ({surah.get('englishNameTranslation')})",
                "value": surah.get('number')
            })
        
        selected_surah = st.selectbox(
            "Select Surah",
            options=[opt["value"] for opt in surah_options],
            format_func=lambda x: next((opt["label"] for opt in surah_options if opt["value"] == x), x),
            index=0
        )
    
    with col2:
        # Select Reciter
        reciter_options = []
        for reciter in reciters:
            reciter_options.append({
                "label": f"{reciter.get('name')} ({reciter.get('language')})",
                "value": reciter.get('id')
            })
        
        selected_reciter = st.selectbox(
            "Select Reciter",
            options=[opt["value"] for opt in reciter_options],
            format_func=lambda x: next((opt["label"] for opt in reciter_options if opt["value"] == x), x),
            index=0
        )
    
    # Get audio URL
    audio_url = f"https://cdn.islamic.network/quran/audio-surah/128/{selected_reciter}/{selected_surah}.mp3"
    
    # Display surah info
    if selected_surah:
        surah_info = next((s for s in surahs if s["number"] == selected_surah), None)
        if surah_info:
            st.markdown(f"""
            <div class="card" style="margin-top: 20px;">
                <h3 style="color: #046307;">{surah_info['englishName']} ({surah_info['englishNameTranslation']})</h3>
                <p><strong>Number of Verses:</strong> {surah_info['numberOfAyahs']}</p>
                <p><strong>Revelation Type:</strong> {surah_info['revelationType']}</p>
                <p>Now playing Surah {surah_info['number']} - {surah_info['englishName']} recited by {next((r['name'] for r in reciters if r['id'] == selected_reciter), 'Unknown Reciter')}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Audio player with enhanced styling
    st.markdown("""
    <h3 style="margin-top: 20px;">Audio Player</h3>
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 10px 0 20px 0;">
    """, unsafe_allow_html=True)
    
    # Audio player
    st.audio(audio_url, format="audio/mp3")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Display Bismillah and first few verses
    loading_animation()
    arabic_surah = get_surah(selected_surah, "quran-uthmani")
    translation_surah = get_surah(selected_surah, "en.asad")
    
    if arabic_surah and translation_surah:
        # Display Bismillah if not Surah 9
        if selected_surah != 9:
            st.markdown('<div class="arabic-text">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>', unsafe_allow_html=True)
        
        # Display first 5 verses or all if less than 5
        num_verses = min(5, len(arabic_surah['ayahs']))
        
        st.markdown("<h3>First Few Verses:</h3>", unsafe_allow_html=True)
        
        for i in range(num_verses):
            ar_ayah = arabic_surah['ayahs'][i]
            tr_ayah = translation_surah['ayahs'][i]
            
            st.markdown(f"""
            <div class="card" style="animation: fadeIn 0.5s ease-in-out;">
                <div class="arabic-text">{ar_ayah['text']} ﴿{ar_ayah['numberInSurah']}﴾</div>
                <div class="translation-text">{tr_ayah['text']} ({tr_ayah['numberInSurah']})</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Link to read full surah
        if st.button("Read Full Surah in Juz Browser", use_container_width=True):
            # Find which juz contains this surah
            juz_number = arabic_surah['ayahs'][0]['juz']
            st.session_state.selected_juz = juz_number
            st.session_state.page = "📚 Juz Browser"
            st.rerun()
    else:
        st.error("Error loading Surah text.")
    
    # Recommendations
    st.markdown("<h3>Recommended Surahs for Recitation:</h3>", unsafe_allow_html=True)
    
    # Create a row of recommended surahs
    recommended = [1, 36, 55, 56, 67, 78, 112, 113, 114]  # Common surahs for recitation
    cols = st.columns(len(recommended))
    
    for i, col in enumerate(cols):
        surah_num = recommended[i]
        surah_info = next((s for s in surahs if s["number"] == surah_num), None)
        
        if surah_info:
            with col:
                st.markdown(f"""
                <div class="name-card" style="text-align: center; min-height: 100px; cursor: pointer;">
                    <h4 style="margin: 0; color: #046307;">{surah_info['englishName']}</h4>
                    <p style="font-size: 0.8rem; margin: 5px 0;">Surah {surah_info['number']}</p>
                    <p style="font-size: 0.7rem;">{surah_info['englishNameTranslation']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Listen", key=f"rec_{surah_num}", use_container_width=True):
                    # Redirect to this page with different surah selected
                    st.session_state.recommended_surah = surah_num
                    st.rerun()
    
    # Apply recommendation if selected
    if 'recommended_surah' in st.session_state:
        selected_surah = st.session_state.recommended_surah
        del st.session_state.recommended_surah
        st.rerun()

elif page == "🕋 Prayer Times":
    st.markdown("<h2 class='section-header'>Prayer Times</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>Get accurate prayer times for your location. The prayer times are calculated based on your location and the selected calculation method.</p>
        <p>Prayer times may vary based on geographical location and calculation methodology. Always verify with your local mosque if in doubt.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Option to use current location
    use_current_location = st.checkbox("Use my current location", value=True)
    
    if use_current_location:
        city = user_location['city']
        country = user_location['country']
        st.info(f"Using detected location: {city}, {country}")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            city = st.text_input("City", "Islamabad")
        
        with col2:
            country = st.text_input("Country (name or 2-letter code)", "Pakistan")
    
    method = st.selectbox(
        "Calculation Method",
        options=[
            (0, "Shia Ithna-Ashari"),
            (1, "University of Islamic Sciences, Karachi"),
            (2, "Islamic Society of North America"),
            (3, "Muslim World League"),
            (4, "Umm Al-Qura University, Makkah"),
            (5, "Egyptian General Authority of Survey"),
            (7, "Institute of Geophysics, University of Tehran"),
            (8, "Gulf Region"),
            (9, "Kuwait")
        ],
        format_func=lambda x: x[1],
        index=3
    )[0]
    
    if st.button("Get Prayer Times", use_container_width=True, type="primary"):
        if city and country:
            loading_animation()
            prayer_data = get_prayer_times(city, country, method)
            
            if prayer_data:
                # Display current date information
                st.markdown(f"""
                <div class="info-box" style="animation: fadeIn 0.8s ease-in-out;">
                    <h3 style="margin-top:0">Date Information</h3>
                    <p><strong>Gregorian:</strong> {prayer_data['date']['gregorian']['date']}</p>
                    <p><strong>Hijri:</strong> {prayer_data['date']['hijri']['date']}</p>
                    <p><strong>Day:</strong> {prayer_data['date']['gregorian']['weekday']['en']} / {prayer_data['date']['hijri']['weekday']['en']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display prayer times
                st.markdown("<h3>Prayer Times</h3>", unsafe_allow_html=True)
                
                # Create a visual timeline of prayer times
                timings = prayer_data['timings']
                
                # Convert prayer times to datetime objects for visualization
                time_format = "%H:%M"
                prayer_times = {}
                for prayer, time_str in [
                    ("Fajr", timings['Fajr'].split()[0]),
                    ("Sunrise", timings['Sunrise'].split()[0]),
                    ("Dhuhr", timings['Dhuhr'].split()[0]),
                    ("Asr", timings['Asr'].split()[0]),
                    ("Maghrib", timings['Maghrib'].split()[0]),
                    ("Isha", timings['Isha'].split()[0])
                ]:
                    try:
                        prayer_times[prayer] = datetime.strptime(time_str, time_format)
                    except:
                        prayer_times[prayer] = datetime.now().replace(
                            hour=int(time_str.split(':')[0]), 
                            minute=int(time_str.split(':')[1]), 
                            second=0, microsecond=0
                        )
                
                # Create a DataFrame for the timeline
                prayer_df = pd.DataFrame({
                    'Prayer': list(prayer_times.keys()),
                    'Time': [t.strftime('%H:%M') for t in prayer_times.values()],
                    'Hour': [t.hour + t.minute/60 for t in prayer_times.values()],
                    'Color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
                })
                
                # Create a horizontal timeline
                fig = px.timeline(
                    prayer_df, 
                    x_start="Hour", 
                    x_end=[h+1 for h in prayer_df['Hour']], 
                    y="Prayer",
                    color="Prayer",
                    labels={"Hour": "Time of Day"},
                    color_discrete_sequence=prayer_df['Color'],
                    title="Daily Prayer Timeline"
                )
                
                # Customize layout
                fig.update_layout(
                    xaxis=dict(
                        title="Time of Day",
                        tickvals=list(range(0, 24, 2)),
                        ticktext=[f"{h:02d}:00" for h in range(0, 24, 2)],
                        range=[4, 22]  # Focus on daylight hours
                    ),
                    yaxis=dict(
                        title=""
                    ),
                    height=250
                )
                
                # Show current time marker
                now = datetime.now()
                current_hour = now.hour + now.minute/60
                
                fig.add_shape(
                    type="line",
                    x0=current_hour,
                    y0=-0.5,
                    x1=current_hour,
                    y1=len(prayer_df)-0.5,
                    line=dict(color="red", width=2, dash="dash")
                )
                
                fig.add_annotation(
                    x=current_hour,
                    y=len(prayer_df)-0.5,
                    text="Current Time",
                    showarrow=True,
                    arrowhead=1,
                    ax=0,
                    ay=-30
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Display prayer times in a card layout with animations
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("""
                    <div class="card" style="animation: fadeIn 0.8s ease-in-out;">
                        <h4 style="margin-top:0">Morning Prayers</h4>
                        <p><strong>Fajr:</strong> <span class="prayer-time">{}</span></p>
                        <p><strong>Sunrise:</strong> <span class="prayer-time">{}</span></p>
                        <p><strong>Dhuhr:</strong> <span class="prayer-time">{}</span></p>
                    </div>
                    """.format(timings['Fajr'], timings['Sunrise'], timings['Dhuhr']), unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="card" style="animation: fadeIn 1s ease-in-out;">
                        <h4 style="margin-top:0">Evening Prayers</h4>
                        <p><strong>Asr:</strong> <span class="prayer-time">{}</span></p>
                        <p><strong>Maghrib:</strong> <span class="prayer-time">{}</span></p>
                        <p><strong>Isha:</strong> <span class="prayer-time">{}</span></p>
                    </div>
                    """.format(timings['Asr'], timings['Maghrib'], timings['Isha']), unsafe_allow_html=True)
                
                # Additional timings
                with st.expander("Additional Timings"):
                    st.markdown("""
                    <p><strong>Imsak:</strong> {}</p>
                    <p><strong>Midnight:</strong> {}</p>
                    <p><strong>Firstthird:</strong> {}</p>
                    <p><strong>Lastthird:</strong> {}</p>
                    """.format(timings['Imsak'], timings['Midnight'], timings['Firstthird'], timings['Lastthird']), unsafe_allow_html=True)
                
                # Additional information
                with st.expander("Prayer Calculation Method Information"):
                    st.markdown("""
                    <p>The prayer times are calculated based on the selected method:</p>
                    <ul>
                        <li><strong>Method 0:</strong> Shia Ithna-Ashari</li>
                        <li><strong>Method 1:</strong> University of Islamic Sciences, Karachi</li>
                        <li><strong>Method 2:</strong> Islamic Society of North America</li>
                        <li><strong>Method 3:</strong> Muslim World League</li>
                        <li><strong>Method 4:</strong> Umm Al-Qura University, Makkah</li>
                        <li><strong>Method 5:</strong> Egyptian General Authority of Survey</li>
                        <li><strong>Method 7:</strong> Institute of Geophysics, University of Tehran</li>
                        <li><strong>Method 8:</strong> Gulf Region</li>
                        <li><strong>Method 9:</strong> Kuwait</li>
                    </ul>
                    """, unsafe_allow_html=True)
            else:
                st.error("Error fetching prayer times. Please check the city and country names and try again.")
        else:
            st.error("Please enter both city and country.")

elif page == "🤲 Duas Collection":
    st.markdown("<h2 class='section-header'>Duas Collection</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>A collection of daily supplications (duas) with Arabic text, transliteration, and translation in both English and Urdu.</p>
        <p>Dua is the act of supplication or calling out to Allah. It is an expression of submission and humility to God. The Prophet Muhammad ﷺ said, "Dua is worship." (Tirmidhi)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get duas
    loading_animation()
    duas = get_duas()
    
    # Create categories for duas
    categories = {
        "Daily Activities": ["Dua for Beginning a Meal", "Dua After Completing a Meal", "Dua Before Entering the Bathroom", "Dua for Food and Drink"],
        "Morning & Evening": ["Dua When Waking Up", "Dua Before Sleeping", "Dua for Protection"],
        "Worship": ["Dua for Entering the Mosque", "Dua for Leaving the Mosque", "Dua for Seeking Knowledge"],
        "Family & Travel": ["Dua for Parents", "Dua for Traveling", "Dua for Returning from Travel"],
        "Emotional Well-being": ["Dua for Anxiety and Sorrow", "Dua for Rain"]
    }
    
    # Create a tab for each category with animations
    dua_tabs = st.tabs(list(categories.keys()))
    
    for i, (category, titles) in enumerate(categories.items()):
        with dua_tabs[i]:
            for title in titles:
                # Find the dua with this title
                dua = next((d for d in duas if title == d["title"]), None)
                if dua:
                    with st.expander(dua["title"]):
                        st.markdown(f"""
                        <div class="arabic-text">{dua['arabic']}</div>
                        <div class="urdu-text">{dua['urdu']}</div>
                        <p><strong>Transliteration:</strong> {dua['transliteration']}</p>
                        <p><strong>Translation:</strong> {dua['translation']}</p>
                        <p><strong>Reference:</strong> {dua['reference']}</p>
                        """, unsafe_allow_html=True)
    
    # Allow users to search for duas
    st.markdown("<h3>Search Duas</h3>", unsafe_allow_html=True)
    search_term = st.text_input("Search by keyword", placeholder="e.g. morning, food, protection")
    
    if search_term:
        search_results = [dua for dua in duas if search_term.lower() in dua['title'].lower() or 
                          search_term.lower() in dua['translation'].lower() or
                          search_term.lower() in dua['urdu'].lower()]
        
        if search_results:
            st.success(f"Found {len(search_results)} duas matching '{search_term}'")
            for dua in search_results:
                with st.expander(dua["title"]):
                    st.markdown(f"""
                    <div class="arabic-text">{dua['arabic']}</div>
                    <div class="urdu-text">{dua['urdu']}</div>
                    <p><strong>Transliteration:</strong> {dua['transliteration']}</p>
                    <p><strong>Translation:</strong> {dua['translation']}</p>
                    <p><strong>Reference:</strong> {dua['reference']}</p>
                    """, unsafe_allow_html=True)
        else:
            st.warning(f"No duas found matching '{search_term}'")
            # Suggest some popular duas
            st.markdown("""
            <div class="info-box">
                <h4>Popular Duas</h4>
                <p>Try searching for these common duas:</p>
                <ul>
                    <li>Protection</li>
                    <li>Food</li>
                    <li>Morning</li>
                    <li>Anxiety</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with st.expander("About Duas"):
     st.markdown('<div class="info-box">', unsafe_allow_html=True)
    
     st.write("The duas presented here are from authentic sources including the Quran and Hadith. They cover various aspects of daily life and are recommended for regular practice.")
    
     st.write("When making dua, it is recommended to:")
    
     st.markdown("""
     <ul>
        <li>Begin with praising Allah</li>
        <li>Send blessings upon the Prophet Muhammad ﷺ</li>
        <li>Raise your hands with palms facing upward</li>
        <li>Be sincere and focused</li>
        <li>End by sending blessings upon the Prophet Muhammad ﷺ again</li>
     </ul>
    """, unsafe_allow_html=True)
    
     st.write("The Prophet Muhammad ﷺ said: \"Nothing is more honorable to Allah the Most High than dua.\" (Sahih al-Jami)")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📿 Durood Shareef":
    st.markdown("<h2 class='section-header'>Durood Shareef Collection</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>Durood Shareef refers to the invocation of blessings upon the Prophet Muhammad ﷺ. The Prophet ﷺ said, "Whoever sends blessings upon me once, Allah will send blessings upon him tenfold." (Muslim)</p>
        <p>Reciting Durood is one of the most virtuous acts and brings numerous blessings in this world and the hereafter.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get durood collection
    loading_animation()
    duroods = get_durood_shareef()
    
    # Display each durood in an expander with animations
    for durood in duroods:
        with st.expander(durood["title"]):
            st.markdown(f"""
            <div class="arabic-text">{durood['arabic']}</div>
            <div class="urdu-text">{durood['urdu']}</div>
            <p><strong>Transliteration:</strong> {durood['transliteration']}</p>
            <p><strong>Translation:</strong> {durood['translation']}</p>
            <p><strong>Virtues:</strong> {durood['virtues']}</p>
            """, unsafe_allow_html=True)
    
    # Durood counter with beautiful animation
    st.markdown("<h3>Daily Durood Counter</h3>", unsafe_allow_html=True)
    
    # Initialize durood count in session state if not present
    if 'durood_count' not in st.session_state:
        st.session_state.durood_count = 0
    
    # Display current count and progress
    col1, col2 = st.columns([2, 1])
    
    with col1:
        count_progress = (st.session_state.durood_count / 100) * 100
        st.markdown(f"""
        <div class="card" style="animation: fadeIn 0.8s ease-in-out;">
            <h4 style="margin-top:0">Daily Goal</h4>
            <p>Many scholars recommend reciting Durood Shareef at least 100 times daily.</p>
            
            <div style="border: 1px solid #ddd; border-radius: 50px; padding: 10px; margin-top: 10px; background-color: #f5f5f5; box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>Progress:</span>
                    <span>{st.session_state.durood_count}/100</span>
                </div>
                <div class="durood-progress">
                    <div class="durood-progress-bar" style="width: {min(count_progress, 100)}%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Buttons to increment count with animation effects
        col1a, col1b, col1c = st.columns(3)
        
        with col1a:
            if st.button("Add 1", key="add_1", use_container_width=True):
                st.session_state.durood_count += 1
                st.rerun()
        
        with col1b:
            if st.button("Add 10", key="add_10", use_container_width=True):
                st.session_state.durood_count += 10
                st.rerun()
        
        with col1c:
            if st.button("Reset", key="reset_durood", use_container_width=True):
                st.session_state.durood_count = 0
                st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card" style="animation: fadeIn 1s ease-in-out;">
            <h4 style="margin-top:0">Best Times to Recite</h4>
            <ul>
                <li>Friday is especially virtuous for sending Durood</li>
                <li>After the Adhan (call to prayer)</li>
                <li>During the final sitting in prayer</li>
                <li>Before making dua (supplication)</li>
                <li>In gatherings, to bring blessings</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Display information about benefits of reciting Durood
    with st.expander("Benefits of Reciting Durood Shareef"):
        st.markdown("""
        <div class="info-box">
            <h4 style="margin-top:0">Virtues of Sending Blessings upon the Prophet Muhammad ﷺ</h4>
            
            <p>The Prophet Muhammad ﷺ said:</p>
            
            <ul>
                <li>"The closest of people to me on the Day of Resurrection will be those who send the most blessings upon me." (Tirmidhi)</li>
                <li>"Whoever sends blessings upon me once, Allah will send blessings upon him tenfold." (Muslim)</li>
                <li>"The miser is the one in whose presence I am mentioned and he does not send blessings upon me." (Tirmidhi)</li>
                <li>"Do not make your houses graves, and do not make my grave a place of celebration. Send blessings upon me, for your blessings reach me wherever you are." (Abu Dawud)</li>
            </ul>
            
            <p><strong>Benefits of reciting Durood Shareef:</strong></p>
            
            <ol>
                <li>Allah sends ten blessings upon the one who sends one blessing upon the Prophet ﷺ</li>
                <li>It is a means of having one's sins forgiven</li>
                <li>It is a means of having one's needs fulfilled</li>
                <li>It brings one closer to the Prophet ﷺ on the Day of Judgment</li>
                <li>It is a means of gaining the Prophet's ﷺ intercession</li>
                <li>It is a means of having one's supplications accepted</li>
                <li>It brings blessings and peace to one's life</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

elif page == "🎵 Naats Collection":
    st.markdown("<h2 class='section-header'>Naats Collection</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>Naat is a devotional poetry in praise of Prophet Muhammad ﷺ. This collection features beautiful naats by renowned reciters from around the world.</p>
        <p>Listening to and reciting naats is a way of expressing love and devotion to the Prophet Muhammad ﷺ.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add Live YouTube Naats
    add_youtube_live()
    
    # Get naats
    loading_animation()
    naats = get_naats()
    
    # Create categories by language
    naats_by_language = {}
    for naat in naats:
        if naat['language'] not in naats_by_language:
            naats_by_language[naat['language']] = []
        naats_by_language[naat['language']].append(naat)
    
    # Create tabs for languages
    language_tabs = st.tabs(list(naats_by_language.keys()))
    
    for i, (language, language_naats) in enumerate(naats_by_language.items()):
        with language_tabs[i]:
            # Group by reciter
            naats_by_reciter = {}
            for naat in language_naats:
                if naat['reciter'] not in naats_by_reciter:
                    naats_by_reciter[naat['reciter']] = []
                naats_by_reciter[naat['reciter']].append(naat)
            
            # Display naats grouped by reciter
            for reciter, reciter_naats in naats_by_reciter.items():
                st.markdown(f"<h3>{reciter}</h3>", unsafe_allow_html=True)
                
                for naat in reciter_naats:
                    st.markdown(f"""
                    <div class="naat-card" style="animation: fadeIn 0.8s ease-in-out;">
                        <h3 class="naat-title">{naat['title']}</h3>
                        <p class="naat-reciter">Duration: {naat['duration']}</p>
                        <div class="urdu-text" style="background-color: #f5f5f5; margin-bottom: 15px;">{naat['lyrics_excerpt']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Embed SoundCloud player
                    st.components.v1.iframe(
                        src=f"https://w.soundcloud.com/player/?url={naat['audio_url']}&color=%23046307&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false",
                        height=120,
                        scrolling=False
                    )
    
    # Featured naats section
    st.markdown("<h3>Featured Naats</h3>", unsafe_allow_html=True)
    
    # Select 3 random naats to feature
    featured_naats = random.sample(naats, min(3, len(naats)))
    
    # Create columns for featured naats
    cols = st.columns(len(featured_naats))
    
    for i, (col, naat) in enumerate(zip(cols, featured_naats)):
        with col:
            st.markdown(f"""
            <div class="naat-card" style="animation: fadeIn {0.8 + i*0.2}s ease-in-out;">
                <h3 class="naat-title">{naat['title']}</h3>
                <p class="naat-reciter">{naat['reciter']}</p>
                <p>Duration: {naat['duration']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Embed SoundCloud player
            st.components.v1.iframe(
                src=f"https://w.soundcloud.com/player/?url={naat['audio_url']}&color=%23046307&auto_play=false&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false",
                height=120,
                scrolling=False
            )
    
    # Information about Naats
    with st.expander("About Naats"):
        st.markdown("""
        <div class="info-box">
            <p>Naat (نعت) is a poetry that specifically praises the Prophet Muhammad ﷺ. The practice of writing and reciting naat has been a long-standing tradition in Islamic culture.</p>
            
            <p>Naats are composed and recited in many languages including Arabic, Urdu, Persian, Punjabi, Sindhi, and others. They express love, devotion, and respect for the Prophet Muhammad ﷺ.</p>
            
            <p>The tradition of naat goes back to the time of the Prophet Muhammad ﷺ when his companions would compose and recite poetry in his praise. The Prophet ﷺ appreciated such poetry when it was within the bounds of propriety.</p>
            
            <p>Famous naat reciters include Junaid Jamshed, Sami Yusuf, Owais Raza Qadri, and many others who have contributed to this beautiful art form.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📋 Asma Al-Husna":
    st.markdown("<h2 class='section-header'>Asma Al-Husna - The 99 Names of Allah</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>The Prophet Muhammad ﷺ said: "Allah has ninety-nine names, one hundred minus one. Whoever enumerates them will enter Paradise." (Bukhari)</p>
        <p>The Asma al-Husna (The Most Beautiful Names) refer to the 99 names of Allah mentioned in Islamic tradition.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get Asma Al-Husna
    loading_animation()
    names = get_asma_al_husna()
    
    # Display view options with animation effects
    view_option = st.radio("Select View", ["Grid View", "List View", "Details View"], horizontal=True)
    
    if view_option == "Grid View":
        # Display in a grid with animations
        cols_per_row = 3
        rows = (len(names) + cols_per_row - 1) // cols_per_row
        
        for i in range(rows):
            row_cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                idx = i * cols_per_row + j
                if idx < len(names):
                    name = names[idx]
                    with row_cols[j]:
                        st.markdown(f"""
                        <div class="name-card" style="animation: fadeIn {0.5 + (idx * 0.02)}s ease-in-out;">
                            <div class="name-number">{name['number']}</div>
                            <h3 style="margin: 0; color: #046307; text-align: center; padding-left: 30px;">{name['name']}</h3>
                            <p style="margin: 5px 0 0 0; font-size: 0.9rem; text-align: center;">{name['transliteration']}</p>
                            <p style="margin: 5px 0 0 0; font-size: 0.8rem; text-align: center;">{name['en']['meaning']}</p>
                        </div>
                        """, unsafe_allow_html=True)
    
    elif view_option == "List View":
        # Create a DataFrame for easier filtering
        names_df = pd.DataFrame({
            'number': [name['number'] for name in names],
            'name': [name['name'] for name in names],
            'transliteration': [name['transliteration'] for name in names],
            'meaning': [name['en']['meaning'] for name in names]
        })
        
        # Add a search functionality
        search_term = st.text_input("Search by name or meaning", placeholder="e.g. Merciful, Creator")
        
        if search_term:
            filtered_names = names_df[
                names_df['transliteration'].str.contains(search_term, case=False) | 
                names_df['meaning'].str.contains(search_term, case=False)
            ]
            
            if not filtered_names.empty:
                st.success(f"Found {len(filtered_names)} names matching '{search_term}'")
                for _, name in filtered_names.iterrows():
                    st.markdown(f"""
                    <div class="name-card" style="animation: fadeIn 0.8s ease-in-out;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div class="name-number">{name['number']}</div>
                            <h3 style="margin: 0; color: #046307;">{name['name']}</h3>
                        </div>
                        <p style="margin: 5px 0 0 0;"><strong>Transliteration:</strong> {name['transliteration']}</p>
                        <p style="margin: 5px 0 0 0;"><strong>Meaning:</strong> {name['meaning']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning(f"No names found matching '{search_term}'")
        else:
            # Display all names in a list with animations
            for i, name in enumerate(names):
                st.markdown(f"""
                <div class="name-card" style="animation: fadeIn {0.5 + (i * 0.02)}s ease-in-out;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="name-number">{name['number']}</div>
                        <h3 style="margin: 0; color: #046307;">{name['name']}</h3>
                    </div>
                    <p style="margin: 5px 0 0 0;"><strong>Transliteration:</strong> {name['transliteration']}</p>
                    <p style="margin: 5px 0 0 0;"><strong>Meaning:</strong> {name['en']['meaning']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    else:  # Details View
        # Group names into categories
        categories = {
            "Divine Essence": [1, 2, 3, 4, 5],
            "Divine Power": [6, 7, 8, 9, 10, 69, 70],
            "Divine Mercy": [45, 46, 47, 48, 49, 50],
            "Divine Knowledge": [11, 12, 13, 14, 27, 28, 29],
            "Divine Majesty": [37, 38, 39, 40, 41, 42],
            "Divine Providence": [15, 16, 17, 18, 19, 20],
            "Divine Justice": [30, 31, 32, 33, 34]
        }
        
        # Create tabs for categories
        category_tabs = st.tabs(list(categories.keys()))
        
        for i, (category, name_numbers) in enumerate(categories.items()):
            with category_tabs[i]:
                for number in name_numbers:
                    name = next((n for n in names if n['number'] == number), None)
                    if name:
                        with st.expander(f"{number}. {name['transliteration']} ({name['en']['meaning']})"):
                            st.markdown(f"""
                            <div style="text-align: center; margin-bottom: 15px;">
                                <h2 style="color: #046307; font-size: 2.5rem;">{name['name']}</h2>
                                <p style="font-size: 1.2rem;">{name['transliteration']}</p>
                            </div>
                            
                            <p><strong>Meaning:</strong> {name['en']['meaning']}</p>
                            
                            <div class="info-box">
                                <p><strong>Significance:</strong> The name {name['transliteration']} emphasizes Allah's attribute of being {name['en']['meaning']}.</p>
                                <p><strong>In the Quran:</strong> This name or its derivatives appear in several verses.</p>
                            </div>
                            
                            <p><strong>Benefits of Recitation:</strong> Remembering this name helps believers connect with this divine attribute and seek Allah's blessings through it.</p>
                            """, unsafe_allow_html=True)
    
     # Display information about Asma Al-Husna
    with st.expander("About Asma Al-Husna"):
        st.markdown("""
        <div class="info-box">
            <h4 style="margin-top:0">The 99 Names of Allah</h4>
            
            <p>These names describe Allah's attributes and characteristics. Muslims are encouraged to call upon Allah using these names, especially in times of need and during supplication.</p>
            
            <p><strong>Significance:</strong></p>
            
            <ul>
                <li>Each name represents a unique attribute of Allah</li>
                <li>Remembering and reflecting on these names brings believers closer to understanding Allah's nature</li>
                <li>Calling upon Allah by His beautiful names is recommended in the Quran: "And to Allah belong the best names, so invoke Him by them" (Quran 7:180)</li>
                <li>Memorizing and understanding these names is considered a means of increasing one's faith and knowledge</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "📒 Names of Muhammad ﷺ":
    st.markdown("<h2 class='section-header'>Beautiful Names of Prophet Muhammad ﷺ</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p>Prophet Muhammad ﷺ has many beautiful names and titles mentioned in the Quran, Hadith, and Islamic tradition. Each name reflects an aspect of his noble character and mission.</p>
        <p>Learning and understanding these names helps us to appreciate the comprehensive nature of the Prophet's ﷺ personality and mission.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get Names of Muhammad
    loading_animation()
    names = get_names_of_muhammad()
    
    # Display view options with animation effects
    view_option = st.radio("Select View", ["Grid View", "List View", "Detailed View"], horizontal=True)
    
    if view_option == "Grid View":
        # Display in a grid with animations
        cols_per_row = 3
        rows = (len(names) + cols_per_row - 1) // cols_per_row
        
        for i in range(rows):
            row_cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                idx = i * cols_per_row + j
                if idx < len(names):
                    name = names[idx]
                    with row_cols[j]:
                        st.markdown(f"""
                        <div class="name-card" style="animation: fadeIn {0.5 + (idx * 0.02)}s ease-in-out;">
                            <div class="name-number">{name['number']}</div>
                            <h3 style="margin: 0; color: #046307; text-align: center; padding-left: 30px;">{name['name']}</h3>
                            <p style="margin: 5px 0 0 0; font-size: 0.9rem; text-align: center;">{name['transliteration']}</p>
                            <p style="margin: 5px 0 0 0; font-size: 0.8rem; text-align: center;">{name['meaning']}</p>
                        </div>
                        """, unsafe_allow_html=True)
    
    elif view_option == "List View":
        # Create a DataFrame for easier filtering
        names_df = pd.DataFrame(names)
        
        # Add a search functionality
        search_term = st.text_input("Search by name or meaning", placeholder="e.g. Mercy, Light, Guide")
        
        if search_term:
            filtered_names = names_df[
                names_df['transliteration'].str.contains(search_term, case=False) | 
                names_df['meaning'].str.contains(search_term, case=False) |
                names_df['description'].str.contains(search_term, case=False)
            ]
            
            if not filtered_names.empty:
                st.success(f"Found {len(filtered_names)} names matching '{search_term}'")
                for _, name in filtered_names.iterrows():
                    st.markdown(f"""
                    <div class="name-card" style="animation: fadeIn 0.8s ease-in-out;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div class="name-number">{name['number']}</div>
                            <h3 style="margin: 0; color: #046307;">{name['name']}</h3>
                        </div>
                        <p style="margin: 5px 0 0 0;"><strong>Transliteration:</strong> {name['transliteration']}</p>
                        <p style="margin: 5px 0 0 0;"><strong>Meaning:</strong> {name['meaning']}</p>
                        <p style="margin: 5px 0 0 0;"><strong>Description:</strong> {name['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning(f"No names found matching '{search_term}'")
        else:
            # Display all names in a list with animations
            for i, name in enumerate(names):
                st.markdown(f"""
                <div class="name-card" style="animation: fadeIn {0.5 + (i * 0.02)}s ease-in-out;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="name-number">{name['number']}</div>
                        <h3 style="margin: 0; color: #046307;">{name['name']}</h3>
                    </div>
                    <p style="margin: 5px 0 0 0;"><strong>Transliteration:</strong> {name['transliteration']}</p>
                    <p style="margin: 5px 0 0 0;"><strong>Meaning:</strong> {name['meaning']}</p>
                    <p style="margin: 5px 0 0 0;"><strong>Description:</strong> {name['description']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    else:  # Detailed View
        # Group names into categories
        categories = {
            "Names in the Quran": [1, 2, 26, 27, 28, 29],
            "Prophetic Titles": [5, 6, 7, 8, 12, 13, 35, 36, 37],
            "Character Attributes": [9, 10, 11, 20, 21, 22],
            "Intercessor Roles": [16, 18, 19, 41, 42, 43, 48],
            "Divine Connection": [30, 31, 32, 33, 34, 39]
        }
        
        # Create tabs for categories
        category_tabs = st.tabs(list(categories.keys()))
        
        for i, (category, name_numbers) in enumerate(categories.items()):
            with category_tabs[i]:
                for number in name_numbers:
                    name = next((n for n in names if n['number'] == number), None)
                    if name:
                        with st.expander(f"{number}. {name['transliteration']} ({name['meaning']})"):
                            st.markdown(f"""
                            <div class="name-detail-card">
                                <div class="name-arabic">{name['name']}</div>
                                <div class="name-transliteration">{name['transliteration']}</div>
                                <div class="name-meaning">{name['meaning']}</div>
                                
                                <div class="name-description">
                                    <strong>Description:</strong> {name['description']}
                                </div>
                                
                                <div class="name-reference">
                                    <strong>Reference:</strong> {name.get('reference', 'The reference for this name is not available.')}
                                </div>
                                
                                <div class="name-benefit">
                                    <strong>Significance:</strong> {name.get('significance', 'The significance of this name is not specified.')}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
    
    # Display information about Names of Muhammad
    with st.expander("About the Names of Prophet Muhammad ﷺ"):
        st.markdown("""
        <div class="info-box">
            <h4 style="margin-top:0">The Beautiful Names of Prophet Muhammad ﷺ</h4>
            
            <p>Prophet Muhammad ﷺ is known by many beautiful names and titles that describe his character, mission, and status. Some of these names are mentioned in the Quran, while others appear in authentic hadith or Islamic tradition.</p>
            
            <p>The most common name "Muhammad" means "The Praised One," indicating his praiseworthy character and the high esteem in which he is held. Another common name "Ahmad" means "The Most Praised One," and is mentioned in the Quran in Surah As-Saff (61:6).</p>
            
            <p><strong>Significance:</strong></p>
            
            <ul>
                <li>Each name represents a different aspect of the Prophet's ﷺ character and mission</li>
                <li>Learning these names helps Muslims to understand and appreciate the comprehensive nature of his prophethood</li>
                <li>Many of these names are used in sending salutations (Durood) upon the Prophet ﷺ</li>
                <li>Some names emphasize his role as a mercy to the worlds, while others highlight his status as the final prophet</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Add footer
st.markdown("""
<div class="footer">
    <p>Developed by Riaz Hussain Saifi | Islamic Resources Hub &copy; 2025</p>
    <p>This application uses various Islamic APIs to provide accurate information.</p>
    <p>For any suggestions or feedback, please contact the developer.</p>
    <p><a href="https://www.linkedin.com/in/riaz-hussain-saifi" target="_blank">LinkedIn Profile</a></p>
</div>
""", unsafe_allow_html=True)

# Handle page navigation from session state
if 'page' in st.session_state:
    page = st.session_state.page
    del st.session_state.page
    st.rerun()