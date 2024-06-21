import streamlit as st
from mainapp import Khodam


st.title('add khodam')
add = st.text_input('masukkan nama khodam',key='unique_name_update')
if st.button('add'):
    Khodam.add_khodam(add)
    st.toast(f'add {add} succesfully')

st.table(Khodam.get_khodam())

st.title('Remove khodam')
delete = st.text_input('masukkan nama khodam',key='unique_name_remove')
if st.button('Remove'):
    Khodam.remove_khodam(delete)
    st.toast(f'remove {delete} succesfully')








