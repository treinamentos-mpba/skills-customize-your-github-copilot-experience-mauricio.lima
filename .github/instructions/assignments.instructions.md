---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`
- Não remova ou pule seções obrigatórias do template.

## 2. Orientação das Seções

Os cabeçalhos devem usar EXATAMENTE o texto do template, incluindo os ícones. Não traduza nem renomeie estes cabeçalhos:

- `# 📘 Atividade: [Título da Atividade]` — Use um nome curto e descritivo, como `Fundamentos de Python` ou `Jogo da Forca`.
- `## 🎯 Objetivo` — Escreva 1-2 frases resumindo o que o aluno aprenderá ou realizará. Foque nas principais habilidades ou conceitos.
- `## 📝 Tarefas` — Para cada tarefa, use `### 🛠️ [Título da Tarefa]` com as subseções abaixo:
   - `#### Descrição` — Indique claramente o que o aluno deve fazer.
   - `#### Requisitos` — Liste em tópicos resultados ou funcionalidades esperadas. Seja específico e mensurável.
   - Inclua exemplos de entrada e saída em blocos de código quando forem úteis.

Não inclua seções extras a menos que explicitamente especificado.