import streamlit as st
import pandas as pd
import numpy as np
import pickle 





# Load All Files
with open('pipeline_xgb_opt', 'rb') as file_1:
  pipeline_xgb_opt = pickle.load(file_1)

def run() :
  # Membuat Title 
  st.markdown("<h1 style='text-align: center;'>Resign Prediction</h1>", unsafe_allow_html=True)

  # Menambahkan Deskripsi Form
  st.write('Page ini berisi model untuk memprediksi potensi resign karyawan dalam 2 tahun mendatang')
  st.write('Mohon persiapkan data terlebih dahulu sebelum melakukan prediksi')

  #Membuat Form
  with st.form(key= 'form_employee'):
      Education = st.radio('Education', options=['Bachelors','Masters','PHD'], horizontal=True)
      JoiningYear = st.number_input('Joining Year', min_value=2012, max_value=2018, value=2015 ,step=1, help='Tahun bergabungnya karyawan')
      City = st.selectbox('City',('Bangalore','Pune','New Delhi'),index=1)
      PaymentTier = st.selectbox('Payment Tier',(1,2,3),index=1)
      Age = st.slider('Age',22,41,25)
      Gender = st.radio('Gender', options=['Male','Female'], horizontal=False)
      EverBenched = st.selectbox('Ever Benched',('Yes','No'),index=1)
      ExperienceInCurrentDomain= st.slider('Experience',0,7,2)
      submitted = st.form_submit_button('Predict')

  #Membuat Data Inference
  data_inf = {
      'Education' : Education, 
      'JoiningYear' : JoiningYear, 
      'City' : City, 
      'PaymentTier' : PaymentTier, 
      'Age' : Age, 
      'Gender' : Gender,
      'EverBenched' : EverBenched, 
      'ExperienceInCurrentDomain' : ExperienceInCurrentDomain
  }

  #Membuat Dataframe
  data_inf = pd.DataFrame([data_inf])
  data_inf

  #Prediksi Kemungkinan Resign

  if submitted :
      # Predict using XGBoost Parameter Tuning
      y_pred_inf = pipeline_xgb_opt.predict(data_inf)

      if y_pred_inf == 1:
        prediction = 'Resign'
      else:
        prediction = 'Not Resign'
        
      st.write('# Resign Prediction : ', prediction)

if __name__ == '__main__':
    run()



