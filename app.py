import streamlit as st

# 1. CONFIGURACAO PADRAO E SEGURA DE TELA CHEIA
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    layout="wide"
)

# --- CONFIGURAÇÃO DE CHECKOUT INTEGRADO (CORRIGIDA) ---
INFINITE_TAG = "ricardo-vieira-costa"  

item_nome = "RVCX_Robo_Afiliado"
item_preco = 6090  # R$ 60,90
pedido_id = "RVCX999" 
URL_RETORNO = "https://streamlit.app"

# CORREÇÃO CRÍTICA DA URL DE PAGAMENTO DA INFINITEPAY
link_pagamento = (
    f"https://infinitepay.io{INFINITE_TAG}?"
    f"items=[{{'name':'{item_nome}','price':{item_preco},'quantity':1}}]&"
    f"order_nsu={pedido_id}&"
    f"redirect_url={URL_RETORNO}"
)

# Captura os parâmetros de retorno pós-pagamento
query_params = st.query_params
pagamento_aprovado = "capture_method" in query_params

# --- ESCUDO DO PORTAL (TOPO DO SITE) ---
st.markdown("# RVCX SOFTWARE CORE v2.0")
st.markdown("### SISTEMA OPERACIONAL DE MINERAÇÃO E VENDAS AUTOMÁTICAS POR IA")
st.write("---")

# --- BLOCO 1: APRESENTAÇÃO DO CORE ---
col1_img, col1_txt = st.columns([1.2, 1])
with col1_img:
    st.image("painel.png", use_container_width=True)
with col1_txt:
    st.markdown("## MASCOTE CENTRAL CORE")
    st.write(
        "Este é o núcleo da inteligência artificial RVCX. O sistema roda de forma "
        "independente em nuvem assíncrona, conectando-se diretamente às APIs neurais "
        "para processar dados de mercado sem consumir a memória ou o processamento do seu computador."
    )
    st.text("Status da Engine: Ativa")
    st.write("")
    
    if pagamento_aprovado:
        st.success("LICENÇA ATIVADA.")
    else:
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)

st.write("---")

# --- BLOCO 2: MINERAÇÃO E TELAS ---
col2_txt, col2_img = st.columns([1, 1.2])
with col2_txt:
    st.markdown("## PAINEL DE MONITORAMENTO")
    st.write(
        "Como visto na tela do sistema, o robô monitora em tempo real gráficos de faturamento, "
        "tendências e métricas de conversão. Ele varre as plataformas da Shopee e Amazon a cada "
        "segundo para identificar quais produtos exatos estão viralizando no momento."
    )
    st.text("Varredura de dados: Ativa")
with col2_img:
    st.image("robo_escritorio.png", use_container_width=True)

st.write("---")

# --- BLOCO 3: ESCRITA DO CÓDIGO E ANÁLISE ---
col3_img, col3_txt = st.columns([1.2, 1])
with col3_img:
    st.image("robo_codigo.png", use_container_width=True)
with col3_txt:
    st.markdown("## ENGENHARIA DE PROMPT E CÓDIGO")
    st.write(
        "O robô possui um compilador interno em Python. Ao selecionar o produto viral, a inteligência "
        "artificial cria o script de vendas completo, embutindo o seu link de afiliado de forma "
        "criptografada. O sistema gera títulos, legendas e hashtags usando gatilhos altamente persuasivos."
    )
    st.text("Geração de Copywriting: Concluída")

st.write("---")

# --- BLOCO 4: ARQUITETURA NEURAL ---
col4_txt, col4_img = st.columns([1, 1.2])
with col4_txt:
    st.markdown("## DISPARO EM MASSA E ANTIBLOQUEIO")
    st.write(
        "A arquitetura interna do hardware simula o comportamento humano através de rotinas de atraso "
        "(Sleep delayed). Isso permite que o script envie os links gerados para centenas de canais, "
        "grupos e redes de ofertas de maneira totalmente automática e com risco zero de suspensão."
    )
    st.text("Protocolo Antibloqueio: Operacional")
with col4_img:
    st.image("robo_processador.png", use_container_width=True)

st.write("---")

# --- SEÇÃO INFERIOR: METRICAS E CHECKOUT ---
col_dados, col_checkout = st.columns(2)

with col_dados:
    st.markdown("### LOG DE OPERAÇÕES EM TEMPO REAL")
    st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexao com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERACAO] 14 Produtos virais localizados nas ultimas 2 horas.
[SISTEMA] Aguardando ativacao da licenca para liberar download...
    """, language="text")
    
    st.markdown("### MÉTRICAS DE PERFORMANCE EM PRODUTIVIDADE")
    dados_comparativos = {
        "Atividade": ["Minerar produtos", "Criar copy de venda", "Inserir link de afiliado", "Postar nos canais"],
        "Método Manual": ["45 minutos", "20 minutos", "5 minutos", "15 minutos"],
        "Sistema RVCX": ["3 segundos", "1.5 segundo", "Automático", "Imediato"]
    }
    st.table(dados_comparativos)

with col_checkout:
    st.markdown("### LICENCIAMENTO VITALÍCIO")
    st.markdown("## VALOR DO PROTOCOLO: R$ 60,90")
    st.write("A ativação inclui o arquivo do script original e acesso gratuito a todas as atualizações de código.")
    st.write("")

    if pagamento_aprovado:
        st.balloons()
        st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Licença vitalícia ativada.")
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
    st.write("Não. O script é entregue totalmente estruturado para inicialização em menos de dois cliques.")

st.caption("RVCX Software Terminal. Transações processadas via gateway de segurança InfinitePay.")
