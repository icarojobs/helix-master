# 12 — Configuração Avançada

## Arquivos de configuração

| Arquivo | Escopo | Conteúdo |
|---------|--------|----------|
| `~/.config/helix/config.toml` | Global | Tema, editor, keymaps |
| `~/.config/helix/languages.toml` | Global | LSPs, formatadores |
| `projeto/.helix/config.toml` | Projeto | Overrides locais |
| `projeto/.helix/languages.toml` | Projeto | LSPs específicos do projeto |

Mesclagem: built-in → global → projeto (último prevalece).

## config.toml — seções principais

### Tema e aparência

```toml
theme = "catppuccin_mocha"
true-color = true
```

Temas built-in populares: `onedark`, `dracula`, `nord`, `catppuccin_mocha`, `catppuccin_latte`, `base16_default_dark`, `gruvbox`, `rose_pine`.

Liste todos com `:theme` dentro do Helix.

### Editor

```toml
[editor]
line-number = "relative"       # "absolute" | "relative"
cursorline = true
auto-save = true
auto-format = true
mouse = true
scrolloff = 8
tab-width = 4
soft-wrap.enable = true
color-modes = true               # cores por modo (normal/insert/select)
```

### Statusline

```toml
[editor.statusline]
left = ["mode", "spinner", "file-name", "read-only-indicator"]
center = ["workspace-diagnostics"]
right = ["diagnostic", "selections", "position", "file-type"]
```

Componentes disponíveis: `mode`, `spinner`, `file-name`, `file-base-name`, `file-modification-indicator`, `read-only-indicator`, `diagnostic`, `selections`, `register`, `position`, `position-percentage`, `file-encoding`, `file-line-ending`, `file-type`, `file-root`, `workspace-diagnostics`.

### LSP

```toml
[editor.lsp]
display-messages = true
display-inlay-hints = true
auto-signature-help = true
snippet = true

[editor.lsp.request]
timeout = 30
```

### Indent guides

```toml
[editor.indent-guides]
render = true
character = "│"
skip-levels = 1
```

### File picker

```toml
[editor.file-picker]
hidden = false
follow-symlinks = true

[editor.file-search]
ignore = [".git", "node_modules", "target", "vendor"]
```

### Cursor shape

```toml
[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"
```

## Keymaps personalizados

```toml
[keys.normal]
C-s = ":w"
"{" = "goto_prev_diag"
"}" = "goto_next_diag"

[keys.insert]
C-s = [":w", "normal_mode"]

[keys.select]
C-s = ":w"
```

### Múltiplos comandos em sequência

```toml
C-s = [":w", "normal_mode"]    # salva e volta ao normal
```

### Desabilitar atalhos

```toml
[keys.insert]
up = "no_op"
down = "no_op"
```

## languages.toml

### Definir language server

```toml
[language-server.meu-lsp]
command = "meu-lsp"
args = ["--stdio"]
config = { key = "value" }
timeout = 30
required-root-patterns = ["package.json"]
```

### Associar LSP a linguagem

```toml
[[language]]
name = "python"
language-servers = ["pyright", "ruff"]
auto-format = true
formatter = { command = "ruff", args = ["format", "--stdin-filename", "%"], input = "pipe" }
```

### Formatter externo

```toml
formatter = { command = "prettier", args = ["--stdin-filepath", "%"] }
```

### Workspace LSP roots (monorepo)

Em `.helix/config.toml` do projeto:

```toml
[[language]]
name = "typescript"
workspace-lsp-roots = ["packages/frontend", "packages/backend"]
```

## Temas customizados

Crie `~/.config/helix/themes/meu-tema.toml`:

```toml
"ui.background" = "#1e1e2e"
"ui.foreground" = "#cdd6f4"
"ui.selection" = { bg = "#45475a" }
"ui.cursor" = { fg = "#1e1e2e", bg = "#f5e0dc" }
"ui.linenr" = "#6c7086"
"ui.linenr.selected" = "#f5e0dc"
# ... mais tokens
```

Ative com `theme = "meu-tema"` no config.toml.

## Recarregar configuração

```
:config-reload
```

Ou via sinal Unix:

```bash
pkill -USR1 hx
```

## Config por projeto (exemplo)

```
meu-projeto/.helix/
├── config.toml        # auto-format, tab-width específico
└── languages.toml     # conexões SQL do projeto
```

## Dicas avançadas

1. **Versione `.helix/`** no git do projeto para compartilhar config com o time.
2. **Use `required-root-patterns`** para LSPs que só devem ativar em certos projetos.
3. **`except-features`** / **`only-features`** controlam quais features do LSP usar.
4. **Teste com `hx --health`** após cada mudança em languages.toml.

## Próximo passo

[13 — Linguagens de Programação](./13-linguagens-de-programacao.md)
