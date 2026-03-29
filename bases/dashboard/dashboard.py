import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#uploaded_file = st.file_uploader("Choose a file", type="csv")
#if uploaded_file :  
    
#df = pd.read_csv(uploaded_file)
df = pd.read_csv("bank.csv")
st.set_page_config(page_title="Real time Science Dashboard", page_icon=":bar_chart:", layout="wide")
    
st.title("Real Time/Live DataAnalysisi")
job_filter = st.selectbox("Select Job", pd.unique(df["job"]))
    
#Creer un endroit pour le filtre
df = df[df["job"] == job_filter]
    
#INDICATEURS
avg_age = np.mean(df["age"])
count_married = int(df[df["marital"] == "married"]["marital"].count())
balance = np.mean(df["balance"])
    
kpi1, kpi2, kpi3 = st.columns(3)
    
kpi1.metric(label="Age", value=round(avg_age), delta=round(avg_age))
kpi2.metric(label="Married Count", value=int(count_married), delta=round(count_married))
kpi3.metric(label="Balance $", value=f"${round(balance, 2)}")
    
#GRAPHIQUES
col1, col2 = st.columns(2)
with col1 : 
st.markdown("### FIRST CHART")
fig1 = plt.figure()
sns.barplot(data=df, x="marital", y="age",palette="viridis")
st.pyplot(fig1)
    
with col2 :
st.markdown("### SECOND CHART")
fig2 = plt.figure()
sns.histplot(data=df,x="age")
st.pyplot(fig2)
    
st.markdown("### DETAILLED DATA VIEW")
st.dataframe(df)
