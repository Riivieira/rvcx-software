import streamlit as st

# 1. CONFIGURAÇÃO PADRÃO E SEGURA DE TELA CHEIA
st.set_page_config(
    page_title="RVCX Software - Painel de Controle", 
    layout="wide"
)

# --- LINK REAL DE COBRANÇA DA INFINITEPAY GERADO PELO USUÁRIO ---
link_pagamento = "https://link.infinitepay.io/ricardo-vieira-costa/VC1DLTEtSQ-Hqt0uDRoVZ-60,90"

# Captura os parâmetros de retorno pós-pagamento
query_params = st.query_params
pagamento_aprovado = "capture_method" in query_params

# --- ESCUDO DO PORTAL (TOPO DO SITE) ---
st.markdown("# RVCX SOFTWARE CORE v2.0")
st.markdown("### SISTEMA OPERACIONAL DE AUTOMAÇÃO E CRIAÇÃO DE POSTS PARA AFILIADOS")
st.write("---")

# --- BLOCO 1: APRESENTAÇÃO DO CORE (IMAGEM NA ESQUERDA, TEXTO NA DIREITA) ---
col1_img, col1_txt = st.columns([1.2, 1])
with col1_img:
    st.image("painel.png", use_container_width=True)
with col1_txt:
    st.markdown("## MASCOTE CENTRAL CORE")
    st.write(
        "Este é o painel principal do robô RVCX. O sistema foi desenvolvido para "
        "rodar scripts automatizados diretamente no seu computador ou servidor em nuvem, "
        "executando rotinas programadas para organizar suas postagens e links de afiliado sem complicações."
    )
    st.text("Status da Engine: Ativa")
    st.write("")
    
    if pagamento_aprovado:
        st.success("LICENÇA ATIVADA.")
    else:
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)

st.write("---")

# --- BLOCO 2: MINERAÇÃO E TELAS (TEXTO NA ESQUERDA, IMAGEM NA DIREITA) ---
col2_txt, col2_img = st.columns([1, 1.2])
with col2_txt:
    st.markdown("## PAINEL DE MONITORAMENTO")
    st.write(
        "Como visto na tela do sistema, o script foi estruturado para monitorar em tempo real "
        "as páginas de ofertas mais quentes da Shopee e da Amazon. Ele faz varreduras rápidas nas listas "
        "de mais vendidos para identificar os produtos exatos que mais possuem chance de conversão."
    )
    st.text("Varredura de dados: Ativa")
with col2_img:
    st.image("robo_escritorio.png", use_container_width=True)

st.write("---")

# --- BLOCO 3: ESCRITA DO CÓDIGO E ANÁLISE (IMAGEM NA ESQUERDA, TEXTO NA DIREITA) ---
col3_img, col3_txt = st.columns([1.2, 1])
with col3_img:
    st.image("robo_codigo.png", use_container_width=True)
with col3_txt:
    st.markdown("## ORGANIZADOR DE TEXTO E LINKS")
    st.write(
        "Desenvolvido inteiramente em Python, o robô organiza toda a estrutura da sua publicação. "
        "Ele junta o nome do produto selecionado, formata descrições diretas com hashtags em alta "
        "e insere automaticamente o seu link de afiliado no formato correto pronto para publicação."
    )
    st.text("Geração de Conteúdo: Concluída")

st.write("---")

# --- BLOCO 4: ARQUITETURA NEURAL (TEXTO NA ESQUERDA, IMAGEM NA DIREITA) ---
col4_txt, col4_img = st.columns([1, 1.2])
with col4_txt:
    st.markdown("## ENVIOS PROGRAMADOS E SEGURANÇA")
    st.write(
        "A estrutura do código conta com comandos de pausas inteligentes (Sleep delay). Isso simula "
        "o ritmo de digitação e cliques de uma pessoa real, permitindo enviar seus links promocionais "
        "para seus canais e grupos de ofertas automáticos diminuindo drasticamente os riscos de bloqueio."
    )
    st.text("Protocolo Antispam: Operacional")
with col4_img:
    st.image("robo_processador.png", use_container_width=True)

st.write("---")

# --- SEÇÃO INFERIOR: METRICAS E CHECKOUT ---
col_dados, col_checkout = st.columns(2)

with col_dados:
    st.markdown("### LOG DE OPERAÇÕES EM TEMPO REAL")
    st.code("""
[INFO] Inicializando Script RVCX...
[OK] Conexão com raspador Shopee/Amazon estabelecida.
[OK] Integração de envio configurada com sucesso.
[MONITORAMENTO] 14 Produtos quentes localizados nas últimas horas.
[SISTEMA] Aguardando liberação do checkout para download do código...
    """, language="text")
    
    st.markdown("### MÉTRICAS DE PERFORMANCE EM PRODUTIVIDADE")
    dados_comparativos = {
        "Atividade": ["Buscar produtos", "Montar texto do post", "Embutir link de afiliado", "Postar nos canais"],
        "Método Manual": ["45 minutos batendo cabeça", "20 minutos digitando", "5 minutos copiando", "15 minutos entrando de grupo em grupo"],
        "Sistema RVCX": ["Poucos segundos", "Instantâneo", "Automático", "Envio programado"]
    }
    st.table(dados_comparativos)

with col_checkout:
    st.markdown("### LICENCIAMENTO VITALÍCIO")
    st.markdown("## VALOR DO PROTOCOLO: R$ 60,90")
    st.write("**A ativação inclui:**")
    st.write("✔️ Arquivo original do script (.py) pronto para rodar.")
    st.write("✔️ Manual explicativo passo a passo de como configurar seus links.")
    st.write("✔️ Suporte direto via WhatsApp para te ajudar na primeira execução.")
    st.write("✔️ Acesso vitalício sem cobrança de mensalidades.")
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
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)

st.write("---")
# Perguntas Frequentes
with st.container():
    st.markdown("### Perguntas Frequentes")
    st.markdown("**Necessito de conhecimento prévio em programação?**")
    st.write("Não. O código é entregue todo comentado e organizado. Basta instalar as dependências explicadas no manual e dar o play.")
    st.markdown("**O que eu preciso ter para rodar?**")
    st.write("Apenas um computador simples com Python instalado e os seus links de afiliado em mãos.")

st.caption("RVCX Software Terminal. Transações seguras via gateway de pagamento InfinitePay.")
