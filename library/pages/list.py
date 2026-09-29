from numpy.core import records

import streamlit as st

from library_db import booklistcreateretriveupdatedelete
b=booklistcreateretriveupdatedelete()
records=b.list()
print(records)

if records:
    st.table(records)
else:
    st.info('no tables')