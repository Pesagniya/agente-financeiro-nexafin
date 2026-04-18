import streamlit as st
import pandas as pd
from agente import processar_pergunta

st.set_page_config(page_title="NexaFin - Seu Guia Financeiro", page_icon="💰")

st.title("💰 NexaFin")
st.markdown("---")

# Inicializar histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Como posso ajudar suas finanças hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("Analisando dados..."):
            resposta = processar_pergunta(prompt, st.session_state.messages)
            st.markdown(resposta)
    
    st.session_state.messages.append({"role": "assistant", "content": resposta})