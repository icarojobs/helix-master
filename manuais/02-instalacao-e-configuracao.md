# 02 — Instalação e Configuração

## Instalação nesta máquina

| Item | Detalhe |
|------|---------|
| SO | Pop!_OS 22.04 LTS |
| Versão | Helix **25.07.1** |
| Método | Snap classic (`snap install helix --classic`) |
| Binário | `/snap/bin/hx` |

### Verificar instalação

```bash
hx --version
# helix 25.07.1 (a05c151b)
```

### Atualizar (quando necessário)

```bash
sudo snap refresh helix
```

## Estrutura de configuração

```
~/.config/helix/
├── config.toml       # Tema, editor, atalhos personalizados
├── languages.toml    # Language servers e formatadores
└── themes/           # Temas customizados (opcional)

# Por projeto:
projeto/.helix/
├── config.toml
└── languages.toml
```

A configuração é **mesclada** nesta ordem (última prevalece):
1. Built-in (Helix)
2. `~/.config/helix/`
3. `.helix/` do projeto

## Configuração aplicada

### `config.toml` — destaques

| Configuração | Valor | Efeito |
|--------------|-------|--------|
| `theme` | `catppuccin_mocha` | Tema escuro popular |
| `line-number` | `relative` | Números relativos à linha atual |
| `auto-save` | `true` | Salva automaticamente |
| `auto-format` | `true` | Formata ao salvar (quando há formatter) |
| `cursorline` | `true` | Destaca linha do cursor |
| `display-inlay-hints` | `true` | Dicas inline do LSP |
| `scrolloff` | `8` | Margem de scroll |

### Atalhos personalizados adicionados

| Atalho | Ação |
|--------|------|
| `Ctrl+s` | Salvar (`:w`) |
| `Ctrl+Shift+s` | Salvar e sair (`:wq`) |
| `Ctrl+q` | Sair (`:q`) |
| `Ctrl+h/j/k/l` | Navegar entre splits |
| `{` / `}` | Diagnóstico anterior / próximo |
| `F` | Formatar arquivo |
| `S` | Selecionar linha inteira |

## Language Servers instalados

### Verificar saúde

```bash
hx --health python
hx --health go
hx --health rust
# etc.
```

### Tabela de LSPs

| Linguagem | LSP | Binário | Instalação |
|-----------|-----|---------|------------|
| Python | pyright + ruff | `~/.local/bin/` | `pip3 install --user ruff pyright` |
| PHP | intelephense | `~/.local/bin/` | `npm install -g --prefix ~/.local intelephense` |
| Go | gopls | `~/go/bin/` | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer | `~/.cargo/bin/` | `rustup component add rust-analyzer` |
| JS/TS/React | typescript-language-server | `~/.local/bin/` | `npm install -g --prefix ~/.local typescript typescript-language-server` |
| HTML | vscode-html-language-server | `~/.local/bin/` | via `vscode-langservers-extracted` |
| CSS | vscode-css-language-server | `~/.local/bin/` | via `vscode-langservers-extracted` |
| JSON | vscode-json-language-server | `~/.local/bin/` | via `vscode-langservers-extracted` |
| SQL | sqls | `~/go/bin/` | `go install github.com/sqls-server/sqls@latest` |
| YAML | yaml-language-server | `~/.local/bin/` | `npm install -g --prefix ~/.local yaml-language-server` |
| TOML | taplo | `~/.cargo/bin/` | `cargo install taplo-cli --locked` |
| Markdown | marksman | `~/.local/bin/` | binário do GitHub releases |

### PATH necessário

Adicionado ao `~/.bashrc`:

```bash
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
```

Certifique-se de que `~/.local/bin` e `~/.cargo/bin` também estão no PATH.

## Configuração SQL (sqls)

O arquivo `languages.toml` inclui conexões de exemplo para PostgreSQL, MySQL e SQLite. Ajuste conforme seu ambiente:

```toml
[language-server.sqls]
command = "sqls"
config = { sqls = { connections = [
  { driver = "postgresql", dataSourceName = "host=127.0.0.1 port=5432 user=SEU_USUARIO dbname=SEU_BANCO sslmode=disable" },
] } }
```

## Recarregar configuração

Dentro do Helix:

```
:config-reload
```

Ou via terminal (recarrega todos os processos hx):

```bash
pkill -USR1 hx
```

## Troubleshooting

| Problema | Solução |
|----------|---------|
| LSP não encontrado | `hx --health <lang>` e instale o binário indicado |
| LSP não inicia | Verifique `roots` do projeto (ex: `package.json`, `go.mod`) |
| Formatação não funciona | Confirme `auto-format = true` e formatter configurado |
| Tema não aparece | Liste temas com `:theme` dentro do Helix |

## Próximo passo

[03 — Filosofia Modal](./03-filosofia-modal.md)
