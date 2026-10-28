# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, modelar dados com Pydantic e implementar operações CRUD usando métodos e códigos de status HTTP.

## 📝 Tarefas

### 🛠️ Criar a aplicação e uma rota de saúde

#### Descrição
Instale as dependências, complete a configuração inicial do FastAPI e crie uma rota simples para confirmar que a API está funcionando.

```bash
python -m pip install "fastapi[standard]"
fastapi dev starter-code.py
```

#### Requisitos
O programa concluído deve:

- Criar uma instância FastAPI chamada `app`
- Implementar `GET /health` e retornar `{"status": "ok"}`
- Iniciar localmente e disponibilizar a documentação interativa em `/docs`


### 🛠️ Modelar e cadastrar livros

#### Descrição
Crie modelos Pydantic para os dados de um livro e implemente operações para cadastrar livros e listar a coleção. Mantenha os dados em memória durante a execução do servidor.

#### Requisitos
O programa concluído deve:

- Definir um modelo de entrada com título, autor e ano de publicação
- Implementar `POST /books`, atribuir um identificador ao novo livro e responder com status `201`
- Implementar `GET /books` e retornar todos os livros, incluindo uma lista vazia quando não houver registros
- Aceitar um corpo JSON como este:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```


### 🛠️ Implementar consulta, atualização e remoção

#### Descrição
Complete as operações da coleção para consultar, atualizar e remover um livro pelo identificador. Use as respostas HTTP para comunicar resultados e erros ao cliente.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar `404` quando o livro não existir
- Implementar `PUT /books/{book_id}` para atualizar os dados e retornar o livro atualizado
- Implementar `DELETE /books/{book_id}` para remover o registro e responder com status `204`
- Retornar `404` ao tentar atualizar ou remover um livro inexistente
- Usar a validação automática do FastAPI/Pydantic para rejeitar dados inválidos