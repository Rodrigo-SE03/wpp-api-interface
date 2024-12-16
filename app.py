import streamlit as st
from utils.api_client import call_api

# Configuração inicial
st.set_page_config(page_title="Gerenciador de API", layout="wide",initial_sidebar_state="collapsed")

# Função para verificar conversas ativas
def verificar_conversas_ativas():
    contatos = call_api("/contatos", method="GET")  # Substitua pelo endpoint correto
    nenhuma = True
    for contato in contatos:
        if contato["em_conversa"] == 1:
            st.warning(f"Conversa ativa no setor {contato['setor']}")
            nenhuma = False
    if nenhuma:
        st.info("Nenhuma conversa ativa.")

# Botão para verificar conversas ativas
if st.button("Verificar Conversas Ativas"):
    verificar_conversas_ativas()

# Sidebar para navegação
menu = st.sidebar.selectbox(
    "Selecione a seção",
    ["Contatos", "FAQ", "EVO", "Conversas", "Fila"],
    index=0
)

# Roteamento para páginas
if menu == "Contatos":
    from paginas import contatos
    contatos.render()
elif menu == "FAQ":
    from paginas import faq
    faq.render()
elif menu == "EVO":
    from paginas import evo
    evo.render()
elif menu == "Conversas":
    from paginas import conversas
    conversas.render()
elif menu == "Fila":
    from paginas import fila
    fila.render()
