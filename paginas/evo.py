import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("EVO")

    option = st.selectbox("Escolha uma ação:", ["Ver Chats", "Remover Chat"])
    
    if option == "Ver Chats":
        if st.button("Listar Chats"):
            response = call_api("/chat", method="GET")
            if response and isinstance(response, list):  # Verifica se a resposta é uma lista
                if len(response) > 0:
                    # Converte a resposta em um DataFrame para exibir como tabela
                    df = pd.DataFrame(response)
                    df.reset_index(drop=True, inplace=True)
                    st.dataframe(df,hide_index=True)  # Exibição como tabela interativa
                else:
                    st.info("Nenhum chat encontrado.")
            else:
                st.error("Erro ao buscar chats.")
    
    elif option == "Remover Chat":
        faq_id = st.text_input("ID do Chat")
        data = {'id': faq_id}
        if st.button("Remover Chat"):
            response = call_api(f"/chat", method="DELETE", data=data)
            st.json(response)
