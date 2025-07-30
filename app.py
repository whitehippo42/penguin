import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('Penguin Prediction App')
st.info('This is end to end app')

with st.expander("Data"):
    pass

with st.expander("Data Visualization"):
    pass

with st.expander("Input Data"):
    pass

with st.expander("Data Preperation"):
    pass

with st.sidebar:
    st.header("Input Vars")
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    bill_length_nm =st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_nm =st.slider('Bill depth (mm)', 13.1, 23.5, 17.2)
    flipper_length_nm =st.slider('Flipper length (mm)', 172.00, 231.00, 201.00)
    body_mass_g =st.slider('Body mass (g)', 2700, 6300, 4207)
    gender =st.selector('Gender', ('male', 'Female'))


