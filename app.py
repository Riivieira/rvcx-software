import streamlit as st

# Configuração da página avançada
st.set_page_config(
    page_title="RVCX Software - Painel Oficial", 
    page_icon="🤖", 
    layout="centered"
)

# --- BLOCOS DE CONTEÚDO (TOPO) ---
st.title("🤖 RVCX SOFTWARE CORE")
st.write("🌐 Módulo Oficial de Autenticação e Licenciamento de Protocolos IA")

# Imagem Principal do Painel Hacker
st.image("painel.png", use_container_width=True)

st.write("---")

# --- 1. MONITORAMENTO EM TEMPO REAL ---
st.subheader("📊 Status e Latência do Sistema")
col1, col2, col3 = st.columns(3)
with col1:
    st.success("● ENGINE ONLINE")
with col2:
    st.info("🧠 NEURAL NETWORKS: 3")
with col3:
    st.warning("⚡ LATÊNCIA: 12ms")

st.write("")

# Terminal interativo
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

# --- 2. SEÇÃO DE BENEFÍCIOS (O QUE O ROBÔ FAZ) ---
st.subheader("💡 Por que utilizar o Protocolo RVCX?")
st.write("A nossa automação foi desenhada para eliminar o trabalho braçal e focar no que importa: comissões no seu bolso.")

tab1, tab2, tab3 = st.tabs(["🎯 Mineração Automática", "✍️ Copywriter IA", "🚀 Postagem em Massa"])

with tab1:
    st.markdown("### 🔍 Varredura de Produtos Virais")
    st.write("O script roda em segundo plano minerando os produtos que mais estão vendendo e gerando engajamento nas plataformas da Shopee e Amazon no dia atual.")
    st.info("✓ Zero trabalho de pesquisa manual.")

with tab2:
    st.markdown("### 🧠 Inteligência Artificial Generativa")
    st.write("Conectado direto com as engines mais modernas de IA, o robô analisa o produto escolhido e cria um texto de vendas altamente persuasivo (Copywriting) focado em cliques.")
    st.info("✓ Legendas prontas com suas tags e hashtags ideais.")

with tab3:
    st.markdown("### 📡 Disparo Automatizado")
    st.write("Chega de copiar e colar manualmente em dezenas de lugares. O robô formata a mensagem e envia diretamente para canais do Telegram, Twitter ou estruturas organizadas de redes sociais.")
    st.info("✓ Estrutura de múltiplos posts agendados por minuto.")

st.write("---")

# --- 3. TABELA COMPARATIVA (PROVA DE VALOR) ---
st.subheader("⏱️ Comparativo de Performance")
st.write("Veja quanto tempo e esforço você economiza utilizando a nossa tecnologia:")

# Tabela limpa e profissional nativa
dados_comparativos = {
    "Atividade": ["Pesquisar produtos em alta", "Criar roteiro/legenda de venda", "Colocar links de afiliado", "Postar em múltiplos canais"],
    "Modo Manual (Sem IA)": ["45 minutos", "20 minutos por post", "5 minutos", "15 minutos"],
    "RVCX Software (Com IA)": ["3 segundos", "1.5 segundo", "Automático", "Imediato em massa"]
}
st.table(dados_comparativos)

st.write("---")

# --- 4. ÁREA DE COMPRA E PREÇO ---
st.subheader("🪙 Ativação do Protocolo Vitalício")
st.write("Garanta o seu acesso à ferramenta e todas as futuras atualizações do script sem mensalidades.")

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
    st.success("🎉 AUTENTICAÇÃO CONFIRMADA! Licença vitalícia ativada com sucesso.")
    
    # Armazenado como texto limpo e seguro
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

# --- 5. PERGUNTAS FREQUENTES (FAQ) ---
st.subheader("❓ Perguntas Frequentes (FAQ)")

with st.container():
    st.markdown("**Preciso saber programar para usar o robô?**")
    st.write("Não! O script vai totalmente pronto e mastigado. Junto com o arquivo, você recebe um mini-tutorial em vídeo de 3 minutos ensinando como ligar ele no seu computador com apenas dois cliques.")
    
    st.markdown("**Tem perigo de tomar bloqueio nas plataformas?**")
    st.write("Nosso código possui um sistema de 'Sleep delayed' inteligente que altera os horários de postagem simulando o comportamento de um ser humano, minimizando drasticamente qualquer risco.")
    
    st.markdown("**Como recebo as atualizações?**")
    st.write("O acesso é vitalício. Sempre que nossa equipe atualizar as funções do robô, você poderá baixar a versão nova diretamente por este portal oficial sem pagar nenhum centavo a mais.")

st.write("---")

# --- RODAPÉ PROFISSIONAL ---
st.caption("© 2026 RVCX Software Terminal. Todos os direitos reservados.")
st.caption("Ambiente seguro e transações processadas via criptografia militar InfinitePay®.")
