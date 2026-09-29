from numpy.ma.core import min_val

import streamlit as st

from library_db import booklistcreateretriveupdatedelete



n=st.number_input('ENTER id nnumber :',min_value=0)
btn=st.button("search")

if btn:
    b=booklistcreateretriveupdatedelete()

    record=b.retrive(n)
    print (record)

    if record:
        st.write("Title", record[1])
        st.write( "Author", record[2])
        st.write( "Price", record[3])
        st.write( "Pages", record [4])
        st.write( "Language" , record[5])
    else:

        st.error("No Record Fo")