import streamlit as st
from library_db import booklistcreateretriveupdatedelete

st.title("Blood Donor Management System")

b=booklistcreateretriveupdatedelete

tab1,tab2,tab3,tab4,tab5(['add','read','retrieve','update','delete'])

with tab1:
    st.write('add')

with tab2:
    st.write('read')

with tab3:
    st.write('retrieve')

with tab4:
    st.write('update')

with tab5:
    st.write('delete')