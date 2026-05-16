import streamlit as st

# Configuração da página (Modo Escuro e Centralizado)
st.set_page_config(page_title="RVCX Software", page_icon="🤖", layout="centered")

# Estilização em uma linha limpa para evitar quebras no servidor
st.markdown("<style>.stApp { background-color: #0d0e15; color: #e2e8f0; } .neon-title { font-size: 42px; font-weight: 800; color: #00f0ff; text-shadow: 0 0 10px #00f0ff; text-align: center; font-family: monospace; } .neon-subtitle { font-size: 16px; color: #ff007f; text-align: center; margin-bottom: 25px; letter-spacing: 2px; font-weight: bold; } .price-tag { font-size: 32px; color: #00ff66; text-align: center; font-weight: bold; margin: 25px 0; }</style>", unsafe_allowed_html=True)

# Títulos Principais do Site
st.markdown('<p class="neon-title">RVCX SOFTWARE</p>', unsafe_allowed_html=True)
st.markdown('<p class="neon-subtitle">MÓDULO DE AUTOMAÇÃO IA INTELIGENTE</p>', unsafe_allowed_html=True)

# Exibição da Imagem do Painel
st.image("painel.png", use_container_width=True)

st.write("---")

# Informações de Preço
st.markdown('<p class="price-tag">Acesso Vitalício: R$ 29,90</p>', unsafe_allowed_html=True)

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

# Sistema de verificação de retorno
query_params = st.query_params

if "capture_method" in query_params:
    st.balloons()
    st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Seu robô foi liberado.")
    
    script_conteudo = b"# Script Original RVCX Software instalado com sucesso"
    st.download_button(
        label="📥 CLIQUE PARA INSTALAR O ROBÔ (rvcx_bot.py)",
        data=script_conteudo,
        file_name="rvcx_bot.py",
        mime="text/x-python",
        use_container_width=True
    )
else:
    # Botão de pagamento limpo em HTML
    st.markdown(
        f'<a href="{link_pagamento}" target="_blank" style="text-decoration: none;">'
        f'<button style="width: 100%; background-color: #00f0ff; color: #0d0e15; font-weight: bold; '
        f'padding: 18px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; '
        f'box-shadow: 0 0 20px #00f0ff; letter-spacing: 1px;">'
        f'⚡ ADQUIRIR PROTOCOLO E ATIVAR ROBÔ'
        f'</button></a>',
        unsafe_allowed_html=True
    )

st.write("")
st.caption("Ambiente seguro processado via criptografia de ponta a ponta InfinitePay®.")
