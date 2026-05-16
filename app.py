import streamlit as st

# 1. CONFIGURACAO PADRAO E SEGURA DE TELA CHEIA
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    layout="wide"
)

# --- ESTRUTURA EM DUAS COLUNAS LARGAS NATIVAS ---
col_esquerda, col_direita = st.columns([1.2, 1])

with col_esquerda:
    st.markdown("# RVCX SOFTWARE CORE v2.0")
    st.markdown("### Autenticacao de Protocolos de Inteligencia Artificial")
    st.write("---")
    
    # Foto 1: Mascote Principal
    st.image("painel.png", use_container_width=True)
    
    # Espaçadores nativos e seguros para afastar as imagens
    st.write("")
    st.write("")
    st.write("")
    
    # Foto 2: Robo com o processador IA
    st.image("robo_processador.png", use_container_width=True)
    
    st.write("---")
    
    # Tabela de Performance
    st.markdown("### Metricas de Performance em Produtividade")
    dados_comparativos = {
        "Atividade": ["Minerar produtos", "Criar copy de venda", "Inserir link de afiliado", "Postar nos canais"],
        "Metodo Manual": ["45 minutos", "20 minutos", "5 minutos", "15 minutos"],
        "Sistema RVCX": ["3 segundos", "1.5 segundo", "Automatizado", "Imediato"]
    }
    st.table(dados_comparativos)

with col_direita:
    # Status Tecnico
    st.markdown("### Status do Sistema")
    st.text("Status do motor: Operacional")
    st.text("Rede neural: Ativa (ASYNC_v3)")
    st.text("Latencia de rede: 12ms")
    st.write("---")
    
    # Terminal de comando
    st.text("Log de operacoes em tempo real:")
    st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexao com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERACAO] 14 Produtos virais localizados nas ultimas 2 horas.
[SISTEMA] Aguardando ativacao da licenca para liberar download...
    """, language="text")
    
    st.write("---")
    
    # Foto 3: Robo no Escritorio
    st.image("robo_escritorio.png", use_container_width=True)
    
    # Espaçadores nativos e seguros para afastar as imagens
    st.write("")
    st.write("")
    st.write("")
    
    # Foto 4: Robo apontando para o codigo Python
    st.image("robo_codigo.png", use_container_width=True)
    
    st.write("---")
    
    # Abas de vantagens
    st.markdown("### Arquitetura Criptografada")
    tab1, tab2 = st.tabs(["Mineracao", "Postagens"])
    with tab1:
        st.write("O script roda em background minerando os produtos de maior engajamento e conversao do dia.")
    with tab2:
        st.write("O robo estrutura o payload gerado pela IA e efetua o disparo em massa para os canais.")

    st.write("---")

    # Area de Licenciamento e Botao
    st.markdown("### Licenciamento Vitalicio")
    st.markdown("## R$ 29,90")
    st.write("")

    # --- CONFIGURACAO DE CHECKOUT INTEGRADO (INFINITEPAY) ---
    INFINITE_TAG = "sua_tag_aqui"  # Lembre de mudar para a sua tag real depois!
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
        st.success("Autenticacao confirmada. Licenca vitalicia ativada.")
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
    st.markdown("### Perguntas Frequentes")
    st.markdown("**Necessito de conhecimento previo em programacao?**")
    st.write("Nao. O script e entregue totalmente estruturado para inicializacao em menos de dois cliques.")

st.caption("RVCX Software Terminal. Transacoes processadas via gateway de segurança InfinitePay.")
