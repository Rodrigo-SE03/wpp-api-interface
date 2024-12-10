import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("Fila")

    option = st.selectbox("Escolha uma ação:", ["Ver Fila", "Remover da Fila"])
    
    if option == "Ver Fila":
        if st.button("Listar Fila"):
            response = call_api("/fila", method="GET")
            if response and isinstance(response, list):  # Verifica se a resposta é uma lista
                if len(response) > 0:
                    # Converte a resposta em um DataFrame para exibir como tabela
                    df = pd.DataFrame(response)
                    df.reset_index(drop=True, inplace=True)
                    st.dataframe(df,hide_index=True)  # Exibição como tabela interativa
                else:
                    st.info("Nenhuma pessoa na fila.")
            else:
                st.error("Erro ao ver a fila.")
    
    elif option == "Remover da Fila":
        numero = st.text_input("Número de Telefone",placeholder='556298299370')
        data = {'numero': numero}
        if st.button("Remover da Fila"):
            response = call_api(f"/conversas", method="DELETE", data=data)
            st.json(response)
