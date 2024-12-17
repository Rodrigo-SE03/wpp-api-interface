import streamlit as st
from time import sleep
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
                st.warning("Nenhum chat encontrado.")
    
    elif option == "Listar Conversas":
        response = call_api("/history", method="GET")
        if response and isinstance(response, list):
            if len(response) > 0:
                st.write("Lista de Arquivos:")
                
                # Itera sobre os arquivos para criar a tabela personalizada
                for index, arquivo in enumerate(response):
                    col1, col2, col3 = st.columns([3, 1, 1])  # Define o layout das colunas
                    arquivo_display = arquivo.replace("_", " ")
                    col1.write(arquivo_display)
                    if col2.download_button(
                        label="Baixar",
                        data=call_api(f"/history/{arquivo}", method="GET"),  # Obtém o conteúdo diretamente
                        file_name=arquivo,  # Nome do arquivo para download
                        mime="text/plain",  # Tipo MIME do arquivo
                        key=f"baixar-{index}"
                    ):
                        st.success("Download concluído.")

                    if col3.button("Apagar", key=f"apagar-{index}"):
                        response = call_api(f"/history/{arquivo}", method="DELETE")
                        st.error(f"Arquivo apagado: {arquivo}")
                        sleep(1)
                        st.rerun()
            else:
                st.info("Nenhuma conversa encontrada.")
        else:
            st.warning("Nenhuma conversa encontrada.")
                    
    
    elif option == "Remover Chat":
        faq_id = st.text_input("ID do Chat")
        data = {'id': faq_id}
        if st.button("Remover Chat"):
            response = call_api(f"/chat", method="DELETE", data=data)
            st.json(response)
