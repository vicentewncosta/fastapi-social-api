API desenvolvida como parte de um desafio técnico de live coding. Permite o cadastro de usuários, criação de postagens, curtidas, listagem de feed e geração de dados em massa para testes.

## 📋 Sobre o Projeto

Esta é uma API REST que simula uma rede social simplificada, desenvolvida com FastAPI e SQLite. O projeto implementa as seguintes funcionalidades principais:

- **Sistema de Usuários**: Cadastro e gestão de usuários com username e email únicos
- **Sistema de Posts**: Permite que usuários criem postagens de texto
- **Interações Sociais**: Implementa sistema de curtidas em posts
- **Feed Dinâmico**: Lista posts com sistema de paginação
- **Dados para Teste**: Inclui gerador automático de dados usando Faker para testes em massa
- **Documentação Automática**: Interface Swagger UI disponível em `/docs`

O projeto foi estruturado seguindo boas práticas de desenvolvimento, com separação clara de responsabilidades, validação de dados via Pydantic e ORM com SQLAlchemy.

---

## 🚀 Tecnologias utilizadas

- FastAPI
- SQLite + SQLAlchemy
- Pydantic
- Faker
- Uvicorn

---

## 📦 Instalação e execução

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn app.main:app --reload

# Gerar dados de teste

python seed.py
```
Gera 100 usuários e 100 posts por usuário (10.000 posts no total).

## 📚 API Reference

### Endpoints

#### 👤 Usuários

##### Criar usuário
```http
POST /users/
```
| Parâmetro  | Tipo     | Descrição                |
| :--------- | :------- | :----------------------- |
| `username` | `string` | **Obrigatório**. Nome do usuário |
| `email`    | `string` | **Obrigatório**. Email do usuário |

Exemplo de Request:
```json
{
    "username": "alice",
    "email": "alice@test.com"
}
```

Exemplo de Response:
```json
{
    "id": 1,
    "username": "alice"
}
```

##### Listar usuários com postagens
```http
GET /users/with-posts
```
| Parâmetro   | Tipo     | Descrição                |
| :---------- | :------- | :----------------------- |
| `username`  | `string` | Filtrar por username     |
| `order`     | `string` | Ordenação (asc/desc)     |
| `limit`     | `int`    | Limite de resultados     |
| `offset`    | `int`    | Offset para paginação    |

#### 📝 Posts

##### Criar post
```http
POST /posts/
```
| Parâmetro  | Tipo     | Descrição                |
| :--------- | :------- | :----------------------- |
| `user_id`  | `int`    | **Obrigatório**. ID do usuário |
| `content`  | `string` | **Obrigatório**. Conteúdo do post |

##### Curtir post
```http
POST /posts/{id}/like
```

##### Listar feed
```http
GET /posts/feed
```
| Parâmetro | Tipo  | Descrição             |
| :-------- | :---- | :-------------------- |
| `limit`   | `int` | Limite de resultados  |
| `offset`  | `int` | Offset para paginação |

## 🏗️ Estrutura do Projeto

```
app/
├── main.py          # Arquivo principal da aplicação
├── database.py      # Configuração do banco de dados
├── models/          # Modelos do SQLAlchemy
├── schemas/         # Schemas do Pydantic
├── routers/         # Rotas da API
├── services/        # Lógica de negócio
└── utils/          # Funções auxiliares
```

## ✅ Features Implementadas

- [x] Banco de dados com SQLite
- [x] Cadastro de usuários
- [x] Criação de postagens
- [x] Sistema de curtidas em posts
- [x] Feed com paginação
- [x] Listagem de usuários com filtros
- [x] Geração de dados de teste
- [x] Documentação da API