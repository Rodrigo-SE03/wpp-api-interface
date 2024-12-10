import streamlit as st

# Configuração inicial
st.set_page_config(page_title="Gerenciador de API", layout="wide",initial_sidebar_state="collapsed")

# Sidebar para navegação
menu = st.sidebar.selectbox(
    "Selecione a seção",
    ["EVO", "FAQ", "Contatos", "Conversas", "Fila"],
    index=0
)

# Roteamento para páginas
if menu == "FAQ":
    from paginas import faq
    faq.render()
elif menu == "EVO":
    from paginas import evo
    evo.render()
elif menu == "Contatos":
    from paginas import contatos
    contatos.render()
elif menu == "Conversas":
    from paginas import conversas
    conversas.render()
elif menu == "Fila":
    from paginas import fila
    fila.render()
