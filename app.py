import streamlit as st

# 1. FORÇANDO O SITE A PEGAR A TELA INTEIRA (layout="wide")
st.set_page_config(
    page_title="RVCX Software - Terminal Oficial", 
    page_icon="🤖", 
    layout="wide"
)

# 2. INJEÇÃO DE FONTE FUTURISTA E FUNDO ANIMADO MATRIX (HTML/JS)
# Desenha um efeito hacker diretamente no fundo da página de forma leve
st.markdown("""
    <style>
    /* Altera a fonte global do site para estilo Computador/Hacker */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Courier New', Courier, monospace !important;
        background-color: #05070a !important;
        color: #00ffcc !important;
    }
    h1, h2, h3, p, span {
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Estilização customizada das caixas e botões */
    div.stButton > button {
        background-color: #ff0055 !important;
        color: white !important;
        border: 2px solid #ff0055 !important;
        box-shadow: 0 0 15px #ff0055;
        font-weight: bold;
    }
    /* Tela de fundo animada */
    #matrix-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        opacity: 0.15; /* Deixa o fundo suave para não atrapalhar a leitura */
        pointer-events: none;
    }
    </style>
    
    <canvas id="matrix-canvas"></canvas>
    
    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const katakana = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789👾🤖⚡💻';
    const alphabet = katakana.split('');

    const fontSize = 16;
    const columns = canvas.width / fontSize;

    const rainDrops = [];

    for( let x = 0; x < columns; x++ ) {
        rainDrops[x] = 1;
    }

    const draw = () => {
        ctx.fillStyle = 'rgba(5, 7, 10, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#00ffcc';
        ctx.font = fontSize + 'px monospace';

        for(let i = 0; i < rainDrops.length; i++) {
            const text = alphabet[Math.floor(random() * alphabet.length)];
            ctx.fillText(text, i*fontSize, rainDrops[i]*fontSize);

            if(rainDrops[i]*fontSize > canvas.height && random() > 0.975){
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    };

    setInterval(draw, 30);
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    </script>
""", unsafe_allowed_html=True)

# --- DIVISÃO DA TELA INTEIRA EM DUAS COLUNAS LARGAS ---
col_esquerda, col_direita = st.columns([1.2, 1])

with col_esquerda:
    st.title("🤖 RVCX SOFTWARE CORE v2.0")
    st.write("🌐 Link de Autenticação de Protocolos de Inteligência Artificial")
    
    # Trocamos a foto antiga pelo espaço do novo Mascote Robô IA que você vai gerar
    st.image("painel.png", caption="RVCX AI Androide de Operações", use_container_width=True)
    
    st.write("---")
    
    # Tabela de Performance expandida nas laterais
    st.subheader("⏱️ Comparativo Real de Performance")
    dados_comparativos = {
        "Atividade": ["Pesquisar produtos em alta", "Criar roteiro/legenda de venda", "Colocar links de afiliado", "Postar em múltiplos canais"],
        "Modo Manual (Sem IA)": ["45 minutos", "20 minutos por post", "5 minutos", "15 minutos"],
        "RVCX Software (Com IA)": ["3 segundos", "1.5 segundo", "Automático", "Imediato em massa"]
    }
    st.table(dados_comparativos)

with col_direita:
    # Monitoramento de Conexão com cores vibrantes hacker
    st.subheader("📊 Status e Latência do Sistema")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("● ENGINE ONLINE")
    with c2: st.info("🧠 NEURAL NETWORKS: 3")
    with c3: st.warning("⚡ LATÊNCIA: 12ms")
    
    # Terminal interativo hacker
    with st.expander("👁️ VISUALIZAR TERMINAL DA AUTOMAÇÃO (Clique para expandir)", expanded=True):
        st.code("""
[INFO] Inicializando RVCX Software...
[OK] Conexão com Banco de Dados Shopee/Amazon estabelecida.
[OK] API ChatGPT vinculada com sucesso.
[MINERAÇÃO] 14 Produtos virais localizados nas últimas 2 horas.
[IA WRITER] Legendas persuasivas criadas automaticamente com link de afiliado.
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
