import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("Contatos")

    option = st.selectbox("Escolha uma ação:", ["Ver Contatos", "Atualizar Contato", "Encerrar Conversa", "Adicionar Contato", "Remover Contato"])
    
    if option == "Ver Contatos":
        if st.button("Listar Contatos"):
            response = call_api("/contatos", method="GET")
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
    
    elif option == 'Atualizar Contato':
        setor  = st.text_input("Setor")
        telefone_responsavel = st.text_input("Telefone do Responsável", placeholder='556298299370')
        nome_responsavel = st.text_input("Nome do Responsável")
        subtopicos = st.text_area("Subtópicos", placeholder="Subtópico1,Subtópico2,Subtópico3,Subtópico4")
        data = {'setor': setor, 'telefone_responsavel': telefone_responsavel, 'nome_responsavel': nome_responsavel, 'subtopicos': subtopicos}
        if st.button("Atualizar Contato"):
            response = call_api(f"/contatos", method="PUT", data=data)
            st.json(response)

    elif option == "Encerrar Conversa":
        telefone_responsavel = st.text_input("Telefone do Responsável", placeholder='556298299370')
        data = {'numero': telefone_responsavel}
        if st.button("Encerrar Conversa"):
            response = call_api(f"/contatos", method="PATCH", data=data)
            st.json(response)
    
    elif option == "Adicionar Contato":
        setor  = st.text_input("Setor")
        telefone_responsavel = st.text_input("Telefone do Responsável", placeholder='556298299370')
        nome_responsavel = st.text_input("Nome do Responsável")
        subtopicos = st.text_area("Subtópicos", placeholder="Subtópico1,Subtópico2,Subtópico3,Subtópico4")
        data = {'setor': setor, 'telefone_responsavel': telefone_responsavel, 'nome_responsavel': nome_responsavel, 'subtopicos': subtopicos}
        if st.button("Adicionar Contato"):
            response = call_api(f"/contatos", method="POST", data=data)
            st.json(response)

    elif option == "Remover Contato":
        setor = st.text_input("Setor")
        data = {'setor': setor}
        if st.button("Remover Contato"):
            response = call_api(f"/contatos", method="DELETE", data=data)
            st.json(response)
