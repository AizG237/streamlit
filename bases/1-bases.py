import streamlit as st
import pandas as pd
st.title("STREAMLIT WEB APP")

st.metric(label="wind speed", value="120ms-1",delta="-1.4ms-1")
tabel = pd.DataFrame({"Column1":[1,2,3], "Column2":[9,8,7]})

# st.image("stream.jpg")

state = st.checkbox('Checbox', value=True)
if state :
    st.write("Box checked")
else :
    st.write("Box unchecked")

radio_btn = st.radio("Radio Button", ("US","UK","Canada"))
btn = st.button("Click Me")
select = st.selectbox("select box",("Audi","BMW","MUSTANG"))
multi_select = st.multiselect("Multibox", ('APPLE','SAMSUNG','HUAWEI','HONOR'))