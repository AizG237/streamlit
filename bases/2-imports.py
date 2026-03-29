import streamlit as st

st.title('Uploading file')

image = st.file_uploader("** PLEASE UPLOAD AN IMAGE", type=['png','jpg'])

if image:
    st.image(image)

video = image = st.file_uploader("** PLEASE UPLOAD A VIDEO", type=['mp4','avi'])
if video :
    st.video(video)

# SLIDER
st.slider("** This is a lider**", min_value=10, max_value=250, value=1, step=5)

#input texte
st.text_area("Courte description")

#
st.date_input("Entrer une date")