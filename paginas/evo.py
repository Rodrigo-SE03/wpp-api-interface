import streamlit as st
import requests
from urllib.parse import quote
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("EVO")

    option = st.selectbox("Escolha uma ação:", ["Ver Chats", "Listar Conversas", "Remover Chat"])
    
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
    
    elif option == "Listar Conversas":
        response = call_api("/history", method="GET")
        if response and isinstance(response, list):
            if len(response) > 0:
                st.write("Lista de Arquivos:")
                
                # Itera sobre os arquivos para criar a tabela personalizada
                for index, arquivo in enumerate(response):
                    col1, col2, col3 = st.columns([3, 1, 1])  # Define o layout das colunas
                    arquivo = arquivo.replace("%", " ") 
                    col1.write(arquivo)
                    if col2.button("Baixar", key=f"baixar-{index}"):
                        st.session_state["download"] = arquivo
                        print('here')
                        st.write(f"Baixando o arquivo: {arquivo}")
                        arquivo_codificado = quote(arquivo) 
                        download_url = call_api(f"/history/download/{arquivo_codificado}", method="GET")
                        print(download_url)
                        response = requests.get(download_url['url'])
                        with open(arquivo, 'wb') as f:
                            f.write(response.content)
                        st.write("Download concluído.")

                    if col3.button("Apagar", key=f"apagar-{index}"):
                        st.write(f"Apagando o arquivo: {arquivo}")
            else:
                st.info("Nenhuma conversa encontrada.")
        else:
            st.error("Erro ao buscar conversas.")
                    
    
    elif option == "Remover Chat":
        faq_id = st.text_input("ID do Chat")
        data = {'id': faq_id}
        if st.button("Remover Chat"):
            response = call_api(f"/chat", method="DELETE", data=data)
            st.json(response)
