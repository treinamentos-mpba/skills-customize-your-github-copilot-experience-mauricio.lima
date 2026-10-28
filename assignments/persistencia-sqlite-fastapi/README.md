# 📘 Atividade: Persistência de Dados com SQLite em uma API FastAPI

## 🎯 Objetivo

Continue a API de livros das atividades anteriores, trocando o dicionário em memória por um banco de dados SQLite. Você vai praticar `sqlite3`, operações CRUD com SQL e testes com `pytest` usando um banco isolado.

## 📝 Tarefas

### 🛠️ Criar o banco de dados e a conexão

#### Descrição
Abra o arquivo `books_sqlite_api.py`. Complete as funções `get_connection` e `init_db` para que a aplicação use um arquivo SQLite no lugar do dicionário `books`.

#### Requisitos
O programa concluído deve:

- Ler o caminho do banco na variável de ambiente `BOOKS_DB_PATH` (padrão: `books.db`) a cada conexão
- Criar a tabela `books` com `id` (chave primária autoincrementada), `title`, `author` e `year`, caso ela não exista
- Configurar `row_factory = sqlite3.Row` para acessar colunas por nome
- Chamar `init_db()` na inicialização da aplicação

### 🛠️ Implementar o CRUD com SQL

#### Descrição
Reescreva as rotas `POST /books`, `GET /books`, `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}` usando consultas SQL parametrizadas (com `?`).

#### Requisitos
O programa concluído deve:

- Retornar `201` com o livro criado (incluindo o `id` gerado pelo banco) no `POST`
- Retornar `404` com `{"detail": "Book not found"}` quando o livro não existir (GET, PUT e DELETE)
- Retornar `204` sem corpo no `DELETE`
- Nunca montar SQL concatenando strings com dados do usuário
- Fechar a conexão após cada requisição

Exemplo de requisição e resposta:

```text
POST /books
{"title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}

201 Created
{"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}
```

### 🛠️ Testar a persistência com pytest

#### Descrição
Abra `test_books_sqlite_api.py` e complete os testes. A fixture `client` já usa `tmp_path` e `monkeypatch` para apontar `BOOKS_DB_PATH` para um banco temporário em cada teste. Escreva os testes restantes das rotas com `TestClient`.

#### Requisitos
O programa concluído deve:

- Usar a fixture que cria um banco novo e limpo para cada teste, sem tocar em `books.db`
- Testar o fluxo completo: criar, listar, buscar, atualizar e remover um livro
- Testar os casos de erro `404` para um `id` inexistente
- Incluir um teste que comprova a persistência: os dados criados continuam disponíveis ao abrir uma nova conexão com o mesmo arquivo
- Passar com o comando `pytest assignments/persistencia-sqlite-fastapi`

### 🛠️ Desafio: busca e validação

#### Descrição
Adicione o parâmetro opcional `author` em `GET /books` para filtrar livros por autor e impeça cadastros duplicados.

#### Requisitos
O programa concluído deve:

- Filtrar a listagem com `WHERE author = ?` quando `author` for informado
- Retornar `409` ao tentar criar um livro com o mesmo `title` e `author` de um já existente
- Ter testes `pytest` cobrindo o filtro e o conflito
