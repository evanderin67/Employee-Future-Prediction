import streamlit as st
import eda
import prediction


#Set Config dan icon
st.set_page_config(
        page_title='Resign Prediction',
        layout='wide',
        initial_sidebar_state='expanded' , page_icon='https://imgur.com/sYKazYD.png'
        )

#Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#Membuat navigasi
st.sidebar.markdown("# Evan Derin Ihsanudin - RMT-FTDS-17")
navigation = st.sidebar.selectbox('Pilih Halaman (Resign Prediction/EDA): ', ('Resign Prediction','Exploratory Data Analysis'))
st.sidebar.image("https://imgur.com/sYKazYD.png", use_column_width=True)

#Run modul dengan if else
if navigation == 'Resign Prediction' :
    prediction.run()
else :
    eda.run()