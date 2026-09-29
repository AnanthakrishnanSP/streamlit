import streamlit as st

from blood_db import DonorCreateRetrieveUpdateDelete

st.title("Add Donor")

name = st.text_input("Enter donor name:")

blood_group = st.selectbox(
    "Select blood group:",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("Enter phone number:")

city = st.text_input("Enter city:")

last_donation = st.date_input("Last donation date:")

btn = st.button("ADD DONOR")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    record = b.create(
        name,
        blood_group,
        phone,
        city,
        last_donation
    )

    if record:
        st.success("Donor added successfully")
    else:
        st.error("Donor not added")