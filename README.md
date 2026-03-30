# TaskFlow - Sistema de Gestão de Tarefas

**Projeto: Bootcamp - Tema 2**

O TaskFlow é um sistema para o controle de tarefas de equipes. A arquitetura separa a camada de apresentação das regras de negócio.

---

## 1. Organização e Fluxo de Trabalho

A estrutura base do sistema (API e Telas principais) será desenvolvida inicialmente e disponibilizada na branch `main`. A partir dessa base, o grupo fará o desenvolvimento das melhorias, finalizações e documentação.

* Adotaremos o fluxo de **Fork e Pull Request (PR)**.
* Cada membro deve fazer um fork deste repositório, preencher a tabela abaixo com o que vai desenvolver, trabalhar em cima do código base e abrir o PR para integração.

---

## 2. Requisitos Básicos

O escopo do projeto contempla:

1. **Usuários:** Cadastro e listagem (Nome, E-mail e Função).
2. **Tarefas:** Cadastro (Título, Descrição, Prioridade, Prazo) e associação a um usuário.
3. **Status:** Controle de andamento (A Fazer, Em Andamento, Concluído).
4. **Filtros e Relatórios:** Listagem e totalizadores simples de tarefas.

---

## 3. Stack Tecnológica

* **Front-end:** Vue.js 3, Pinia, Tailwind CSS
* **Back-end:** Python, FastAPI, SQLAlchemy
* **Banco de Dados:** PostgreSQL (via Docker)

---

## 4. Divisão de Tarefas

**Instrução:** Faça o fork do repositório, insira seu nome, a área e a descrição do que você vai desenvolver. Depois, abra o Pull Request com suas implementações.

| ID | Responsável | Área | Descrição da Tarefa (O que vai fazer) |
| :--- | :--- | :--- | :--- |
| **01** | Jhuan | Base (MVP) | Estrutura inicial do Back-end, Front-end e Banco de Dados |
| **02** | [ Gabriela ] | [ Ex: Front-end ] | [ Responsável pelo design e estilização da parte front-end do projeto. ] |
| **03** | [ Nome ] | [ Ex: Back-end ] | [ Descreva sua tarefa aqui ] |
| **04** | [ Gabriela | Gabriel David ] | [ Ex: Documentação ]| [ Responsável pela elaboração da documentação e envio do trabalho na plataforma. ] |
| **05** | [ Carlos David ] | [ Validação ] | [ Teste em ambiente local ] |
| **06** | [ Nome ] | [ Área ] | [ Descreva sua tarefa aqui ] |
| **07** | [ Nome ] | [ Área ] | [ Descreva sua tarefa aqui ] |
| **08** | [ Nome ] | [ Área ] | [ Descreva sua tarefa aqui ] |
| **09** | [ Nome ] | [ Área ] | [ Descreva sua tarefa aqui ] |
| **10** | [ Nome ] | [ Área ] | [ Descreva sua tarefa aqui ] |

---

## 5. Como rodar o projeto localmente

### Pré-requisitos

Antes de iniciar, certifique-se de possuir:

- Docker em execução
- Python 3.11
- Node.js (versão LTS recomendada)

### 5.1 Banco de Dados (PostgreSQL)

Na raiz do projeto, execute:

```bash
docker-compose up -d
```

### 5.2 Back-end

Acesse a pasta do back-end:

```bash
cd backend
```

Crie o ambiente virtual com Python 3.11:
```bash
py -3.11 -m venv .venv
```

Ative o ambiente virtual no Windows:
```bash
.venv\Scripts\activate
```

Instale as dependências:
```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Execute o servidor:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em:
```bash
http://127.0.0.1:8000
```

### 5.3 Validação do Back-end (Swagger)

Acesse:

```bash
http://127.0.0.1:8000/docs
```

#### Criar usuário

No endpoint `POST /usuarios`, clique em **Try it out** e utilize um corpo como este:

```json
{
  "nome": "Gabriel",
  "email": "gabriel@example.com",
  "funcao": "desenvolvedor"
}
```

Depois, clique em **Execute**.

---

#### Listar usuários

No endpoint `GET /usuarios`, verifique se o usuário foi cadastrado corretamente.

---


### 5.4 Front-end

A partir da raiz do projeto:

```bash
cd frontend
npm install
npm run dev
```

A aplicação estará disponível em:

```bash
http://localhost:5173
```

---

## 6. Observações

- O projeto segue uma arquitetura com separação entre front-end e back-end.
- O banco de dados é executado em container Docker para facilitar a portabilidade.
- A API foi desenvolvida com FastAPI e possui documentação automática via Swagger.