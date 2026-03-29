import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Upload file")

st.subheader("Input csv")
uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df)
    col1, col2 = st.columns(2)
    with col1:
        fig1 = plt.figure()
        sns.scatterplot(data=df,x='EstimatedSalary',y='Age',hue='Purchased')
    with col2:
        fig2 = plt.figure()
        st.subheader("Distribution of Age")
        sns.histplot(df.Age)
        st.pyplot(fig2)