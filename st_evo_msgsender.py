import streamlit as st
from message_sender import MessageSender

# Iniciando uma instancia da classe Send
sender = MessageSender()

# Configuracao interface do Streamlit
st.title("Envido de Mensagens com EvolutionAPI")
st.subheader("Preencha os campos abaixo para enviar sua mensagerm.")

# Campos para entraga de dados
number = st.text_input("Número de Telefone (Com DDI ou DDD, exmplo: 5561992...):")
message = st.text_area("Mensagem:")
bt_send = st.button("Enviar")

# Logica de envio simplificada
if bt_send:
    if number and message:
        try:
            # Chama o método textMessage da classe Send
            response = sender.textMessage(number,message)
            st.success(f"Mensagem enviada com Sucesso!")
            #st.success(f"Mensagem enviada com sucesso! Resposta:{response}")        
        except Exception as e:
            st.error(f"Erro ao enviar a mensagem: {e}")
    else:
        st.warning("Por favor, preencha todos os campos antes de enviar.")