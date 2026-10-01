# 📚 Miniguia de APIs REST e Automação com Python

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte de um desafio da **DIO**, com o objetivo de utilizar Inteligência Artificial como ferramenta de aprendizagem ativa.

O tema escolhido foi **APIs REST e Automação com Python**.

Para desenvolver o estudo, utilizei o **NotebookLM** para analisar fontes técnicas, elaborar perguntas, testar diferentes formas de prompting e identificar lacunas no meu próprio entendimento.

Além da parte teórica, desenvolvi e executei um pequeno programa em Python que realiza uma requisição real a uma API REST.

---

## 🎯 Objetivos de aprendizagem

Os principais objetivos deste estudo foram:

- Entender o conceito de API REST;
- Compreender o modelo cliente-servidor;
- Conhecer os principais métodos HTTP;
- Entender endpoints e códigos de status HTTP;
- Compreender o uso de JSON em APIs;
- Consumir uma API utilizando Python;
- Utilizar a biblioteca `requests`;
- Praticar engenharia de prompts;
- Utilizar IA como ferramenta ativa de aprendizagem.

---

## 🛠️ Tecnologias e ferramentas

- Python
- NotebookLM
- Git
- GitHub
- Google Colab
- Biblioteca Requests
- JSONPlaceholder

---

# 📖 Curadoria de fontes

Para construir o caderno temático no NotebookLM, foram selecionadas fontes abertas e documentações técnicas relacionadas ao assunto.

### 1. MDN Web Docs — HTTP

https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Overview

Utilizada para estudar o funcionamento do protocolo HTTP, requisições, respostas e comunicação cliente-servidor.

### 2. Requests — documentação oficial

https://requests.readthedocs.io/en/latest/

Utilizada para compreender como realizar requisições HTTP utilizando Python.

### 3. Python — urllib.request

https://docs.python.org/3/library/urllib.request.html

Utilizada para conhecer uma alternativa presente na biblioteca padrão do Python para trabalhar com URLs e requisições HTTP.

### 4. JSONPlaceholder

https://jsonplaceholder.typicode.com/

API REST gratuita utilizada para testes e prototipagem durante o projeto.

---

# 🧠 Aprendizagem ativa com NotebookLM

O NotebookLM foi utilizado não apenas para gerar resumos, mas para realizar um processo iterativo de aprendizagem.

A estratégia utilizada foi:

**Fonte → Pergunta → Resposta → Análise → Identificação de lacuna → Refinamento do prompt → Novo teste**

Isso permitiu comparar diferentes respostas e melhorar progressivamente a qualidade das explicações.

---

# 💬 Engenharia de Prompts e Cicatrizes

## Prompt #1 — Exploração inicial

> Explique o que é uma API REST e como ela pode ser utilizada com Python.

### Resultado

O NotebookLM apresentou conceitos como:

- modelo cliente-servidor;
- métodos HTTP;
- JSON;
- `urllib.request`;
- biblioteca `requests`;
- JSONPlaceholder.

### Problema identificado

Apesar de tecnicamente completa, a resposta apresentou muitos conceitos simultaneamente.

Para alguém iniciando no assunto, ainda não estava totalmente claro o caminho percorrido por uma requisição desde o programa Python até a resposta do servidor.

---

## Prompt #2 — Tentativa de aprofundamento

Foi solicitado ao NotebookLM que explicasse passo a passo uma requisição GET utilizando:

`https://jsonplaceholder.typicode.com/posts/1`

O prompt também solicitava três perguntas para verificar o aprendizado.

### Cicatriz encontrada

A resposta voltou a apresentar principalmente um resumo geral sobre APIs.

Além disso, algumas instruções específicas do prompt não foram seguidas, incluindo a geração das três perguntas solicitadas.

### Aprendizado

Dar mais contexto nem sempre garante uma resposta melhor.

Foi necessário definir explicitamente:

- o que não deveria ser feito;
- a ordem da resposta;
- o cenário analisado;
- os conceitos obrigatórios;
- o formato da saída.

---

## Prompt #3 — Prompt refinado

O prompt foi reformulado para analisar exclusivamente:

```python
requests.get("https://jsonplaceholder.typicode.com/posts/1")
```

A resposta deveria obrigatoriamente explicar:

1. Cliente;
2. Endpoint;
3. Requisição HTTP;
4. Servidor;
5. Status code;
6. JSON;
7. `response.json()`.

Também foi solicitado o seguinte fluxo:

`Python → requisição HTTP → endpoint → servidor → resposta HTTP → JSON → objeto Python`

E exatamente três perguntas para testar o aprendizado.

### Resultado

Dessa vez, o NotebookLM seguiu a estrutura solicitada e apresentou o processo de maneira muito mais clara.

Isso demonstrou como **restrições, contexto, formato de saída e escopo bem definidos melhoram a qualidade das respostas de uma IA**.

---

# 🧩 Verificação do aprendizado

As perguntas produzidas pelo NotebookLM também revelaram algumas lacunas no meu conhecimento.

Entre elas:

- diferença entre endpoint e método HTTP;
- significado de códigos como `200` e `404`;
- diferença entre uma resposta textual e um objeto Python produzido por `response.json()`.

Essas dificuldades foram utilizadas como pontos de revisão em vez de simplesmente solicitar as respostas prontas.

---

# 📘 Miniguia de APIs REST

## O que é uma API?

Uma API (*Application Programming Interface*) permite que diferentes aplicações troquem informações de maneira estruturada.

Em uma API web, normalmente uma aplicação cliente envia uma requisição e um servidor devolve uma resposta.

---

## O que é REST?

REST é um estilo arquitetural utilizado na construção de serviços web.

APIs REST normalmente trabalham com recursos acessíveis através de URLs e utilizam métodos HTTP para indicar as operações desejadas.

---

## Cliente e servidor

Em nosso exemplo:

```python
requests.get("https://jsonplaceholder.typicode.com/posts/1")
```

O programa Python funciona como **cliente**.

O JSONPlaceholder funciona como o serviço acessado pelo cliente.

O fluxo simplificado é:

`Python → requisição → servidor → resposta → Python`

---

## Endpoint

Um endpoint representa um endereço pelo qual determinado recurso de uma API pode ser acessado.

Exemplo:

`https://jsonplaceholder.typicode.com/posts/1`

Nesse cenário, `/posts/1` identifica o recurso que estamos solicitando.

Uma maneira simples de lembrar:

**Endpoint = onde**

---

## Métodos HTTP

Alguns dos principais métodos são:

| Método | Utilização |
|---|---|
| GET | Obter dados |
| POST | Criar/enviar dados |
| PUT | Substituir ou atualizar um recurso |
| PATCH | Atualizar parcialmente |
| DELETE | Excluir um recurso |

Uma maneira simples de diferenciar:

**Endpoint = onde**

**Método HTTP = o que queremos fazer**

---

## Status Codes

O servidor utiliza códigos HTTP para informar o resultado da requisição.

| Código | Significado |
|---|---|
| 200 | OK |
| 201 | Recurso criado |
| 400 | Requisição inválida |
| 401 | Não autenticado |
| 403 | Acesso proibido |
| 404 | Recurso não encontrado |
| 500 | Erro interno do servidor |

---

## JSON

JSON é um formato muito utilizado para troca de dados entre aplicações.

Exemplo:

```json
{
  "id": 1,
  "title": "Meu post"
}
```

A biblioteca `requests` permite converter uma resposta JSON para estruturas Python utilizando:

```python
dados = response.json()
```

Depois disso podemos acessar valores como:

```python
print(dados["title"])
```

---

# 💻 Implementação prática

Para aplicar os conceitos estudados, foi criado o arquivo:

`api_example.py`

Código:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200:
    dados = response.json()

    print("ID:", dados["id"])
    print("Título:", dados["title"])
    print("Conteúdo:", dados["body"])
else:
    print("Erro ao consultar a API.")
```

---

## 🧪 Teste realizado

O código foi executado utilizando Python no Google Colab.

Resultado:

```text
Status: 200
ID: 1
Título: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Conteúdo: quia et suscipit...
```

O status `200` confirmou que a requisição foi processada com sucesso.

O exercício permitiu observar na prática o seguinte processo:

`Python → GET → endpoint → servidor → 200 OK → JSON → response.json() → dicionário Python`

---

# 📚 Glossário

**API:** interface utilizada para comunicação entre sistemas.

**REST:** estilo arquitetural utilizado em serviços web.

**HTTP:** protocolo utilizado para comunicação na Web.

**Request:** requisição enviada pelo cliente.

**Response:** resposta enviada pelo servidor.

**Endpoint:** endereço utilizado para acessar determinado recurso de uma API.

**GET:** método HTTP utilizado para solicitar dados.

**POST:** método HTTP normalmente utilizado para enviar/criar dados.

**JSON:** formato estruturado utilizado para troca de dados.

**Status Code:** código que representa o resultado de uma requisição HTTP.

**Payload:** dados transportados em uma requisição ou resposta.

---

# 🤖 Prompts reutilizáveis

Durante o projeto, alguns padrões de prompts mostraram-se úteis para futuros estudos.

### Explicação para iniciantes

> Explique [CONCEITO] como se eu estivesse aprendendo o assunto pela primeira vez. Utilize apenas as fontes fornecidas e apresente um exemplo prático.

### Explicação passo a passo

> Analise exclusivamente [CENÁRIO]. Explique cada etapa na ordem em que acontece e apresente ao final um fluxo visual utilizando setas.

### Verificação de conhecimento

> Com base nas fontes fornecidas, crie 5 perguntas progressivas sobre [ASSUNTO]. Não forneça as respostas até que eu tente respondê-las.

### Identificação de lacunas

> Analise minha explicação sobre [ASSUNTO]. Identifique conceitos incorretos ou incompletos e indique quais fontes fornecidas sustentam a correção.

### Revisão

> Crie uma revisão curta sobre [ASSUNTO], destacando os conceitos essenciais, erros comuns e três perguntas para verificar meu entendimento.

---

# 🚀 Principais aprendizados

Este projeto mostrou que Inteligência Artificial pode ser utilizada não apenas para obter respostas, mas como ferramenta para estruturar um processo de aprendizagem.

Um dos principais aprendizados foi perceber que a qualidade da resposta depende significativamente da qualidade das instruções fornecidas.

O processo de testar, identificar problemas e refinar prompts tornou o estudo mais ativo e permitiu compreender melhor conceitos de APIs REST e Python.

Também foi possível aplicar a teoria através de uma requisição real utilizando Python e a biblioteca `requests`.

---

## 🔜 Próximos passos

Como evolução deste projeto, pretendo estudar:

- autenticação em APIs;
- API Keys;
- tratamento de exceções;
- parâmetros de requisição;
- requisições POST;
- integração entre APIs e automações;
- construção de uma API própria utilizando Python.

---

## 👨‍💻 Autor

**Gabriel Ribeiro Pedroso**

Estudante de Análise e Desenvolvimento de Sistemas, com foco em Python, automação e Inteligência Artificial aplicada.
