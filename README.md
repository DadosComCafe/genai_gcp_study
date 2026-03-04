# Genai GCP Study
Este é um projeto que visa explorar o desenvolvimento de Inteligência Artificial Generativa (GENAI) com o uso das ferramentas da GCP. Portanto, como um primeiro requisito, é necessário ter um projeto na GCP. Logo, algum investimento em cloud é necessário. Não há problema em utilizar os créditos oferecidos pela Google, para experimentação de 3 meses.

- Mais informações no site oficial: https://cloud.google.com/free -> 300 dólares de crédito para ser usados em 3 meses, é um baita insentivo para os estudos.


## Índice

- __[1.Criando o projeto e ativando o vertex:](./1.Criando%20o%20projeto%20e%20ativando%20o%20Vertex/README.md)__
    - Nesta parte do repositório, é explicado como criar o projeto, ativar o vertex e criar a service account, deixando feito todo o necessário para a utilização da ferramenta `vertex` na sua máquina local, seja num script python, de um container docker, ou até mesmo em outra linguagem.

- __[2.Utilizando o vertex no python:](./2.Utilizando%20o%20vertex%20no%20python/README.md)__
    - Neste ponto você já possui um projeto na gcp, o vertex já está habilitado para o seu projeto, você gerou uma service account com a permissão mínima para usar o serviço vertex da gcp.
    - Agora, vamos iniciar um projeto python com o uv, gerar as variávies de ambiente, e fazer uma primeira pergunta a nossa IA: "Você é uma inteligência artificial?".

- __[3.Construindo Agentes de IA:](./3.Criando%20agentes%20com%20o%20ADK/README.md)__
    - Aqui iniciaremos os estudos e práticas da construção de agentes de IA, utilizando o ADK da google.

