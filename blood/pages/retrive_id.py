import streamlit as st

from blood_db import DonorCreateRetrieveUpdateDelete

st.title("Search Donor")

n = st.number_input(
    "Enter donor ID:",
    min_value=1,
    step=1
)

btn = st.button("SEARCH")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    records = b.retrieve_by_id(n)

    if records:
        st.table(records)
    else:
        st.error("Donor not found")