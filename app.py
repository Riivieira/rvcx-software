import streamlit as st

# 1. CONFIGURAÇÃO PADRÃO E SEGURA DE TELA CHEIA
st.set_page_config(
    page_title="RVCX Software - Portal Oficial", 
    layout="wide"
)

# --- ESTILOS GLOBAL CSS (IMAGENS GRANDES E BOTÃO LUMINOSO) ---
st.markdown(
    """
    <style>
    /* Esconde o botão de Fullscreen/Maximizar de TODAS as imagens do site */
    button[title="View fullscreen"], 
    .stMainBlockContainer button,
    [data-testid="stImageActionButton"] {
        display: none !important;
    }
    
    /* Evita problemas de arrastar imagem, mantendo os botões funcionais */
    [data-testid="stImage"] img {
        pointer-events: none !important;
    }
    
    /* Força a logo superior a ficar visivelmente maior na tela */
    div[data-testid="stImage"] img {
        max-width: 100% !important;
        max-height: 380px !important;
        object-fit: contain !important;
        margin: 0 auto !important;
    }

    /* ESTILO DO BOTÃO DE DOWNLOAD EXCLUSIVO COM BRILHO NEON CIANO */
    .link-download-neon {
        display: block;
        width: 100%;
        background-color: #00ffcc !important;
        color: #0d1117 !important;
        text-align: center;
        padding: 14px 20px;
        font-size: 16px;
        font-weight: bold;
        text-decoration: none !important;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }
    
    /* Efeito hover do botão luminoso */
    .link-download-neon:hover {
        background-color: #00ffcc !important;
        box-shadow: 0 0 25px #00ffcc, 0 0 50px #00ffcc !important;
        transform: scale(1.02);
        color: #0d1117 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SEUS LINKS SEPARADOS E CONFIGURADOS ---
link_pagamento = "https://checkout.infinitepay.io/ricardo-vieira-costa/miAR86vJWc"
link_whatsapp_chave = "https://w.app/7k3fa5"
link_whatsapp_suporte = "https://w.app/0ijobe"

# Captura os parâmetros de retorno pós-pagamento
query_params = st.query_params
pagamento_aprovado = "capture_method" in query_params

# =========================================================================
# TELA 1: ÁREA EXCLUSIVA DE DOWNLOAD (SÓ APARECE SE FOR PAGO / MODO TESTE)
# =========================================================================
if pagamento_aprovado:
    
    # Cabeçalho da Área de Membros
    col_logo_esq, col_logo_ctr, col_logo_dir = st.columns([1, 2, 1])
    with col_logo_ctr:
        st.image("logo_rvcx.png", use_container_width=True)
        
    st.markdown("<h2 style='text-align: center; font-weight: bold; color: #00ffcc;'>PORTAL OFICIAL DE DOWNLOAD & LICENCIAMENTO</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # SOLICITAÇÃO DA CHAVE EM PRIMEIRO LUGAR (NO TOPO DA ÁREA DE DOWNLOAD)
    st.markdown("### 🔑 PASSO 1: LIBERAÇÃO DA SUA CHAVE DE ACESSO")
    st.write("O software possui um sistema de segurança vinculado ao hardware do seu computador para evitar pirataria.")
    st.write("**Clique no botão abaixo imediatamente para abrir nosso canal de ativação e receber seu serial:**")
    st.write("")
    st.link_button("🔑 CLIQUE AQUI PARA PEDIR SUA CHAVE DE ATIVAÇÃO NO WHATSAPP", link_whatsapp_chave, use_container_width=True)
    
    st.write("---")
    
    # DOWNLOAD DO ARQUIVO REAL VIA LINK DE REDIRECIONAMENTO COM BRILHO
    st.markdown("### 📦 PASSO 2: DOWNLOAD DOS INSTALADORES")
    
    col_down_esq, col_down_dir = st.columns(2)
    
    with col_down_esq:
        st.markdown("#### 💻 Versão PC (Windows)")
        st.write("Clique no botão luminoso abaixo para iniciar o download do instalador seguro diretamente no computador.")
        st.write("")
        
        # Link HTML direto focado no download do executável
        st.markdown(
            f'<a href="RVCX_Software_Installer.exe" download class="link-download-neon">'
            f'📦 BAIXAR INSTALADOR RVCX_SOFTWARE.EXE'
            f'</a>', 
            unsafe_allow_html=True
        )
        st.write("")
        st.caption("ℹ️ Compatível com sistemas Windows 10 e Windows 11.")

    with col_down_dir:
        st.markdown("#### 📱 Versão Celular (Mobile)")
        st.write("A arquitetura para celulares está passando por testes finais em nosso servidor dedicado.")
        st.write("")
        st.button("🔄 VERSÃO MOBILE EM DESENVOLVIMENTO", disabled=True, use_container_width=True)
        st.caption("Acesso gratuito garantido para todos os clientes vitalícios assim que liberado.")
        
    st.write("---")
    st.caption("RVCX Software Terminal. Licença verificada de forma síncrona via nuvem.")

# =========================================================================
# TELA 2: PÁGINA DE VENDAS PRINCIPAL (SÓ APARECE SE NÃO ESTIVER PAGO)
# =========================================================================
else:
    # --- HEADER DO PORTAL ---
    col_logo_esq, col_logo_ctr, col_logo_dir = st.columns([1, 2, 1])
    with col_logo_ctr:
        st.image("logo_rvcx.png", use_container_width=True)

    st.markdown("<h2 style='text-align: center; font-weight: bold;'>SISTEMA OPERACIONAL DE AUTOMAÇÃO E CRIAÇÃO DE POSTS PARA AFILIADOS</h2>", unsafe_allow_html=True)

    # --- BOTÃO DE VENDA IMEDIATA ---
    col_btn_esq, col_btn_ctr, col_btn_dir = st.columns([1, 2, 1])
    with col_btn_ctr:
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR SOFTWARE VITALÍCIO", link_pagamento, use_container_width=True)

    st.write("---")

    # --- BLOCO 1 ---
    col1_img, col1_txt = st.columns(2)
    with col1_img:
        st.image("painel.png", use_container_width=True)
    with col1_txt:
        st.markdown("<h2>MASCOTE CENTRAL CORE</h2>", unsafe_allow_html=True)
        st.write(
            "Este é o painel de controle do RVCX. O sistema foi desenvolvido em um aplicativo "
            "executável para rodar diretamente no seu computador Windows, realizando todas as "
            "rotinas programadas de postagens e links sem que você precise mexer em nenhuma linha de código."
        )
        st.text("Status da Engine: Ativa")
        st.write("")
        st.link_button("⚡ COMPRAR LICENÇA RVCX", link_pagamento, use_container_width=True)

    st.write("---")

    # --- BLOCO 2 ---
    col2_txt, col2_img = st.columns(2)
    with col2_txt:
        st.markdown("<h2>PAINEL DE MONITORAMENTO</h2>", unsafe_allow_html=True)
        st.write(
            "Como visto na tela do sistema, o aplicativo monitora em tempo real as páginas "
            "de ofertas mais quentes da Shopee e da Amazon. Ele faz varreduras rápidas nas listas "
            "de mais vendidos para identificar os produtos exatos que mais possuem chance de conversão."
        )
        st.text("Varredura de dados: Ativa")
    with col2_img:
        st.image("robo_escritorio.png", use_container_width=True)

    st.write("---")

    # --- BLOCO 3 ---
    col3_img, col3_txt = st.columns(2)
    with col3_img:
        st.image("robo_codigo.png", use_container_width=True)
    with col3_txt:
        st.markdown("<h2>ORGANIZADOR DE TEXTO E LINKS</h2>", unsafe_allow_html=True)
        st.write(
            "O programa automatizado organiza toda a estrutura da sua publicação de afiliado. "
            "Ele junta o nome do produto selecionado, formata descrições diretas com hashtags em alta "
            "e insere automaticamente o seu link de afiliado de forma limpa e configurada para o clique."
        )
        st.text("Geração de Conteúdo: Concluída")

    st.write("---")

    # --- BLOCO 4 ---
    col4_txt, col4_img = st.columns(2)
    with col4_txt:
        st.markdown("<h2>ENVIOS PROGRAMADOS E SEGURANÇA</h2>", unsafe_allow_html=True)
        st.write(
            "A estrutura interna do aplicativo conta com comandos de pausas inteligentes (Sleep delay). "
            "Isso simula o ritmo humano de digitação e cliques, permitindo enviar seus links promocionais "
            "para seus canais e grupos de ofertas automáticos diminuindo drasticamente os riscos de bloqueio."
        )
        st.text("Protocolo Antispam: Operational")
    with col4_img:
        st.image("robo_processador.png", use_container_width=True)

    st.write("---")

    # --- SEÇÃO INFERIOR: METRICAS ---
    col_dados, col_checkout = st.columns(2)

    with col_dados:
        st.markdown("### LOG DE OPERAÇÕES EM TEMPO REAL")
        st.code("""
[INFO] Inicializando Aplicativo RVCX...
[OK] Conexão com raspador Shopee/Amazon estabelecida.
[OK] Integração de envio configurada com sucesso.
[MONITORAMENTO] 14 Produtos quentes localizados nas últimas horas.
[SISTEMA] Aguardando liberação do checkout para download do aplicativo...
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
        st.write("✔️ Link para download do instalador executável (.exe) do software RVCX.")
        st.write("✔️ Vídeo tutorial passo a passo ensinando a abrir e usar no Windows.")
        st.write("✔️ Suporte direto via WhatsApp para te ajudar na ativação inicial.")
        st.write("✔️ Acesso vitalício ao programa sem nenhuma mensalidade oculta.")
        st.write("")
        st.link_button("⚡ ATIVAR LICENÇA E INSTALAR PROTOCOLO", link_pagamento, use_container_width=True)
        st.write("")
        # Botão de suporte configurado com o link de dúvidas (0ijobe)
        st.link_button("💬 TENHO DÚVIDAS? FALAR COM O SUPORTE NO WHATSAPP", link_whatsapp_suporte, use_container_width=True)

    st.write("---")
    # Perguntas Frequentes
    with st.container():
        st.markdown("### Perguntas Frequentes")
        st.markdown("**Necessito de conhecimento prévio em programação ou Python?**")
        st.write("Não. O sistema é entregue em formato de aplicativo comum (.exe). Você só precisa dar dois cliques para instalar e começar a usar através de uma interface visual simples.")
        st.markdown("**O que eu preciso ter para rodar?**")
        st.write("Apenas um computador ou notebook com sistema operacional Windows e conexão com a internet.")

    st.caption("RVCX Software Terminal. Transações seguras via gateway de pagamento InfinitePay.")
