import streamlit as st

from blood_db import DonorCreateRetrieveUpdateDelete

st.title("Update Donor")

n = st.number_input(
    "Enter donor ID:",
    min_value=1,)

name = st.text_input("Enter donor name:")

blood_group = st.selectbox(
    "Select blood group:",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("Enter phone number:")

city = st.text_input("Enter city:")

last_donation = st.date_input("Last donation date:")

btn = st.button("UPDATE")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    record = b.update(
        n,
        name,
        blood_group,
        phone,
        city,
        last_donation
    )

    if record:
        st.success("Donor updated successfully")
    else:
        st.error("Donor not found")