import streamlit as st
import pandas as pd
from utils.api_client import call_api

def render():
    st.title("Eventos")
    with st.expander("Sobre esta página:"):
        st.write("""
            Esta seção está relacionada aos eventos configurados nas automações de marketing do RD Station.
            Para integrar o chatbot à automação, é necessário configurar um evento por aqui, definindo o nome do evento e a mensagem a ser enviada.\n
            O modelo da mensagem deve ser configurado através da plataforma da Meta, e o nome da mensagem deve ser informado aqui.\n
            Após feitas as configurações, é necessário inserir no fluxo de automação do RD Station o bloco "Enviar Leads para Integração" com a url "http://engtec.pythonanywhere.com/rd/leads/{nome-do-evento}".\n
            O nome do evento não deve possuir espaços, letras maiúsculas ou caracteres especiais.
            \n\n
            Funções disponíveis:
            - Ver Eventos: Lista todos os eventos cadastrados.    
            - Adicionar Evento: Adiciona um novo evento.
            - Remover Evento: Remove um evento existente
        """)
    option = st.selectbox("Escolha uma ação:", ["Ver Eventos", "Adicionar Evento", "Remover Evento"])
    response = call_api("/eventos", method="GET")
    eventos = []
    for evento in response:
        eventos.append(evento['evento'])

    if option == "Ver Eventos":
        if st.button("Listar Eventos"):
            response = call_api("/eventos", method="GET")
            if response and isinstance(response, list):  # Verifica se a resposta é uma lista
                if len(response) > 0:
                    # Converte a resposta em um DataFrame para exibir como tabela
                    df = pd.DataFrame(response)
                    df.reset_index(drop=True, inplace=True)
                    st.dataframe(df,hide_index=True)  # Exibição como tabela interativa
                else:
                    st.info("Nenhum evento encontrado.")
            else:
                st.warning("Nenhum evento encontrado.")
    
    elif option == "Adicionar Evento":
        evento = st.text_input("Nome do evento (não deve conter caracteres especiais)")
        mensagem = st.text_input("Nome da mensagem (mesmo nome cadastrado no Meta)")
        variavel = st.selectbox("Nome do cliente (em que lugar da mensagem será inserido o nome do cliente)", ["Cabeçalho","Corpo","Nenhuma"])
        if st.button("Adicionar Evento"):
            data = {"evento": evento, "mensagem": mensagem, "variavel": variavel}
            response = call_api("/eventos", method="POST", data=data)
            st.json(response)
    
    elif option == "Remover Evento":
        # Dropdown para escolher o evento
        evento = st.selectbox("Escolha o evento a ser removido:", eventos)
        data = {'evento': evento}
        if st.button("Remover evento"):
            response = call_api(f"/eventos", method="DELETE", data=data)
            st.json(response)