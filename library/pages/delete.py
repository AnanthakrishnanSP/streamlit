from numpy.ma.core import min_val

import streamlit as st

from library_db import booklistcreateretriveupdatedelete



n=st.number_input('ENTER id nnumber :',min_value=0)
btn=st.button("delete")

if btn:
    b=booklistcreateretriveupdatedelete()

    record=b.delete(n)
    print (record)

    if record:
        st.info('deletion success')
    else:
        st.error("no data fount")
        # st.error("No Record Fo")