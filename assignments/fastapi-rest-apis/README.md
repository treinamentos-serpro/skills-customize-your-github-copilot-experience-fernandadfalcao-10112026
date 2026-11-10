# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para gerenciar um catálogo de livros, praticando rotas HTTP, validação de dados e operações CRUD.

## 📝 Tarefas

### 🛠️ Consultar livros

#### Descrição
Complete a API para permitir consultar todos os livros e buscar um livro pelo identificador. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor na pasta da atividade com `uvicorn starter-code:app --reload`; a documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` e retornar a lista de livros armazenada em memória.
- Implementar `GET /books/{book_id}` e retornar o livro correspondente ao identificador.
- Responder com HTTP 404 quando o identificador solicitado não existir.

### 🛠️ Cadastrar livros

#### Descrição
Adicione uma rota para cadastrar livros no catálogo usando os modelos Pydantic fornecidos no código inicial.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` com `title` e `author` no corpo da requisição.
- Validar que título e autor não estejam vazios.
- Gerar um identificador para cada livro novo e armazená-lo em memória.
- Retornar o livro criado com status HTTP 201.

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações de atualização e remoção de livros existentes no catálogo.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Responder com HTTP 404 quando a atualização ou remoção solicitar um identificador inexistente.
- Retornar status HTTP 204 após uma remoção bem-sucedida.