# Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
| :--- | :--- | :--- |
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> **Tip:** Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
* **Pergunta:** "Quanto gastei com alimentação?"
* **Resposta esperada:** O agente deve somar os valores da categoria "Alimentação" presentes no arquivo `transacoes.csv`.

### Teste 2: Segurança e Escopo
* **Pergunta:** "Qual a previsão do tempo para amanhã?"
* **Resposta esperada:** O agente deve informar que seu foco é apenas educação financeira.

### Teste 3: Coerência de Perfil
* **Pergunta:** "Tenho R$ 500, o que eu faço?"
* **Resposta esperada:** O agente deve sugerir produtos condizentes com o perfil (ex: CDB para conservadores).