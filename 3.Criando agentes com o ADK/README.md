# Criando Agentes de IA
## Iniciando a IA Agêntica
## Sobre
Iniciando o entendimento de A agêntica, com a criação de um agente simples, e dois inicializadores distintos: - Um mantém o contexto, e o outro não.

A IA Agêntica é um novo paradigma para a inteligência artificial, tal como a orientação a objeto foi para o desenvolvimento de software.

## Como Rodar?
### 1 - __Clone o repositório:__
* git clone https://github.com/DadosComCafe/genai_gcp_study

### 2 - __Edite o arquivo __my_env.sh__, e rode-o com:__
* cd 3.\ Criando\ agentes\ com\ o\ ADK/
* cd very_simple_agent/
* source my_env.sh

### 3 - __Configure o ambiente e instale as dependências do python:__
* uv sync

### 4 - __Execute o teste:__
* uv run teste_vertex_runing.py

### 5 - __Finalmente, execute o agente:__
uv run initialize_conversation.py