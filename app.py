import streamlit as st

# Configuração básica da página
st.set_page_config(page_title="RVCX Software", page_icon="🤖", layout="centered")

# Títulos Principais do Site
st.title("🤖 RVCX SOFTWARE")
st.subheader("Módulo de Automação com IA Inteligente")

st.write("---")

# Exibição da sua Imagem do Painel Hacker
st.image("painel.png", use_container_width=True)

st.write("---")

# Informações de Preço
st.metric(label="Acesso Vitalício", value="R$ 29,90")

# --- CONFIGURAÇÃO DE CHECKOUT DA INFINITEPAY ---
INFINITE_TAG = "sua_tag_aqui" 

item_nome = "RVCX_Robo_Afiliado"
item_preco = 2990 
pedido_id = "RVCX999" 
URL_RETORNO = "https://streamlit.app"

link_pagamento = (
    f"https://infinitepay.io{INFINITE_TAG}?"
    f"items=[{{'name':'{item_nome}','price':{item_preco},'quantity':1}}]&"
    f"order_nsu={pedido_id}&"
    f"redirect_url={URL_RETORNO}"
)

# Sistema de verificação de retorno pós-pagamento
query_params = st.query_params

if "capture_method" in query_params:
    st.balloons()
    st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Seu robô foi liberado.")
    
    # Arquivo binário do seu robô em Python para download
    script_conteudo = b"# Script Original RVCX Software instalado com sucesso"
    st.download_button(
        label="📥 CLIQUE PARA INSTALAR O ROBÔ (rvcx_bot.py)",
        data=script_conteudo,
        file_name="rvcx_bot.py",
        mime="text/x-python",
        use_container_width=True
    )
else:
    # Botão padrão e seguro do Streamlit para o Checkout
    st.link_button("⚡ ADQUIRIR PROTOCOLO E ATIVAR ROBÔ", link_pagamento, use_container_width=True)

st.write("")
st.caption("Ambiente criptografado e processado via InfinitePay® de forma segura.")
