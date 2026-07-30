# 13 — Linguagens de Programação

Guia específico para cada linguagem da stack de desenvolvimento full-stack, com LSPs recomendados.

## Python

| Item | Valor |
|------|-------|
| LSP principal | **pyright** (tipos, autocomplete, goto) |
| Linter/formatter | **ruff** (lint + format) |
| Extensões | `.py`, `.pyi` |
| Root markers | `pyproject.toml`, `setup.py`, `requirements.txt` |

### Verificar

```bash
hx --health python
```

### Workflow

```
gd          → ir à definição de função/classe
Space k     → ver docstring
Space a     → quick fix (import, unused)
=           → formatar seleção com ruff
F           → formatar arquivo
]d          → próximo erro de lint
```

### Dicas

- Pyright usa `pyrightconfig.json` ou `pyproject.toml` `[tool.pyright]`.
- Ruff respeita `pyproject.toml` `[tool.ruff]`.
- Virtualenvs são detectados automaticamente se houver `.venv/` na raiz.

---

## PHP

| Item | Valor |
|------|-------|
| LSP | **intelephense** |
| Extensões | `.php` |
| Root markers | `composer.json` |

### Verificar

```bash
hx --health php
```

### Workflow

```
gd          → goto definition (classe, método)
Space r     → rename em todo projeto
Space k     → documentação de função/método
gr          → encontrar usos de método
```

### Dicas

- Intelephense indexa `vendor/` — aguarde na primeira abertura.
- Configure `intelephense.environment.phpVersion` em languages.toml se necessário.
- Para Laravel/Symfony, o LSP resolve namespaces via composer autoload.

---

## Go

| Item | Valor |
|------|-------|
| LSP | **gopls** |
| Extensões | `.go` |
| Root markers | `go.mod` |

### Verificar

```bash
hx --health go
```

### Workflow

```
gd          → goto definition
gi          → goto implementation (interfaces)
Space k     → documentação
=           → gofmt na seleção
```

### Dicas

- Gopls formata automaticamente com `go fmt` quando `auto-format = true`.
- Organize imports automaticamente ao salvar.
- `go.mod` deve estar na raiz para o LSP iniciar.

---

## Rust

| Item | Valor |
|------|-------|
| LSP | **rust-analyzer** |
| Extensões | `.rs` |
| Root markers | `Cargo.toml` |

### Verificar

```bash
hx --health rust
```

### Workflow

```
gd          → goto definition
gy          → goto type definition
Space a     → assist (add derive, import, etc.)
=           → rustfmt
```

### Dicas

- Rust-analyzer é o LSP oficial da comunidade Rust.
- Inlay hints mostram tipos inferidos — muito útil.
- Code actions incluem "Add derive", "Extract function", "Inline variable".

---

## JavaScript / TypeScript / React

| Item | Valor |
|------|-------|
| LSP | **typescript-language-server** |
| Extensões | `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs` |
| Root markers | `package.json`, `tsconfig.json` |

### Verificar

```bash
hx --health typescript
hx --health tsx
```

### Workflow

```
gd          → goto definition
gi          → goto implementation
Space k     → JSDoc / type info
Space r     → rename symbol
Ctrl-x      → autocomplete com tipos
```

### Dicas

- TLS usa `tsconfig.json` para resolver paths e tipos.
- Para React, instale `@types/react` no projeto.
- JSX/TSX usam o mesmo LSP com grammars diferentes.

---

## HTML / CSS

| Item | Valor |
|------|-------|
| HTML LSP | **vscode-html-language-server** |
| CSS LSP | **vscode-css-language-server** |
| Extensões | `.html`, `.htm`, `.css`, `.scss` |

### Verificar

```bash
hx --health html
hx --health css
```

### Workflow

```
gd          → goto definition (em templates com LSP)
Space k     → documentação de tag/propriedade CSS
```

---

## SQL

| Item | Valor |
|------|-------|
| LSP | **sqls** |
| Extensões | `.sql` |
| Config | `~/.config/helix/languages.toml` |

### Verificar

```bash
hx --health sql
```

### Configurar conexões

Edite `languages.toml`:

```toml
[language-server.sqls]
command = "sqls"
config = { sqls = { connections = [
  { driver = "postgresql", dataSourceName = "host=127.0.0.1 port=5432 user=SEU_USUARIO dbname=SEU_BANCO sslmode=disable" },
] } }
```

### Workflow

```
Space k     → documentação de tabela/coluna (com conexão ativa)
gd          → goto (quando suportado)
```

### Dicas

- Sqls precisa de conexão com banco para autocomplete de tabelas/colunas.
- Suporta PostgreSQL, MySQL, SQLite, SQL Server, Oracle.

---

## JSON / YAML / TOML

| Linguagem | LSP |
|-----------|-----|
| JSON | vscode-json-language-server |
| YAML | yaml-language-server |
| TOML | taplo |

Essenciais para configs de CI/CD, Docker, Kubernetes, e `pyproject.toml`.

---

## Markdown

| Item | Valor |
|------|-------|
| LSP | **marksman** |
| Extensões | `.md`, `.markdown` |

Útil para documentação do projeto (como estes manuais).

---

## Tabela resumo

| Linguagem | LSP | Formatter | Auto-format |
|-----------|-----|-----------|-------------|
| Python | pyright + ruff | ruff | Sim |
| PHP | intelephense | — | Sim |
| Go | gopls | gofmt (via gopls) | Sim |
| Rust | rust-analyzer | rustfmt | Sim |
| JS/TS/JSX/TSX | typescript-language-server | — | Sim |
| HTML | vscode-html-language-server | — | Sim |
| CSS | vscode-css-language-server | — | Sim |
| SQL | sqls | — | Não |
| JSON | vscode-json-language-server | — | Sim |
| YAML | yaml-language-server | — | Sim |
| TOML | taplo | — | Sim |
| Markdown | marksman | — | Não |

## Próximo passo

[14 — Macros e Automação](./14-macros-e-automacao.md)
