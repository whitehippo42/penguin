import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('Penguin Prediction App')
st.info('This is end to end app')

with st.expander("Data"):
    st.write("Raw Data")
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    df

    st.write("input vars")
    X_raw = df.drop("species", axis=1)
    X_raw

    st.write("Target vars")
    Y_raw = df.species
    Y_raw
    
    st.write("Description St")
    des = df.describe()
    des
    
    st.write("More information")
    inf = df.info()
    inf


with st.expander("Data Visualization"):
    st.scatter_chart(df, x='bill_length_mm', y='body_mass_g', color='species')



with st.expander("Data Preperation"):
    pass

with st.sidebar:
    st.header("Input Vars")
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    bill_length_nm =st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_nm =st.slider('Bill depth (mm)', 13.1, 23.5, 17.2)
    flipper_length_nm =st.slider('Flipper length (mm)', 172.00, 231.00, 201.00)
    body_mass_g =st.slider('Body mass (g)', 2700, 6300, 4207)
    gender =st.selectbox('Gender', ('male', 'Female'))
    data = {'island':island,
            'bill_length_nm':bill_length_nm,
            'bill_depth_nm':bill_depth_nm,
            'flipper_length_nm':flipper_length_nm,
            'body_mass_g':body_mass_g,
            'gender':gender
            }
    input_df = pd.DataFrame(data, index=[0])
    input_penguins =pd.concat([input_df, X_raw], axis=0)

with st.expander("Input Data"):
    st.write("input data")
    input_df
    st.write("combined data")
    input_penguins




