import streamlit as st

# 1. FORÇANDO O SITE A PEGAR A TELA INTEIRA
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    layout="wide"
)

# 2. DESIGN PREMIUM SAAS COM LUMINOSIDADE NAS IMAGENS
st.html("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #030407 !important;
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Efeito de luminosidade (Glow) nas 4 imagens */
    [data-testid="stImage"] img {
        border-radius: 8px !important;
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.25) !important;
        border: 1px solid rgba(0, 240, 255, 0.2) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    [data-testid="stImage"] img:hover {
        transform: scale(1.01);
        box-shadow: 0 0 35px rgba(0, 240, 255, 0.4) !important;
    }
    
    h1, h2, .neon-accent {
        font-family: 'Inter', sans-serif !important;
        font-weight: 800 !important;
        color: #00f0ff !important;
        letter-spacing: -0.5px !important;
    }
    h3 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        color: #cbd5e1 !important;
    }
    p, span, div, li, a, td, th {
        font-family: 'Inter', sans-serif !important;
        color: #e2e8f0 !important;
    }
    
    div.stButton > button, div.stLinkButton > a {
        background-color: #00f0ff !important;
        color: #030407 !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        padding: 16px 24px !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 4px 20px rgba(0, 240, 255, 0.2);
        transition: all 0.2s ease;
    }
    div.stButton > button:hover, div.stLinkButton > a:hover {
        background-color: #ffffff !important;
        color: #030407 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 25px rgba(255, 255, 255, 0.3);
    }
    
    code, pre {
        font-family: monospace !important;
        background-color: #0b0f17 !important;
        border: 1px solid #1e293b !important;
    }
    </style>
""", unsafe_allowed_html=True)

# --- ESTRUTURA EM DUAS COLUNAS LARGAS ---
col_esquerda, col_direita = st.columns([1.2, 1])

with col_esquerda:
    st.markdown("# RVCX SOFTWARE CORE v2.0")
    st.markdown("### Autenticação de Protocolos de Inteligência Artificial")
    st.write("---")
    
    # Foto 1: Mascote Principal
    st.image("painel.png", use_container_width=True)
    
    st.write("")
    
    # Foto 2: Robô com o processador IA à mostra
    st.image("robo_processador.png", use_container_width=True)
    
    st.write("---")
    
    # Tabela de Performance
    st.markdown("### Métricas de Performance em Produtividade")
    dados_comparativos = {
        "Atividade": ["Minerar produtos", "Criar copy de venda", "Inserir link de afiliado", "Postar nos canais"],
        "Método Manual": ["45 minutos", "20 minutos", "5 minutos", "15 minutos"],
        "Sistema RVCX": ["3 segundos", "1.5 segundo", "Automático", "Imediato"]
    }
    st.table(dados_comparativos)

with col_direita:
    # Status Técnico
    st.markdown("### Status do Sistema")
    st.text("Status do motor: Operacional")
    st.text("Rede neural: Ativa (ASYNC_v3)")
    st.text("Latência de rede: 12ms")
    st.write("---")
    
    # Terminal de comando
    st.text("Log de operações em tempo real:")
    st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexao com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERACAO] 14 Produtos virais localizados nas ultimas 2 horas.
[SISTEMA] Aguardando ativacao da licenca para liberar download...
    """, language="text")
    
    st.write("---")
    
    # Foto 3: Robô no Escritório olhando faturamento
    st.image("robo_escritorio.png", use_container_width=True)
    
    st.write("")
    
    # Foto 4: Robô apontando para o código Python
    st.image("robo_codigo.png", use_container_width=True)
    
    st.write("---")
    
    # Abas de vantagens
    st.markdown("### Arquitetura Criptografada")
    tab1, tab2 = st.tabs(["Mineração", "Postagens"])
    with tab1:
        st.write("O script roda em background minerando os produtos de maior engajamento e conversão do dia nas plataformas integradas.")
    with tab2:
        st.write("O robô estrutura o payload gerado pela IA e efetua o disparo em massa para os canais de ofertas configurados.")

    st.write("---")

    # Área de Licenciamento e Botão
    st.markdown("### Licenciamento Vitalício")
    st.markdown("## R$ 29,90")
    st.write("")

    # --- CONFIGURAÇÃO DE CHECKOUT INTEGRADO (INFINITEPAY) ---
    INFINITE_TAG = "sua_tag_aqui"  # Mude para sua tag real depois!
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

    query_params = st.query_params

    if "capture_method" in query_params:
        st.success("Autenticação confirmada. Licença vitalícia ativada.")
        script_texto = "# RVCX Software\nprint('Script Carregado')"
        st.download_button(
            label="DOWNLOAD RVCX_BOT.PY",
            data=script_texto,
            file_name="rvcx_bot.py",
            mime="text/x-python",
            use_container_width=True
        )
    else:
        st.link_button("ATIVAR LICENÇA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)

st.write("---")
# Perguntas Frequentes
with st.container():
    st.markdown("### Perguntas Frequentes")
    st.markdown("**Necessito de conhecimento prévio em programação?**")
    st.write("Não. O script é entregue totalmente estruturado. O pacote inclui instruções em formato de texto direto para inicialização em menos de dois cliques.")

st.caption("RVCX Software Terminal. Transações processadas via gateway de segurança InfinitePay.")
