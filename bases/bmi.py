import streamlit as st

st.title(" BMI CALCULATOR")

weight = st.number_input("Entrer votre poids (kg)")
statut = st.radio("Selectionner le format de la taille",("cm","metres","pieds"))
try :
    if statut == "cm":
        height = st.number_input('Centimetres')
        bmi = weight/((height/100)**2)
        bmi = round(bmi)
    elif statut == "metres":
        height = st.number_input('Metres')
        bmi = weight/(height**2)
        bmi = round(bmi)
    elif statut== "pieds":
        height = st.number_input('Pieds')
        bmi = weight/((height/3.28)**2)
        bmi = round(bmi)
    
except Exception as e:
    print(" Erreur division 0")


if(st.button('Calcule BMI')) :
    st.write(f"Ton BMI est de {bmi:.2f}")

    if bmi < 18.5 :
        st.error("Tu es en sous-poids")
    elif bmi > 18.5 and bmi < 25 :
        st.info("Tu es en bonne sante")
    elif bmi > 25:
        st.warning("Va a la salle de sport bro")
    else:
        st.error("Tu es un alien")