import streamlit as st
import time


class SessionManager:
    def __init__(self):
        if 'khodam_data' not in st.session_state:
            st.session_state['khodam_data'] = []

    def get_khodam(self):
        return st.session_state['khodam_data']

    def add_khodam(self, value):
        st.session_state['khodam_data'].append(value)

    def remove_khodam(self, value):
        st.session_state['khodam_data'].remove(value)
    def cook_breakfast(self):
        msg = st.toast('Tunggu Sebentar...')
        time.sleep(1)
        msg.toast('......')
        time.sleep(1)
        msg.toast('Ready!', icon = "👌")
    def spinner(self):
        with st.spinner('Wait for it...'):
            time.sleep(5)