import streamlit as st
st.header("mult")

num1=st.number_input("enter number1",min_value=0)
num2=st.number_input("enter number2",min_value=0)

btn=st.button("mult")
if btn:
    st.write("mult =",num1*num2)