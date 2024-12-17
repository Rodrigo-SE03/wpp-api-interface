import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("FAQ")

    option = st.selectbox("Escolha uma ação:", ["Ver Itens", "Adicionar Item", "Remover Item"])
    
    if option == "Ver Itens":
        if st.button("Listar FAQ"):
            response = call_api("/faq", method="GET")
            if response and isinstance(response, list):  # Verifica se a resposta é uma lista
                if len(response) > 0:
                    # Converte a resposta em um DataFrame para exibir como tabela
                    df = pd.DataFrame(response)
                    df.reset_index(drop=True, inplace=True)
                    st.dataframe(df,hide_index=True)  # Exibição como tabela interativa
                else:
                    st.info("Nenhum item encontrado no FAQ.")
            else:
                st.warning("Nenhum item encontrado no FAQ.")
    
    elif option == "Adicionar Item":
        pergunta = st.text_input("Pergunta")
        resposta = st.text_area("Resposta")
        categoria = st.selectbox("Categoria", ["Mercado Livre de Energia","Geração de Energia"])
        if st.button("Adicionar FAQ"):
            data = {"pergunta": pergunta, "resposta": resposta, "categoria": categoria}
            response = call_api("/faq", method="POST", data=data)
            st.json(response)
    
    elif option == "Remover Item":
        faq_id = st.text_input("ID do item")
        data = {'id': faq_id}
        if st.button("Remover item"):
            response = call_api(f"/faq", method="DELETE", data=data)
            st.json(response)
