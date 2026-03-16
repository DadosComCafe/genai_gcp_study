# Playground
Aqui é criado um ambiente local, que disponibiliza o agente em um servidor Fastapi.
Desta forma, as interações com a IA vão ocorrer através da realização de posts no servidor.

## Como Rodar
### 1 - __Clone o repositório:__
* git clone https://github.com/DadosComCafe/genai_gcp_study

### 2 - __Inicialize seu ambiente com o `uv`, e rode o servidor com o uvicorn:__
* cd playground
* uv sync
* cd app/server
* uvicorn main:app --reload

Ou utilizando docker:
* Buildar a imagem:
    - Com o terminal aberto na raiz do projeto playground, execute:
    - docker build -t fastapi_server:1.0 .

* Rodar o servidor:
    - docker run -p 3000:3000 fastapi_server:1.0


