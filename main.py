import streamlit as st
import base64
import time
import random

# Set page configuration
st.set_page_config(
    page_title="Quran Majeed - Audio Recitation with Urdu Translation",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling (unchanged)
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }
    .css-1d391kg {
        padding: 1rem;
    }
    .para-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    .para-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        background-color: #e8f0fe;
    }
    .para-card-playing {
        background-color: #e3f2fd;
        border: 2px solid #1e88e5;
    }
    .para-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #1e3a8a;
    }
    .para-urdu {
        font-size: 22px;
        font-weight: bold;
        color: #10554a;
        font-family: 'Noto Nastaliq Urdu', serif;
    }
    .surah-name {
        font-size: 16px;
        color: #4b5563;
        margin-top: 8px;
        font-style: italic;
    }
    .header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #1e3a8a 0%, #10554a 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header h1 {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .header h2 {
        font-size: 1.5rem;
        font-weight: normal;
        margin-bottom: 15px;
    }
    .header h3 {
        font-size: 1.2rem;
        font-weight: normal;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #10554a 0%, #1e3a8a 100%);
        color: white;
        border-radius: 10px;
        margin-top: 20px;
    }
    .share-section {
        background-color: #e8f0fe;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
    }
    .developer-info {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        flex-wrap: wrap;
    }
    .dev-bio {
        max-width: 500px;
        text-align: center;
        margin: 10px auto;
    }
    .linkedin-button {
        display: inline-block;
        background-color: #9c27b0;
        color: white;
        padding: 8px 15px;
        border-radius: 5px;
        text-decoration: none;
        margin-left: 10px;
        transition: background-color 0.3s ease;
    }
    .linkedin-button:hover {
        background-color: #7b1fa2;
    }
    .playing-now {
        padding: 15px;
        background-color: #e0f7fa;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
        border-left: 5px solid #00897b;
    }
    .audio-control {
        width: 100%;
        margin: 10px 0;
    }
    .play-button {
        display: inline-block;
        background-color: #1e88e5;
        color: white;
        padding: 8px 15px;
        border-radius: 5px;
        text-decoration: none;
        width: 100%;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .play-button:hover {
        background-color: #1565c0;
    }
    .app-description {
        background-color: #fff8e1;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
        border-left: 5px solid #ffa000;
    }
    .notification {
        background-color: #ffebee;
        color: #c62828;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 5px solid #c62828;
        font-weight: bold;
        text-align: center;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 5px solid #1976d2;
        font-style: italic;
    }
    .reciter-info {
        background-color: #f3e5f5;
        border-radius: 5px;
        padding: 10px 15px;
        margin: 10px 0;
        border-left: 5px solid #8e24aa;
    }
    @media (max-width: 768px) {
        .header h1 {
            font-size: 1.8rem;
        }
        .header h2 {
            font-size: 1.2rem;
        }
        .para-title {
            font-size: 16px;
        }
        .para-urdu {
            font-size: 18px;
        }
        .surah-name {
            font-size: 14px;
        }
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Dictionary of para links
para_links = {
    "1": "http://bit.ly/2qpLHGY",
    "2": "http://bit.ly/2qnS2Ha",
    "3": "http://bit.ly/2sbSqoq",
    "4": "http://bit.ly/2r6TOeq",
    "5": "http://bit.ly/2qzzsYk",
    "6": "http://bit.ly/2qI4EE2",
    "7": "http://bit.ly/2rW88HS",
    "8": "http://bit.ly/2qK0aO4",
    "9": "http://bit.ly/2rBqzB0",
    "10": "http://bit.ly/2s3dkdd",
    "11": "http://bit.ly/2so5po5",
    "12": "http://bit.ly/2rzgVP9",
    "13": "http://bit.ly/2rSIJ1l",
    "14": "http://bit.ly/2sk5Lid",
    "15": "http://bit.ly/2rKJHw3",
    "16": "http://bit.ly/2sMTr7y",
    "17": "http://bit.ly/2r9opp2",
    "18": "http://bit.ly/2rpK4c8",
    "19": "http://bit.ly/2rpq1iW",
    "20": "http://bit.ly/2rAX4Mc",
    "21": "http://bit.ly/2rBv2Aa",
    "22": "http://bit.ly/2sbmkft",
    "23": "http://bit.ly/2rtPXpH",
    "24": "http://bit.ly/2sfUCOE",
    "25": "http://bit.ly/2smfZxF",
    "26": "http://bit.ly/2tLUEvC",
    "27": "http://bit.ly/2tru5wz",
    "28": "http://bit.ly/2rXeW98",
    "29": "http://bit.ly/2s5NLEk",
    "30": "http://bit.ly/2s1BBB4"
}

# Dictionary of para names and included surahs
para_info = {
    "1": {"name": "الم", "surahs": "Al-Fatihah, Al-Baqarah"},
    "2": {"name": "سیقول", "surahs": "Al-Baqarah"},
    "3": {"name": "تلك الرسل", "surahs": "Al-Baqarah, Ali 'Imran"},
    "4": {"name": "لن تنالوا", "surahs": "Ali 'Imran, An-Nisa"},
    "5": {"name": "والمحصنات", "surahs": "An-Nisa, Al-Ma'idah"},
    "6": {"name": "لا یحب اللہ", "surahs": "Al-Ma'idah, Al-An'am"},
    "7": {"name": "وإذا سمعوا", "surahs": "Al-An'am, Al-A'raf"},
    "8": {"name": "ولو أننا", "surahs": "Al-A'raf, Al-Anfal, At-Tawbah"},
    "9": {"name": "قال الملأ", "surahs": "At-Tawbah, Yunus, Hud"},
    "10": {"name": "واعلموا", "surahs": "Hud, Yusuf, Ar-Ra'd"},
    "11": {"name": "يعتذرون", "surahs": "Ar-Ra'd, Ibrahim, Al-Hijr, An-Nahl"},
    "12": {"name": "وما من دابة", "surahs": "An-Nahl, Al-Isra, Al-Kahf"},
    "13": {"name": "وما أبرئ", "surahs": "Al-Kahf, Maryam, Ta-Ha"},
    "14": {"name": "اقترب للناس", "surahs": "Ta-Ha, Al-Anbya, Al-Hajj"},
    "15": {"name": "قد أفلح", "surahs": "Al-Hajj, Al-Mu'minun, An-Nur, Al-Furqan"},
    "16": {"name": "قال ألم", "surahs": "Al-Furqan, Ash-Shu'ara, An-Naml"},
    "17": {"name": "اقترب", "surahs": "An-Naml, Al-Qasas, Al-'Ankabut"},
    "18": {"name": "قد سمع", "surahs": "Al-'Ankabut, Ar-Rum, Luqman, As-Sajdah, Al-Ahzab"},
    "19": {"name": "وقال الذين", "surahs": "Al-Ahzab, Saba, Fatir, Ya-Sin"},
    "20": {"name": "أمن خلق", "surahs": "Ya-Sin, As-Saffat, Sad, Az-Zumar, Ghafir"},
    "21": {"name": "إليه يرد", "surahs": "Ghafir, Fussilat, Ash-Shuraa, Az-Zukhruf, Ad-Dukhan"},
    "22": {"name": "ومن يقنت", "surahs": "Ad-Dukhan, Al-Jathiyah, Al-Ahqaf, Muhammad, Al-Fath, Al-Hujurat"},
    "23": {"name": "وما لي", "surahs": "Al-Hujurat, Qaf, Adh-Dhariyat, At-Tur, An-Najm, Al-Qamar, Ar-Rahman, Al-Waqi'ah"},
    "24": {"name": "فمن أظلم", "surahs": "Al-Waqi'ah, Al-Hadid, Al-Mujadila, Al-Hashr, Al-Mumtahanah, As-Saf, Al-Jumu'ah, Al-Munafiqun, At-Taghabun, At-Talaq, At-Tahrim"},
    "25": {"name": "إليه يرد", "surahs": "At-Tahrim, Al-Mulk, Al-Qalam, Al-Haqqah, Al-Ma'arij, Nuh, Al-Jinn, Al-Muzzammil, Al-Muddathir, Al-Qiyamah, Al-Insan, Al-Mursalat"},
    "26": {"name": "حم", "surahs": "Al-Mursalat, An-Naba, An-Nazi'at, 'Abasa, At-Takwir, Al-Infitar, Al-Mutaffifin, Al-Inshiqaq, Al-Buruj, At-Tariq, Al-A'la, Al-Ghashiyah, Al-Fajr"},
    "27": {"name": "قال فما خطبكم", "surahs": "Al-Fajr, Al-Balad, Ash-Shams, Al-Layl, Ad-Duha, Ash-Sharh, At-Tin, Al-'Alaq, Al-Qadr, Al-Bayyinah, Az-Zalzalah, Al-'Adiyat, Al-Qari'ah, At-Takathur, Al-'Asr, Al-Humazah"},
    "28": {"name": "قد سمع الله", "surahs": "Al-Humazah, Al-Fil, Quraysh, Al-Ma'un, Al-Kawthar, Al-Kafirun, An-Nasr, Al-Masad, Al-Ikhlas, Al-Falaq, An-Nas"},
    "29": {"name": "تبارك الذي", "surahs": "Al-Mulk to Al-Mursalat"},
    "30": {"name": "عم", "surahs": "An-Naba to An-Nas"}
}

# Header section
st.markdown("""
<div class="header">
    <h1>القرآن الكريم</h1>
    <h2>Quran Majeed with Audio Recitation and Urdu Translation</h2>
    <h3>Ramzan Shareef 1446 Hijri</h3>
</div>
""", unsafe_allow_html=True)

# App description
st.markdown("""
<div class="app-description">
    <h3>🌙 Welcome to the Quran Recitation App</h3>
    <p>This app allows you to listen to the beautiful recitation of the Holy Quran with Urdu translation. Simply click on any Para (Juz) below to listen to the recitation. Each audio file contains the complete recitation with Urdu translation for the selected Para.</p>
    <p>For those who cannot read the Quran, this audio recitation provides an opportunity to listen and understand the divine message. May Allah bless you for listening to and sharing the Quran.</p>
</div>
""", unsafe_allow_html=True)

# Reciter information
st.markdown("""
<div class="reciter-info">
    <h3>🎙️ Quran Recitation Credits</h3>
    <p><strong>Tilawat Quran Pak:</strong> Sheikh Mishary Rashid Alafasy</p>
    <p><strong>Urdu Tarjuma:</strong> Molana Muhammad Taqi Usmani</p>
    <p><strong>Urdu Awaz:</strong> Hafiz Afzal Mishtiaq</p>
</div>
""", unsafe_allow_html=True)

# User instruction note
st.markdown("""
<div class="info-box">
    <p><strong>Note:</strong> You must stop or close the current para before playing another one. Click on the "Stop Audio" button to close the current para.</p>
    <p>You can download any para's audio by right-clicking on the audio player and selecting "Download". The audio player also provides options to adjust "Playback Speed", "Pause", and control volume using the built-in controls.</p>
</div>
""", unsafe_allow_html=True)

# Initialize session states
if 'current_para' not in st.session_state:
    st.session_state.current_para = None

if 'timestamp' not in st.session_state:
    st.session_state.timestamp = time.time()

if 'show_notification' not in st.session_state:
    st.session_state.show_notification = False

if 'requested_para' not in st.session_state:
    st.session_state.requested_para = None

# Create a container for the audio player so we can replace it dynamically
audio_container = st.container()

# Display currently playing para
with audio_container:
    if st.session_state.current_para:
        para_num = st.session_state.current_para
        
        # Create a unique key for this audio element
        audio_key = f"audio_{para_num}_{st.session_state.timestamp}"
        
        # Create the playing now section with audio player
        st.markdown(f"""
        <div class="playing-now" id="playing-section-{audio_key}">
            <h3>🎧 Now Playing: Para {para_num} - {para_info[para_num]["name"]}</h3>
            <p>Surahs included: {para_info[para_num]["surahs"]}</p>
            <audio controls autoplay class="audio-control" id="{audio_key}">
                <source src="{para_links[para_num]}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </div>
        """, unsafe_allow_html=True)
        
        # Display notification right after audio player if needed
        if st.session_state.show_notification and st.session_state.requested_para is not None:
            st.markdown(f"""
            <div class="notification">
                <p>Please stop the current Para {st.session_state.current_para} before playing Para {st.session_state.requested_para}.</p>
            </div>
            """, unsafe_allow_html=True)

# Button for stopping audio
if st.session_state.current_para:  # Only show stop button if audio is playing
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⏹️ Stop Audio", key="stop_all_audio"):
            # Reset the current para to stop audio
            st.session_state.current_para = None
            st.session_state.show_notification = False
            st.session_state.requested_para = None
            st.rerun()

# Function to handle para selection
def handle_para_selection(para_num):
    if st.session_state.current_para is None:
        # No para playing, so start this one
        st.session_state.current_para = para_num
        st.session_state.timestamp = time.time()
        st.session_state.show_notification = False
        st.rerun()
    elif st.session_state.current_para == para_num:
        # Same para clicked, just replay it
        st.session_state.timestamp = time.time()
        st.session_state.show_notification = False
        st.rerun()
    else:
        # Different para requested while one is playing
        st.session_state.show_notification = True
        st.session_state.requested_para = para_num
        st.rerun()

# Display all paras in a grid
cols_per_row = 3
total_paras = 30

# Display all paras in a grid
for i in range(0, total_paras, cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < total_paras:
            para_num = str(i + j + 1)
            with cols[j]:
                # Highlight currently playing para
                card_style = "para-card"
                if st.session_state.current_para == para_num:
                    card_style += " para-card-playing"
                
                card_html = f"""
                <div class="{card_style}">
                    <div class="para-title">Para {para_num}</div>
                    <div class="para-urdu">پارہ نمبر {para_num}</div>
                    <div class="surah-name">{para_info[para_num]["name"]}</div>
                    <div class="surah-name">({para_info[para_num]["surahs"]})</div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                
                # Customize button label based on current state
                button_label = "▶️ Play"
                if st.session_state.current_para == para_num:
                    button_label = "🔄 Replay"
                
                # Create button with on_click to handle para selection
                if st.button(button_label, key=f"play_{para_num}"):
                    handle_para_selection(para_num)

# Share section
st.markdown("""
<div class="share-section">
    <h3>📢 Share this App with Others</h3>
    <p>Help spread the beautiful recitation of the Quran with those who cannot read but can listen. Share this app with your friends and family, especially during the blessed month of Ramadan.</p>
    <p>This audio-only app is perfect for those who want to listen to the Quran while traveling, working, or relaxing at home.</p>
    <p>"The best among you are those who learn the Quran and teach it." - Prophet Muhammad (PBUH)</p>
</div>
""", unsafe_allow_html=True)

# Developer information
st.markdown("""
<div class="developer-info">
    <span>Developed by: <strong>Riaz Hussain Saifi</strong></span>
    <a href="https://www.linkedin.com/in/riaz-hussain-saifi" target="_blank" class="linkedin-button">
        Follow on LinkedIn
    </a>
</div>
<div class="dev-bio">
    <p>I'm Riaz Hussain, a senior student. With the arrival of Ramadan 1446 Hijri, I had the thought of creating an app featuring the Quran with Urdu audio translation. This would allow those who cannot see or read to listen and benefit from its beauty, peace, and rewards. I kindly request you to include my parents in your prayers.</p>
</div>
""", unsafe_allow_html=True)

# Footer section
st.markdown("""
<div class="footer">
    <p>بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم</p>
    <p>In the name of Allah, the Most Gracious, the Most Merciful</p>
    <p>© 2025 Quran Majeed App | All rights reserved</p>
</div>
""", unsafe_allow_html=True)

# Add JavaScript to ensure audio plays when loaded
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Find all audio elements and try to play them
    const audioElements = document.querySelectorAll('audio');
    audioElements.forEach(audio => {
        audio.play().catch(e => console.log('Auto-play prevented:', e));
    });
});
</script>
""", unsafe_allow_html=True)