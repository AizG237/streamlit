import streamlit as st

st.markdown("<h1 style='text-align: center;'> USER REGISTRATION </h1>", unsafe_allow_html=True)

with st.form("Formulaire"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    coonfirm_password = st.text_input("Confirm Password", type="password")
    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    st_state = st.form_submit_button("Submit")
    if st_state :
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success(f"Welcome {f_name} {l_name}")
            st.pills("LABEL", options=("1 ","2 ","3 "))
p = st.sidebar.radio("Navigation", options=("Home","About","Contact"))