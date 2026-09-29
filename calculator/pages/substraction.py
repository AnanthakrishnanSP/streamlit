import streamlit as st
st.header("substraction")

num1=st.number_input("enter number1",min_value=0)
num2=st.number_input("enter number2",min_value=0)

btn=st.button("diff")
if btn:
    st.write("diff =",num1-num2)