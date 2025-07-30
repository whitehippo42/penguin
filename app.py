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
    st.head("Input Vars")
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
