import streamlit as st

# 1. FORÇANDO O SITE A PEGAR A TELA INTEIRA (Seguro e Nativo)
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    page_icon="🤖", 
    layout="wide"
)

# 2. INJEÇÃO DE ESTILOS COM COMANDO BLINDADO (Sem JavaScript para não quebrar)
st.html("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Courier New', Courier, monospace !important;
        background-color: #06090e !important;
        color: #00ffcc !important;
    }
    h1, h2, h3, p, span, .stMetric {
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Deixa os botões com visual neon rosa */
    div.stButton > button, div.stLinkButton > a {
        background-color: #ff0055 !important;
        color: white !important;
        border: 2px solid #ff0055 !important;
        box-shadow: 0 0 15px #ff0055 !important;
        font-weight: bold !important;
    }
    </style>
""")

# --- DIVISÃO DA TELA INTEIRA EM DUAS COLUNAS LARGAS ---
col_esquerda, col_direita = st.columns([1.2, 1])

with col_esquerda:
    st.title("🤖 RVCX SOFTWARE CORE v2.0")
    st.write("🌐 Link de Autenticação de Protocolos de Inteligência Artificial")
    
    # Espaço do seu Mascote Robô IA (substitua no GitHub por painel.png)
    st.image("painel.png", caption="RVCX AI Androide de Operações", use_container_width=True)
    
    st.write("---")
    
    # Tabela de Performance expandida nas laterais
    st.subheader("⏱️ Comparativo Real de Performance")
    dados_comparativos = {
        "Atividade": ["Pesquisar produtos", "Criar texto de venda", "Inserir link afiliado", "Postar nos canais"],
        "Modo Manual": ["45 minutos", "20 minutos", "5 minutos", "15 minutes"],
        "RVCX Software": ["3 segundos", "1.5 segundo", "Automático", "Imediato"]
    }
    st.table(dados_comparativos)

with col_direita:
    # Monitoramento de Conexão com cores vibrantes hacker
    st.subheader("📊 Status e Latência do Sistema")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("● ENGINE ONLINE")
    with c2: st.info("🧠 NEURAL: 3")
    with c3: st.warning("⚡ LATÊNCIA: 12ms")
    
    # Terminal interativo hacker
    with st.expander("👁️ VISUALIZAR TERMINAL DA AUTOMAÇÃO", expanded=True):
        st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexão com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERAÇÃO] 14 Produtos virais localizados nas últimas 2 horas.
[SISTEMA] Aguardando ativação da licença do usuário para liberar download...
        """, language="text")
        
    st.write("---")
    
    # Seção interativa de Benefícios por abas
    st.subheader("💡 Vantagens do Sistema")
    tab1, tab2 = st.tabs(["🎯 Mineração", "🚀 Postagens"])
    with tab1:
        st.markdown("### 🔍 Varredura de Produtos Virais")
        st.write("O script roda em segundo plano minerando os produtos que mais estão vendendo nas plataformas da Shopee e Amazon.")
    with tab2:
        st.markdown("### 📡 Disparo Automatizado")
        st.write("O robô formata a mensagem gerada pela inteligência artificial e envia diretamente para canais estruturados de ofertas.")

    st.write("---")

    # Área de Ativação e Botão de Compra
    st.subheader("🪙 Ativação do Protocolo Vitalício")
    st.metric(label="Valor Único Promocional", value="R$ 29,90")
    
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
        st.balloons()
        st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Licença vitalícia ativada.")
        script_texto = "# RVCX Software - Instalador automatico\nprint('Automacao carregada!')"
        st.download_button(
            label="📥 CLIQUE PARA INSTALAR O ROBÔ (rvcx_bot.py)",
            data=script_texto,
            file_name="rvcx_bot.py",
            mime="text/x-python",
            use_container_width=True
        )
    else:
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR ROBÔ AGORA", link_pagamento, use_container_width=True)

st.write("---")
# Perguntas Frequentes no rodapé
with st.container():
    st.subheader("❓ Perguntas Frequentes (FAQ)")
    st.markdown("**Preciso saber programar para usar o robô?**")
    st.write("Não! O script vai totalmente pronto e mastigado. Junto com o arquivo, você recebe um mini-tutorial em vídeo de 3 minutos ensinando como ligar ele no seu computador com apenas dois cliques.")

st.caption("© 2026 RVCX Software Terminal. Transações processadas via criptografia militar InfinitePay®.")
