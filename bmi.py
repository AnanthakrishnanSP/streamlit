import streamlit as st

w=st.number_input("enter weight in kg",min_value=1)
h=st.number_input("enter height in cm",min_value=1)

btn=st.button("calculate BMI")
if btn:
    bmi=w / ((h/100)**2)
    st.write('BMI value=',bmi)
    if bmi <18.5:
        st.info('underweight')
    elif bmi >=18.5 and bmi<25:
        st.success('normal')
    elif bmi >=25 and bmi <30:
        st.warning('overweight')
    elif bmi>30:
        st.error('obesity - poda thadiyaa')