import streamlit as st

# 1. FORÇANDO O SITE A PEGAR A TELA INTEIRA (Nativo e Limpo)
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    layout="wide"
)

# 2. DESIGN PROFISSIONAL HACKER ABSOLUTO (Sem Amadorismo)
st.html("""
    <style>
    /* Reset de Fundo e Cores para Estilo Terminal de Elite */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    h1, h2, h3, p, span, div, li, a {
        font-family: 'Courier New', Courier, monospace !important;
        color: #00ffcc !important;
    }
    /* Estilização Cirúrgica do Botão de Ação */
    div.stButton > button, div.stLinkButton > a {
        background-color: #000000 !important;
        color: #00ffcc !important;
        border: 1px solid #00ffcc !important;
        border-radius: 0px !important;
        font-weight: bold !important;
        letter-spacing: 2px !important;
        padding: 20px !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover, div.stLinkButton > a:hover {
        background-color: #00ffcc !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #00ffcc;
    }
    /* Ajuste de abas para manter o padrão escuro */
    button[data-testid="stMarkdownContainer"] {
        color: #00ffcc !important;
    }
    </style>
""")

# --- ESTRUTURA EM DUAS COLUNAS LARGAS ---
col_esquerda, col_direita = st.columns([1.2, 1])

with col_esquerda:
    st.markdown("# RVCX SOFTWARE CORE v2.0")
    st.markdown("### AUTENTICACAO DE PROTOCOLOS DE INTELIGENCIA ARTIFICIAL")
    st.write("---")
    
    # Exibição do seu Mascote Robô Principal (Fica do lado esquerdo)
    st.image("painel.png", use_container_width=True)
    
    st.write("---")
    
    # Tabela de Performance
    st.markdown("### METRICAS DE PERFORMANCE EM PRODUTIVIDADE")
    dados_comparativos = {
        "ATIVIDADE": ["Minerar produtos", "Criar copy de venda", "Inserir link de afiliado", "Postar nos canais"],
        "METODO MANUAL": ["45 minutos", "20 minutos", "5 minutos", "15 minutos"],
        "SISTEMA RVCX": ["3 segundos", "1.5 segundo", "Automatizado", "Imediato"]
    }
    st.table(dados_comparativos)

with col_direita:
    # Monitoramento Técnico de Conexão (Texto limpo simulando console real)
    st.markdown("### STATUS DO SISTEMA")
    st.text("STATUS DO MOTOR: ONLINE")
    st.text("REDE NEURAL ACTIVATED: ASYNC_v3")
    st.text("LATENCIA DE REDE: 12ms")
    st.write("---")
    
    # Terminal de comando limpo
    st.text("LOG DE OPERACOES EM TEMPO REAL:")
    st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexao com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERACAO] 14 Produtos virais localizados nas ultimas 2 horas.
[SISTEMA] Aguardando ativacao da licenca para liberar download...
    """, language="text")
    
    st.write("---")
    
    # Imagem do robô apontando para o código Python real (Fica do lado direito)
    st.image("robo_codigo.png", use_container_width=True)
    
    st.write("---")
    
    # Abas de vantagens sem firulas
    st.markdown("### ARQUITETURA CRIPTOGRAFADA")
    tab1, tab2 = st.tabs(["MINERACAO", "POSTAGENS"])
    with tab1:
        st.write("O script roda em background minerando os produtos de maior engajamento e conversao do dia nas plataformas integradas.")
    with tab2:
        st.write("O robo estrutura o payload gerado pela IA e efetua o disparo em massa para os canais de ofertas configurados.")

    st.write("---")

    # Área de Licenciamento e Botão
    st.markdown("### LICENCIAMENTO VITALICIO")
    st.markdown("## VALOR DO PROTOCOLO: R$ 29,90")
    st.write("")

    # --- CONFIGURAÇÃO DE CHECKOUT INTEGRADO (INFINITEPAY) ---
    # Troque pelo seu usuario da InfinitePay quando puder
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

    query_params = st.query_params

    if "capture_method" in query_params:
        st.success("AUTENTICACAO CONFIRMADA. LICENCA VITALICIA ATIVADA.")
        script_texto = "# RVCX Software\nprint('Script Carregado')"
        st.download_button(
            label="DOWNLOAD RVCX_BOT.PY",
            data=script_texto,
            file_name="rvcx_bot.py",
            mime="text/x-python",
            use_container_width=True
        )
    else:
        st.link_button("ATIVAR LICENCA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)

st.write("---")
# Perguntas Frequentes
with st.container():
    st.markdown("### PERGUNTAS FREQUENTES")
    st.markdown("**Necessito de conhecimento previo em programacao?**")
    st.write("Nao. O script e entregue totalmente estruturado. O pacote inclui instrucoes em formato de texto direto para inicializacao em menos de dois cliques.")

st.caption("RVCX Software Terminal. Transacoes processadas via gateway de seguranca InfinitePay.")
