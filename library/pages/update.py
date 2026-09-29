from numpy.ma.core import min_val

import streamlit as st
st.title("update")
from library_db import booklistcreateretriveupdatedelete



n=st.number_input('ENTER id nnumber :',min_value=0)
n1=st.text_input('ENTER title :')
n2=st.text_input('ENTER author :')
n3=st.number_input('ENTER price :')
n4=st.number_input('ENTER pages :',min_value=0)
n5=st.text_input('ENTER language :',)


btn=st.button("update")

if btn:
    b=booklistcreateretriveupdatedelete()

    record=b.update(n,n1,n2,n3,n4,n5)
    print (record)

    if record:
        st.info('updated')
    else:
        st.error("no record")
        # st.error("No Record Fo")