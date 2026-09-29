import streamlit as st

from blood_db import DonorCreateRetrieveUpdateDelete

st.title("Retrieve Donors")

b = DonorCreateRetrieveUpdateDelete()

records = b.retrieve()

if records:
    st.table(records)
else:
    st.info("No donors found")