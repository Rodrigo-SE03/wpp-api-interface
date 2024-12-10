import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("Conversas")

    option = st.selectbox("Escolha uma ação:", ["Ver Conversas", "Remover Conversa"])
    
    if option == "Ver Conversas":
        if st.button("Listar Conversas"):
            response = call_api("/conversas", method="GET")
            if response and isinstance(response, list):  # Verifica se a resposta é uma lista
                if len(response) > 0:
                    # Converte a resposta em um DataFrame para exibir como tabela
                    df = pd.DataFrame(response)
                    df.reset_index(drop=True, inplace=True)
                    st.dataframe(df,hide_index=True)  # Exibição como tabela interativa
                else:
                    st.info("Nenhuma conversa encontrada.")
            else:
                st.error("Erro ao buscar conversas.")
    
    elif option == "Remover Conversa":
        faq_id = st.text_input("ID da Conversa")
        data = {'id': faq_id}
        if st.button("Remover Conversa"):
            response = call_api(f"/conversas", method="DELETE", data=data)
            st.json(response)
