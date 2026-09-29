import streamlit as st

from blood_db import DonorCreateRetrieveUpdateDelete

st.title("Delete Donor")

n = st.number_input(
    "Enter donor ID:",
    min_value=1,
)

btn = st.button("DELETE")

if btn:

    b = DonorCreateRetrieveUpdateDelete()

    record = b.delete(n)

    if record:
        st.success("Donor deleted successfully")
    else:
        st.error("Donor not found")