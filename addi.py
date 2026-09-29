import streamlit as st
num1=st.number_input("enter number1",min_value=0)
num2=st.number_input("enter number2",min_value=0)

btn=st.button("Add")
if btn:
    st.write("sum =",num1+num2)