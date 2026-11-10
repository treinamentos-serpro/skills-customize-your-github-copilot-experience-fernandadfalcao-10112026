# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Adapte uma API FastAPI para armazenar os livros em um banco SQLite, praticando criação de tabelas, consultas SQL e persistência de dados entre reinicializações.

## 📝 Tarefas

### 🛠️ Criar o banco de dados

#### Descrição
Implemente a inicialização do SQLite para que a aplicação crie a tabela de livros automaticamente ao iniciar. Na pasta da atividade, instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`; a documentação interativa ficará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `books.db` na pasta da atividade, sem instalar uma biblioteca adicional para SQLite.
- Criar uma tabela `books` com colunas `id`, `title` e `author`.
- Definir `id` como chave primária e autoincrementável.
- Inicializar o banco durante o ciclo de vida da aplicação FastAPI.

### 🛠️ Persistir consultas e cadastros

#### Descrição
Substitua o armazenamento em memória por operações SQLite nas rotas de consulta e cadastro da API.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros do banco.
- Implementar `GET /books/{book_id}` para buscar um livro pelo identificador e responder HTTP 404 quando não existir.
- Implementar `POST /books` para inserir um livro e retornar o registro criado com HTTP 201.
- Usar consultas parametrizadas para inserir e consultar dados.

### 🛠️ Atualizar, remover e verificar persistência

#### Descrição
Conclua as operações de atualização e remoção, depois confirme que os dados continuam disponíveis após reiniciar o servidor.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar título e autor, respondendo HTTP 404 se o livro não existir.
- Implementar `DELETE /books/{book_id}` para remover um livro, respondendo HTTP 404 se ele não existir.
- Retornar HTTP 204 após uma remoção bem-sucedida.
- Manter os livros cadastrados após parar e iniciar novamente a aplicação.