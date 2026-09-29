from streamlit import number_input, text_input

import streamlit as st

# text_input()
# number_input()

num1=st.number_input('enter number1',min_value=0)
num2=st.number_input('enter number2',min_value=0)



text=st.text_input('enter your text')



date=st.date_input("enter date")


# button

btn=st.button("click")


if btn:
    st.write(num1)
    st.write(num2)
    st.write(text)
    st.write(date)
