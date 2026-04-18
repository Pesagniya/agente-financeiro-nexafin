# NexaFin - Agente de Bem-Estar Financeiro com IA Generativa

O **NexaFin** é uma experiência digital voltada ao relacionamento financeiro, fundamentada em inteligência artificial generativa e princípios avançados de UX (User Experience). O projeto integra Processamento de Linguagem Natural (NLP), cálculos financeiros demonstrativos e persistência de contexto para oferecer interações seguras, claras e personalizadas.

---

## 🚀 Funcionalidades

* **FAQ Inteligente:** Respostas rápidas e contextualizadas sobre produtos financeiros e conceitos bancários.
* **Simulador de Investimentos:** Cálculos de juros compostos e projeções baseadas em dados inseridos pelo usuário.
* **Explicação de Produtos:** Tradução de termos técnicos ("economês") para linguagem acessível.
* **Persistência de Contexto:** Capacidade de manter o histórico da conversa para fluxos de atendimento contínuos.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **IA Generativa:** Google Gemini API (ou LangChain)
* **Interface:** Streamlit (para prototipação rápida)
* **Processamento de Dados:** Pandas / NumPy
* **UX/UI:** Princípios de design centrado no usuário e acessibilidade.

---

## 📂 Estrutura do Projeto

O desenvolvimento seguiu as seguintes etapas obrigatórias:

1.  **Etapa 1: Documentação do Agente** - Definição de persona, tom de voz e regras de comportamento.
2.  **Etapa 2: Base de Conhecimento** - Estruturação dos dados e documentos que alimentam a IA (RAG).
3.  **Etapa 3: Prompts do Agente** - Engenharia de prompt para garantir respostas precisas e seguras.
4.  **Etapa 4: Aplicação Funcional** - Desenvolvimento do código back-end e front-end em Python.
5.  **Etapa 5: Avaliação e Métricas** - Testes de usabilidade, acurácia financeira e mitigação de alucinações.
6.  **Etapa 6: Pitch** - Demonstração de valor e entrega final da solução.

---

## 🧮 Base Matemática

O agente utiliza fórmulas financeiras padrão para garantir a precisão dos cálculos demonstrativos, como a de juros compostos:

$$M = P(1 + i)^n$$

Onde:
* $M$: Montante final
* $P$: Principal (valor inicial)
* $i$: Taxa de juros por período
* $n$: Número de períodos

---

## 🔧 Como Executar

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/nexafin-ux-ai.git](https://github.com/seu-usuario/nexafin-ux-ai.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure sua chave de API no arquivo `.env`.
4.  Execute a aplicação:
    ```bash
    streamlit run app.py
    ```

---