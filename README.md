app/database.py
Cria a conexão com o banco SQLite

Define SessionLocal para interagir com o banco

Define Base para os modelos ORM

🧍 app/models/user_model.py
Define a tabela users com campos: id, username, email, posts

📝 app/models/post_model.py
Define a tabela posts com campos: id, user_id, content, likes, created_at

Relaciona cada post com um usuário

📦 app/schemas/
Define os modelos Pydantic para entrada (Create) e saída (Response)

Garante validação e estrutura das requisições/respostas

🔄 app/services/
Contém a lógica de negócio:

Criar usuário

Criar post

Curtir post

Listar feed

Listar usuários com paginação

🌐 app/routers/
Define os endpoints da API:

POST /users/ → cria usuário

GET /users/ → lista usuários com paginação

POST /posts/ → cria post

POST /posts/{id}/like → curte post

GET /posts/feed → lista feed com paginação

🧪 app/utils/seed_data.py
Gera 1000 usuários e 1000 posts por usuário usando Faker

Ideal para testes de performance e volume

🚀 app/main.py
Inicializa o FastAPI

Cria as tabelas no banco

Inclui os routers de usuários e posts