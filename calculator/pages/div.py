import streamlit as st
st.header("division")

num1=st.number_input("enter number1",min_value=0)
num2=st.number_input("enter number2",min_value=0)

btn=st.button("divide")
if btn:
    st.write("div =",num1/num2)