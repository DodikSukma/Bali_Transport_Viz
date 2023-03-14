# --------- IMPORT MODULE YANG DIGUNAKAN ------- #

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   streamlit_option_menu import option_menu 
import plotly.express as px
import plotly.figure_factory as ff
import base64

# --------- IMPORT DATASET --------- #
df = pd.read_csv('Kendaraan Bali.csv')

# -------- MEMBUAT TAMPILAN ----------- #

st.set_page_config(
    page_title="vis_data_bali",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg_fix.jpg') 

# --------- MEMBUAT FUNGSI LINEPLOT -------- #
def lineplot():
    
    col1, col2 = st.columns(2)
    fig = px.line(df, 
        x = "TAHUN", y = "BUS",title = "🚌BUS")
    col1.plotly_chart(fig,use_container_width = True)

    fig = px.line(df, 
      x = "TAHUN", y = "SEPEDA MOTOR",title = "🛵SEPEDA MOTOR")
    col2.plotly_chart(fig,use_container_width = True)

    fig = px.line(df, 
        x = "TAHUN", y = "MOBIL PENUMPANG",title = "🚗MOBIL PENUMPANG")
    col1.plotly_chart(fig,use_container_width = True)

    fig = px.line(df, 
      x = "TAHUN", y = "TRUK",title = "🚛TRUK")
    col2.plotly_chart(fig,use_container_width = True)

    fig = px.line(df, 
      x = "TAHUN", y = ["TRUK","BUS","MOBIL PENUMPANG","SEPEDA MOTOR"],title = "LINE PLOT KENDARAAN DI BALI")
    st.plotly_chart(fig,use_container_width = True)

# --------- MEMBUAT FUNGSI BARCHART -------- #
def barchart():
    col1, col2 = st.columns(2)
    fig = px.bar(df, 
        x = "TAHUN", y = "BUS",title = "BUS")
    col1.plotly_chart(fig,use_container_width = True)

    fig = px.bar(df, 
      x = "TAHUN", y = "SEPEDA MOTOR",title = "SEPEDA MOTOR")
    col2.plotly_chart(fig,use_container_width = True)

    fig = px.bar(df, 
        x = "TAHUN", y = "MOBIL PENUMPANG",title = "MOBIL PENUMPANG")
    col1.plotly_chart(fig,use_container_width = True)

    fig = px.bar(df, 
      x = "TAHUN", y = "TRUK",title = "TRUK")
    col2.plotly_chart(fig,use_container_width = True)

    fig = px.bar(df, 
      x = "TAHUN", y = ["TRUK","BUS","MOBIL PENUMPANG","SEPEDA MOTOR"],title = "bar PLOT KENDARAAN DI BALI")
    st.plotly_chart(fig,use_container_width = True)

st.write("""
            # VISUALISASI DATA JUMLAH KENDARAAN DI PROVINSI BALI BERDASARKAN JENISNYA (1996 - 2021)
""")

#----- MEMBUAT MENU APLIKASI -------#

pilihan =   option_menu(
            menu_title="MENU",  # required
            options=["HOME", "VISUALISASI", "REFRENSI"],  # required
            icons=["house", "bi bi-bar-chart-fill", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

#----- IF ELSE STATEMENT FOR MENU -------#

if pilihan == "HOME":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
       st.header("🚌BUS")
       st.write(df.drop(columns=['TRUK', 'SEPEDA MOTOR', 'MOBIL PENUMPANG', 'TOTAL']))
       st.write("📑RATA RATA : ",round(np.mean(df['BUS'])))
    with col2:
       st.header("🚛TRUK")
       st.write(df.drop(columns=['BUS', 'SEPEDA MOTOR', 'MOBIL PENUMPANG', 'TOTAL']))
       st.write("📑RATA RATA : ",round(np.mean(df['TRUK'])))
    with col3:
       st.header("🛵MOTOR")
       st.write(df.drop(columns=['TRUK', 'BUS', 'MOBIL PENUMPANG', 'TOTAL']))
       st.write("📑RATA RATA : ",round(np.mean(df['SEPEDA MOTOR'])))
    with col4:
       st.header("🚗MOBIL")
       st.write(df.drop(columns=['TRUK', 'SEPEDA MOTOR', 'BUS', 'TOTAL']))
       st.write("📑RATA RATA : ",round(np.mean(df['MOBIL PENUMPANG'])))

elif pilihan == "VISUALISASI":
#---- SIDE BAR ----#
    options = st.sidebar.selectbox(
    'PILIH VISUALISASI',
    ['LINE PLOT','BAR CHART'],
    )

    if options == 'LINE PLOT':
       lineplot()
    else:
        barchart()
else :
    st.write("""

     # Dataset ini diperoleh dari Badan Pusat Statistik Provinsi Bali
    
    """
    )