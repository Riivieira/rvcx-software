import streamlit as st

# Configuração da página (Modo Escuro e Centralizado)
st.set_page_config(page_title="RVCX Software", page_icon="🤖", layout="centered")

# Estilização CSS customizada (Efeito Cyberpunk Neon)
st.markdown("""
    <style>
    .stApp { background-color: #0d0e15; color: #e2e8f0; }
    .neon-title { font-size: 42px; font-weight: 800; color: #00f0ff; text-shadow: 0 0 10px #00f0ff; text-align: center; font-family: monospace; margin-bottom: 5px; }
    .neon-subtitle { font-size: 16px; color: #ff007f; text-align: center; margin-bottom: 25px; letter-spacing: 2px; font-weight: bold; }
    .price-tag { font-size: 32px; color: #00ff66; text-align: center; font-weight: bold; margin: 25px 0; text-shadow: 0 0 5px rgba(0,255,102,0.3); }
    </style>
""", unsafe_allowed_html=True)

# Títulos Principais do Site
st.markdown('<p class="neon-title">RVCX SOFTWARE</p>', unsafe_allowed_html=True)
st.markdown('<p class="neon-subtitle">MÓDULO DE AUTOMAÇÃO IA INTELIGENTE</p>', unsafe_allowed_html=True)

# 🖼️ EXIBIÇÃO DA SUA IMAGEM DO PAINEL (Carrega direto do seu GitHub)
st.image("painel.png", use_container_width=True)

st.write("---")

# Informações de Valor e Preço
st.markdown('<p class="price-tag">Acesso Vitalício: R$ 29,90</p>', unsafe_allowed_html=True)

# --- CONFIGURAÇÃO DE CHECKOUT DA INFINITEPAY ---
# IMPORTANTE: No futuro, mude essa tag para o seu usuário do app da InfinitePay
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

# Captura se o usuário voltou da tela de pagamento aprovado
query_params = st.query_params

if "capture_method" in query_params:
    st.balloons()
    st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Seu robô foi liberado.")
    
    # Código simulado do robô para download instantâneo após a compra
    script_conteudo = b"# Script Original RVCX Software instalado com sucesso"
    st.download_button(
        label="📥 CLIQUE PARA INSTALAR O ROBÔ (rvcx_bot.py)",
        data=script_conteudo,
        file_name="rvcx_bot.py",
        mime="text/x-python",
        use_container_width=True
    )
else:
    # Exibe o botão de pagamento estilizado em Neon Azul
    st.markdown(
        f'<a href="{link_pagamento}" target="_blank" style="text-decoration: none;">'
        f'<button style="width: 100%; background-color: #00f0ff; color: #0d0e15; font-weight: bold; '
        f'padding: 18px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; '
        f'box-shadow: 0 0 20px #00f0ff; letter-spacing: 1px; transition: 0.3s;">'
        f'⚡ ADQUIRIR PROTOCOLO E ATIVAR ROBÔ'
        f'</button></a>',
        unsafe_allowed_html=True
    )

st.write("")
st.caption("Ambiente seguro processado via criptografia de ponta a ponta InfinitePay®.")
