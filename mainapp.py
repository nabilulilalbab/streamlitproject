import streamlit as st
import random 
from khodam_module import SessionManager




Khodam = SessionManager()
st.title('cek khodam')
name = st.text_input('masukkan nama anda ')

if st.button('check'):
    if name :
        Khodam.spinner()
        st.write(f'hai {name}, khodam anda adalah : ')
        khodam_data = Khodam.get_khodam()
        if khodam_data:
            st.success(f'{random.choice(khodam_data)}', icon=random.choice(['😊','😂','🤣','😁','😎','👍']))
        else:
            st.error('Data khodam masih kosong!')
        if st.button('ulangi'):
            pass
    else:
        st.toast('please insert value',icon='👀')






