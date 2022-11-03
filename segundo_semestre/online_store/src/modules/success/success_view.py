# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


class SuccessView():
    def __init__(self) -> None:
        st.title('Parabéns, você finalizou sua compra!!!')
        st.button('Fazer mais compras', on_click=self.backToHome)

    def backToHome(self):
        st.session_state['page'] = 'home'
