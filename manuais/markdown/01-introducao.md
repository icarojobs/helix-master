# 01 — Introdução ao Helix Editor

## O que é o Helix?

O **Helix** é um editor de texto modal, escrito em Rust, inspirado no **Kakoune** e no **Vim**. Ele combina:

- **Edição modal** — você alterna entre modos (normal, insert, select) em vez de ficar sempre no modo de digitação.
- **Seleções primeiro** — toda operação atua sobre uma *seleção* (região de texto), não sobre um cursor solto.
- **Tree-sitter nativo** — syntax highlighting, textobjects e navegação estrutural sem plugins.
- **LSP integrado** — Language Server Protocol embutido: autocomplete, diagnósticos, goto definition, rename, etc.
- **Zero configuração obrigatória** — funciona out-of-the-box; configuração é opcional e poderosa.

## Por que usar o Helix?

| Vantagem | Descrição |
|----------|-----------|
| Performance | Binário nativo em Rust, startup instantâneo |
| Simplicidade | Sem ecossistema de plugins — tudo embutido |
| LSP de primeira classe | Suporte LSP é core, não add-on |
| Tree-sitter | AST real para seleção de funções, classes, etc. |
| Modal editing | Menos movimentos de mão, edição mais precisa |

## Helix vs Vim/Neovim

| Aspecto | Helix | Vim/Neovim |
|---------|-------|------------|
| Modelo | Seleção → ação (Kakoune) | Cursor → comando (Vim) |
| Plugins | Não suporta | Ecossistema enorme |
| Config | TOML simples | Lua/Vimscript |
| LSP | Nativo | Via plugin (nvim-lspconfig, etc.) |
| Curva de aprendizado | Moderada | Alta (Neovim) / Média (Vim) |
| Extensibilidade | Limitada | Ilimitada |

## Conceitos fundamentais

### 1. Modos

- **Normal** — modo padrão; você navega e comanda.
- **Insert** — digitação de texto (`i`, `a`, `o`).
- **Select** — estende a seleção com movimentos (`v`).

### 2. Seleções

No Helix, o cursor é sempre uma seleção (mesmo que de um caractere). Comandos como `d` (delete), `y` (yank), `c` (change) operam sobre a seleção atual.

### 3. Operadores + Movimentos

Padrão Kakoune: primeiro você *seleciona* o alvo, depois *age*.

```
x       → seleciona linha inteira
d       → deleta a seleção
c       → deleta e entra em insert mode
y       → copia (yank) a seleção
```

### 4. Sub-modos (prefixos)

Teclas que abrem "camadas" de atalhos:

| Prefixo | Nome | Exemplo |
|---------|------|---------|
| `g` | Goto | `gd` = goto definition |
| `m` | Match | `mm` = matching bracket |
| `z` | View | `zz` = centralizar linha |
| `Space` | Space | `Space f` = file picker |
| `Ctrl-w` | Window | `Ctrl-w v` = split vertical |

## Comandos básicos para começar

```
hx arquivo.py          # Abrir arquivo
hx .                   # Abrir diretório
hx -c config.toml      # Usar config alternativa
:q                     # Sair
:w                     # Salvar
:wq                    # Salvar e sair
:config-open           # Abrir config.toml
:config-reload         # Recarregar configuração
:help                  # Ajuda interativa
```

## Próximo passo

Continue para [02 — Instalação e Configuração](./02-instalacao-e-configuracao.md) para ver o setup desta máquina.
