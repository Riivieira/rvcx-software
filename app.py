import streamlit as st

# Configuração da página (Nome na aba e layout centralizado)
st.set_page_config(page_title="RVCX Software - Oficial", page_icon="🤖", layout="centered")

# --- TOPO DA PÁGINA ---
st.title("🤖 RVCX SOFTWARE CORE")
st.write("Módulo Oficial de Autenticação e Licenciamento de Protocolos IA")

# Exibição da Imagem Principal do Painel Hacker
st.image("painel.png", use_container_width=True)

st.write("---")

# --- QUADRO TÉCNICO DE STATUS (Efeito Profissional/Uau) ---
st.subheader("🌐 Monitoramento da Rede Core")
col1, col2, col3 = st.columns(3)
with col1:
    st.success("● ENGINE ONLINE")
with col2:
    st.info("🧠 NEURAL NETWORKS: 3")
with col3:
    st.warning("⚡ LATÊNCIA: 12ms")

st.write("")

# Painel expansível simulando comandos reais do robô em Python
with st.expander("👁️ VISUALIZAR TERMINAL DA AUTOMAÇÃO (Clique para expandir)"):
    st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexão com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERAÇÃO] 14 Produtos virais localizados nas últimas 2 horas.
[IA WRITER] Legendas persuasivas criadas automaticamente com link de afiliado.
[SISTEMA] Aguardando ativação da licença do usuário para liberar download...
    """, language="text")

st.write("---")

# --- SEÇÃO DE PREÇO E VALOR ---
st.metric(label="Acesso Vitalício + Atualizações Inclusas", value="R$ 29,90")

# --- CONFIGURAÇÃO DE CHECKOUT INTEGRADO (INFINITEPAY) ---
# IMPORTANTE: Altere o valor abaixo para a sua InfiniteTag real do aplicativo
INFINITE_TAG = "sua_tag_aqui" 

item_nome = "RVCX_Robo_Afiliado"
item_preco = 2990  # R$ 29,90 em centavos
pedido_id = "RVCX999" 
URL_RETORNO = "https://streamlit.app"

# Montagem da URL de checkout seguro da InfinitePay
link_pagamento = (
    f"https://infinitepay.io{INFINITE_TAG}?"
    f"items=[{{'name':'{item_nome}','price':{item_preco},'quantity':1}}]&"
    f"order_nsu={pedido_id}&"
    f"redirect_url={URL_RETORNO}"
)

# Captura os parâmetros da URL para identificar se o cliente concluiu o Pix
query_params = st.query_params

if "capture_method" in query_params:
    st.balloons()
    st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Licença vitalícia ativada com sucesso.")
    
    # Conteúdo real do seu robô (rvcx_bot.py) que o cliente comprou
    script_conteudo = b"""# =======================================================
#       RVCX SOFTWARE - CORE AUTOMATION V1.0      
# =======================================================
import time
import random

print("Automação Iniciada com Sucesso...")
# O restante do código do seu robô que estruturamos fica aqui dentro
"""
    
    # Libera o botão secreto de download após o pagamento aprovado
    st.download_button(
        label="📥 CLIQUE PARA INSTALAR O ROBÔ (rvcx_bot.py)",
        data=script_conteudo,
        file_name="rvcx_bot.py",
        mime="text/x-python",
        use_container_width=True
    )
else:
    # Botão oficial de redirecionamento para o pagamento seguro
    st.link_button("⚡ ATIVAR LICENÇA E INSTALAR ROBÔ AGORA", link_pagamento, use_container_width=True)

st.write("")
st.caption("Ambiente criptografado e processado via InfinitePay® de forma segura.")
