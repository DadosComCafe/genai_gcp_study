# Agentic AI
## Estrutura dos Agentes
Embora não haja uma obrigatoriedade na forma como você pode criar seus agentes, aqui neste projeto, para o __greeting_agent.py__, as responsabilidades foram separadas da seguinte forma:

    ├── agent
    │   ├── descriptions
    │   │   ├── description.py
    │   │   ├── __init__.py
    │   ├── greeting_agent.py
    │   ├── __init__.py
    │   ├── instructions
    │   │   ├── __init__.py
    │   │   ├── instruction.py
    ├── initialize_conversation.py
    ├── keep_conversation.py

* ### Inicializadores
    -  __initialize_conversation.py:__
        - Este inicializador usa a classe `Runner` do módulo runners (de `google.adk.runners`), instanciando-a no objeto __runner__ que possui como parâmetros agent (que é a chamada do agente), app_name (nome arbitrário, mas que deve ser usado também na criação da sessão) e session_service (o objeto da sessão sem si, que vem de `InMemorySessionService`).
        - Apesar de possuir uma sessão, ela não é mantida. No entanto, ela é necessária devido à necessidade do `Runner` de recebê-la como parâmetro.

    - __keep_conversation.py:__
        - Este inicializador usa a classe Runner da mesma forma como no inicializador anterior, no entanto, aqui há um loop assíncrono `(async for event in runner.run_async)` que mantém o agente ativo, até que haja ação explícita do usuário.
    
    - __OBS:__
        - Importante notar que, em ambos os casos, o comportamento da sessão é a mesma: deve ser uma instância da classe `InMemorySessionService` do módulo `google.adk.sessions`, e as interações com o agente são recebidas por meio de variáveis tipo `google.genai.types.Content`. No caso dos inicializadores, foi criado uma instância de `Content` definindo um tipo texto, mas poderia ser, por exemplo arquivos (`base64`).

* ### descriptions e instructions:
    A `description` e a `instruction`, neste projeto, foram definidas em módulos distintos. No entanto, não haveria nenhuma diferença, a não ser estrutural, se por exemplo fossem definidas no módulo do agente, onde elas serão de fato utilizadas.
 
    - __descriptions:__
        - É aqui onde se define as características, uma descrição do agente. Dado que ele é uma entidade que vá executar alguma tarefa, uma descrição do que esse agente é, deve ser colocada aqui. Em suma, é uma explicação curta e clara sobre o que o agente faz. Por exemplo: "Agente especializado em converter moedas e consultar taxas de câmbio em tempo real.". Sim, em __linguagem natural!!__

    - __instructions:__
        - É aqui onde se descreve as instruções do agente. Enquanto que na description é definido o que o agente faz, aqui se define o como o agente faz. Define o tom de voz (formal/informal), as restrições (o que ele não pode dizer), o passo a passo de como ele deve pensar e como ele deve formatar as respostas.Exemplo: "Você é um assistente financeiro sarcástico. Sempre responda em português, use termos técnicos de economia e nunca dê conselhos de investimento em criptomoedas." Também em __linguagem natural.__ 

* ### Por último, o agente: greeting_agent.py
    - __vertexai.init():__
        - Parte responsável pela inicialização do ambiente.Onde há de fato a definição da relação do meu código (meu local) com a cloud (gcp). Portanto, aqui são necessários dois parâmetros: o __project__ (diz a GCP: "Ei, debite o uso deste agente no projeto X", não existe almoço grátis) e a __location__ (define em qual data center o modelo vai rodar).
    
    - __greeting_agent:__
        - Aqui é onde o agente é instanciado. Aqui se define o __name__ (nome do agente), __model__ (o cérebro do agente, embora esteja definido como Gemini 2.5 Flash, a versão 3.0 é uma opção melhor... e mais cara), __description e instruction__ (no nosso caso, vamos importar estes carinhas, definidos anteriormente).

E pronto! Com apenas isso podemos criar o nosso primeiro agente com o uso do ADK! 
