import openai
import json
import pandas as pd

# Carregar Base de Conhecimento
def carregar_dados():
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
    transacoes = pd.read_csv('data/transacoes.csv')
    return perfil, produtos, transacoes

def processar_pergunta(pergunta, historico):
    perfil, produtos, transacoes = carregar_dados()
    
    # Contexto para injeção no prompt (RAG)
    contexto_dados = f"""
    Perfil do Usuário: {perfil['usuario']['perfil']}
    Objetivos: {perfil['usuario']['objetivos']}
    Últimas Transações: {transacoes.tail(3).to_dict()}
    Produtos Disponíveis: {produtos}
    """

    system_prompt = f"""
    Você é o NexaFin, um assistente financeiro. 
    REGRAS: 
    1. Use os dados abaixo para responder: {contexto_dados}
    2. Nunca peça senhas.
    3. Seja didático. Explique termos como CDI e Selic.
    4. Se o usuário quiser investir, verifique se condiz com o perfil {perfil['usuario']['perfil']}.
    """

    # Chamada para a API (Exemplo usando OpenAI/Gemini)
    # Aqui você integraria com sua API Key
    try:
        # Mock de resposta caso não tenha API key configurada no momento do teste
        if "CDI" in pergunta.upper():
            return "O CDI é uma taxa de referência. Baseado nos seus produtos, o CDB rende 100% dele!"
        return "Olá! Sou o NexaFin. Analisei seu perfil e notei que você busca segurança. Como posso ajudar com seus gastos ou investimentos hoje?"
    except Exception as e:
        return "Desculpe, tive um problema técnico. Pode repetir?"