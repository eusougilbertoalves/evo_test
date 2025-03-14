import streamlit as st
import os
from message_sender import MessageSender

# Configuração da página
st.set_page_config(
    page_title="Evolution WhatsApp Sender", 
    page_icon="📱",
    layout="centered"
)

# Iniciando uma instância da classe MessageSender
sender = MessageSender()

# Título principal com estilo
st.title("📲 Envio de Mensagens WhatsApp")
st.markdown("<p style='font-size: 1.2em; color: #4CAF50;'>Powered by Evolution API</p>", unsafe_allow_html=True)

# Configurações de features habilitáveis
with st.sidebar:
    st.header("⚙️ Configurações")
    enable_file_upload = st.toggle("Habilitar envio de arquivos", value=False)
    show_advanced = st.toggle("Mostrar opções avançadas", value=False)
    st.markdown("---")
    st.markdown("### 📊 Status da Conexão")
    if sender.client:
        st.success("✅ Conectado à Evolution API")
    else:
        st.error("❌ Falha na conexão com a API")

# Criar pasta temporária para arquivos (se habilitado)
if enable_file_upload and not os.path.exists("temp"):
    os.makedirs("temp")

# Container principal
with st.container():
    # Campos de entrada com melhor formatação
    number = st.text_input(
        "📞 Número de telefone:", 
        placeholder="Ex: 5511999999999 (com DDI e DDD)",
        help="Insira o número com DDI (55 para Brasil) + DDD + número"
    )
    
    message = st.text_area(
        "✍️ Mensagem:", 
        placeholder="Digite sua mensagem aqui...",
        help="Escreva o texto que deseja enviar"
    )
    
    # Opção de upload de arquivo (se habilitado)
    file = None
    if enable_file_upload:
        file = st.file_uploader(
            "📎 Escolha um arquivo (opcional):", 
            type=["jpg", "jpeg", "png", "pdf", "mp3", "mp4"],
            help="Selecione um arquivo para enviar junto com a mensagem"
        )
    
    # Opções avançadas (se habilitadas)
    if show_advanced:
        st.markdown("### 🔧 Opções Avançadas")
        col1, col2 = st.columns(2)
        with col1:
            show_response = st.checkbox("Mostrar resposta da API", value=False)
        with col2:
            enable_preview = st.checkbox("Habilitar pré-visualização", value=True)
    else:
        show_response = False
        enable_preview = True
    
    # Botão de envio com estilo
    bt_send = st.button("📤 Enviar Mensagem", type="primary", use_container_width=True)

# Lógica de envio aprimorada
if bt_send:
    # Validação de entrada
    if not number:
        st.error("❌ Por favor, insira um número de telefone.")
    elif len(number) < 10:
        st.error("❌ Número de telefone inválido. Use o formato: DDI+DDD+Número")
    elif not message and not file:
        st.warning("⚠️ Por favor, insira uma mensagem ou selecione um arquivo.")
    else:
        # Processamento do envio com feedback visual
        with st.spinner("Enviando mensagem..."): 
            try:
                # Lógica para envio de arquivo (se implementado e habilitado)
                if enable_file_upload and file:
                    # Placeholder para futura implementação de envio de mídia
                    st.info("🚧 Envio de arquivos será implementado em uma versão futura.")
                    # Aqui entraria a lógica de envio de mídia quando implementada
                    # Exemplo: response = sender.mediaMessage(number, file, message)
                else:
                    # Envio de mensagem de texto
                    response = sender.textMessage(number, message)
                
                # Feedback de sucesso
                st.success("✅ Mensagem enviada com sucesso!")
                
                # Mostrar resposta da API se opção habilitada
                if show_response:
                    st.json(response)
                    
            except Exception as e:
                st.error(f"❌ Erro ao enviar a mensagem: {e}")

# Informações adicionais
st.markdown("---")
st.markdown("""
### ℹ️ Instruções:
1. Digite o número de telefone com DDI e DDD (ex: 5511999999999)
2. Escreva sua mensagem no campo de texto
3. Clique em enviar e aguarde a confirmação

Para habilitar recursos adicionais, utilize o menu de configurações na barra lateral.
""")
