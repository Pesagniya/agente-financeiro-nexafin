import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """Configurações centrais do Agente NexaFin"""
    
    # Chaves de API (Devem estar no arquivo .env)
    API_KEY = os.getenv("OPENAI_API_KEY") # Ou GOOGLE_API_KEY se estiver usando Gemini
    
    # Configurações do Modelo
    MODEL_NAME = "gpt-4o"  # ou "gemini-1.5-flash"
    TEMPERATURE = 0.3      # Baixa temperatura para respostas mais precisas e menos criativas
    
    # Caminhos de Dados
    DATA_PATH = {
        "perfil": "data/perfil_investidor.json",
        "produtos": "data/produtos_financeiros.json",
        "transacoes": "data/transacoes.csv",
        "historico": "data/historico_atendimento.csv"
    }
    
    # Configurações de UX/UI
    CHAT_TITLE = "NexaFin - Seu Guia Financeiro"
    WELCOME_MESSAGE = "Olá! Sou o NexaFin. Como posso ajudar nas suas decisões financeiras hoje?"

# Verificação de segurança básica
if not Config.API_KEY:
    print("AVISO: API_KEY não encontrada. Verifique o seu arquivo .env")