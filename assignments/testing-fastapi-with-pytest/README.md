# 📘 Atividade: Testando APIs com pytest e FastAPI

## 🎯 Objetivo

Aprenda a testar uma API REST com pytest e o `TestClient` do FastAPI. Você vai verificar respostas HTTP, criação de dados, validação e tratamento de erros sem iniciar um servidor manualmente.

## 📝 Tarefas

### 🛠️ Escrever e executar o primeiro teste

#### Descrição
Use a aplicação de livros fornecida e o arquivo inicial de testes. Instale as dependências e crie testes para confirmar que a API está funcionando.

```bash
python -m pip install fastapi pytest httpx
python -m pytest -v
```

#### Requisitos
O programa concluído deve:

- Criar um `TestClient` para a aplicação FastAPI
- Verificar que `GET /health` retorna status `200` e `{"status": "ok"}`
- Verificar que `GET /books` retorna uma lista vazia quando não há livros
- Executar os testes com `python -m pytest -v`


### 🛠️ Testar cadastro e validação

#### Descrição
Adicione testes para cadastrar livros e conferir como a API responde a dados válidos e inválidos.

#### Requisitos
O programa concluído deve:

- Testar `POST /books` com um livro válido e verificar status `201` e os dados retornados
- Verificar que o livro cadastrado aparece em `GET /books`
- Enviar um livro sem um campo obrigatório e verificar status `422`
- Usar dados de teste explícitos, sem depender da execução de outro teste


### 🛠️ Testar consulta, atualização e remoção

#### Descrição
Complete a cobertura das operações de livro testando os fluxos de sucesso e os casos em que o identificador não existe.

#### Requisitos
O programa concluído deve:

- Testar `GET /books/{book_id}` e `PUT /books/{book_id}` com um livro existente
- Testar `DELETE /books/{book_id}` e confirmar que o livro foi removido
- Verificar que consultar, atualizar ou remover um livro inexistente retorna status `404`
- Confirmar que os testes podem ser executados repetidamente sem depender de dados deixados por outro teste
