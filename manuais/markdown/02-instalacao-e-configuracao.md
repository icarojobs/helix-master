# 02 — Instalação e Configuração

Guia completo: instalar o Helix em **Debian/Ubuntu/Pop!_OS** e **macOS**, configurar atalhos e instalar todos os language servers (LSP).

---

## Parte 1 — Instalar o Helix

### Linux — Debian / Ubuntu / Pop!_OS / Mint

#### Opção A: Snap (recomendada — mais simples)

```bash
sudo snap install helix --classic
hx --version
```

Atualizar:

```bash
sudo snap refresh helix
```

#### Opção B: Binário oficial (GitHub Releases)

```bash
# Baixar última release (ajuste a versão se necessário)
HELIX_VERSION="25.07.1"
ARCH="x86_64-unknown-linux-gnu"   # use aarch64-unknown-linux-gnu em ARM

curl -fsSL "https://github.com/helix-editor/helix/releases/download/${HELIX_VERSION}/helix-${HELIX_VERSION}-${ARCH}.tar.xz" \
  -o /tmp/helix.tar.xz

tar -xf /tmp/helix.tar.xz -C /tmp
sudo mv /tmp/helix-${HELIX_VERSION}/hx /usr/local/bin/hx
sudo mv /tmp/helix-${HELIX_VERSION}/runtime /usr/local/share/helix

hx --version
```

> O diretório `runtime` é obrigatório — contém grammars tree-sitter e temas.

#### Opção C: Compilar do source (avançado)

```bash
sudo apt install -y git build-essential pkg-config \
  libssl-dev libgit2-dev

git clone https://github.com/helix-editor/helix.git
cd helix
cargo install --path helix-term --locked --force
```

---

### macOS

#### Opção A: Homebrew (recomendada)

```bash
brew install helix
hx --version
```

Atualizar:

```bash
brew upgrade helix
```

#### Opção B: MacPorts

```bash
sudo port install helix
```

#### Opção C: Binário oficial

```bash
HELIX_VERSION="25.07.1"
ARCH="aarch64-apple-darwin"   # Apple Silicon; use x86_64-apple-darwin em Intel

curl -fsSL "https://github.com/helix-editor/helix/releases/download/${HELIX_VERSION}/helix-${HELIX_VERSION}-${ARCH}.tar.xz" \
  -o /tmp/helix.tar.xz

tar -xf /tmp/helix.tar.xz -C /tmp
sudo mv /tmp/helix-${HELIX_VERSION}/hx /usr/local/bin/hx
sudo mv /tmp/helix-${HELIX_VERSION}/runtime /usr/local/share/helix
```

---

### Verificar instalação

```bash
which hx
hx --version
# Esperado: helix 25.07.x
```

---

## Parte 2 — Pré-requisitos para LSPs

Antes de instalar os language servers, garanta estas ferramentas:

| Ferramenta | Debian/Ubuntu | macOS (Homebrew) |
|------------|---------------|------------------|
| Python 3 + pip | `sudo apt install python3 python3-pip` | `brew install python@3` |
| Node.js + npm | [nodejs.org](https://nodejs.org) ou `nvm` | `brew install node` |
| Go | [go.dev/dl](https://go.dev/dl/) | `brew install go` |
| Rust + Cargo | `curl -sSf https://sh.rustup.rs \| sh` | `brew install rust` |
| Git | `sudo apt install git` | `brew install git` |
| curl | já incluso | já incluso |

---

## Parte 3 — Instalar Language Servers (LSP)

### Instalação automatizada (recomendada)

O repositório inclui scripts prontos:

```bash
# Linux (Debian/Ubuntu/Pop!_OS)
bash exemplos/install-lsps-linux.sh

# macOS
bash exemplos/install-lsps-macos.sh
```

Reinicie o terminal após a instalação.

### Instalação manual — referência completa

| Linguagem | LSP | Comando de instalação |
|-----------|-----|----------------------|
| Python | pyright + ruff | `pip3 install --user ruff pyright` |
| PHP | intelephense | `npm install -g intelephense` |
| Go | gopls | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer | `rustup component add rust-analyzer` |
| JS/TS/React | typescript-language-server | `npm install -g typescript typescript-language-server` |
| HTML/CSS/JSON | vscode-langservers-extracted | `npm install -g vscode-langservers-extracted` |
| SQL | sqls | `go install github.com/sqls-server/sqls@latest` |
| YAML | yaml-language-server | `npm install -g yaml-language-server` |
| TOML | taplo | `cargo install taplo-cli --locked` |
| Markdown | marksman | `brew install marksman` (macOS) ou binário do [GitHub](https://github.com/artempyanykh/marksman/releases) |

### Configurar PATH

Os binários precisam estar no `$PATH`. Adicione ao seu shell:

**Linux (`~/.bashrc`):**

```bash
export PATH="$HOME/.local/bin:$PATH"
export PATH="$PATH:/usr/local/go/bin:$HOME/go/bin"
. "$HOME/.cargo/env"
```

**macOS (`~/.zshrc`):**

```bash
export PATH="$HOME/.local/bin:$PATH"
export PATH="$PATH:$HOME/go/bin"
. "$HOME/.cargo/env"
```

Recarregue:

```bash
source ~/.bashrc   # Linux
source ~/.zshrc    # macOS
```

### Verificar saúde dos LSPs

```bash
hx --health python
hx --health php
hx --health go
hx --health rust
hx --health typescript
hx --health tsx
hx --health html
hx --health css
hx --health sql
hx --health yaml
hx --health toml
hx --health markdown
```

Saída esperada: `✓` verde para cada language server. Se aparecer `✘`, instale o binário indicado.

---

## Parte 4 — Configurar o Helix

### Estrutura de diretórios

```
~/.config/helix/
├── config.toml       # Tema, editor, atalhos
├── languages.toml    # LSPs e formatadores
└── themes/           # Temas customizados (opcional)

# Por projeto (opcional):
projeto/.helix/
├── config.toml
└── languages.toml
```

Ordem de mesclagem (última prevalece): built-in → `~/.config/helix/` → `.helix/` do projeto.

### Setup rápido (copiar arquivos prontos)

```bash
mkdir -p ~/.config/helix

# Clone ou baixe este repositório, depois:
cp exemplos/config.toml    ~/.config/helix/config.toml
cp exemplos/languages.toml ~/.config/helix/languages.toml
```

Ou, se já estiver dentro do repositório `helix-master`:

```bash
mkdir -p ~/.config/helix
cp ~/projects/icarojobs/helix-master/exemplos/config.toml    ~/.config/helix/
cp ~/projects/icarojobs/helix-master/exemplos/languages.toml ~/.config/helix/
```

Recarregue dentro do Helix:

```
:config-reload
```

---

## Parte 5 — Setup completo de atalhos

O arquivo `exemplos/config.toml` já inclui todos os atalhos recomendados. Abaixo, o que cada grupo faz:

### Atalhos de arquivo

| Atalho | Modo | Ação | Config |
|--------|------|------|--------|
| `Ctrl+s` | normal | Salvar | `C-s = ":w"` |
| `Ctrl+Shift+s` | normal | Salvar e sair | `C-S = ":wq"` |
| `Ctrl+q` | normal | Sair | `C-q = ":q"` |
| `Ctrl+s` | insert | Salvar e voltar ao normal | `C-s = [":w", "normal_mode"]` |

### Navegação entre splits

| Atalho | Ação | Config |
|--------|------|--------|
| `Ctrl+h` | Split à esquerda | `C-h = "jump_view_left"` |
| `Ctrl+j` | Split abaixo | `C-j = "jump_view_down"` |
| `Ctrl+k` | Split acima | `C-k = "jump_view_up"` |
| `Ctrl+l` | Split à direita | `C-l = "jump_view_right"` |

### LSP e formatação

| Atalho | Ação | Config |
|--------|------|--------|
| `{` | Diagnóstico anterior | `"{" = "goto_prev_diag"` |
| `}` | Próximo diagnóstico | `"}" = "goto_next_diag"` |
| `F` | Formatar arquivo | `F = ":format"` |
| `S` | Selecionar linha inteira | `S = "extend_to_line_bounds"` |

### Atalhos nativos importantes (não precisam de config)

| Atalho | Ação |
|--------|------|
| `gd` | Goto definition |
| `gr` | Goto references |
| `Space k` | Hover |
| `Space a` | Code action |
| `Space r` | Rename symbol |
| `Space f` | File picker |
| `Space /` | Busca global |
| `]d` / `[d` | Próximo/anterior diagnóstico |
| `Ctrl+c` | Comentar/descomentar |
| `Ctrl+x` (insert) | Autocomplete |

### Adicionar seus próprios atalhos

Edite `~/.config/helix/config.toml`:

```toml
[keys.normal]
# Exemplo: Alt+w para salvar
A-w = ":w"

# Exemplo: desabilitar uma tecla
Q = "no_op"
```

Lista completa de comandos: `:help` dentro do Helix ou [manual 06](./06-atalhos-essenciais.md).

---

## Parte 6 — Setup completo de LSP

O arquivo `exemplos/languages.toml` configura todos os LSPs da stack full-stack.

### O que está configurado

| Linguagem | LSPs | Auto-format |
|-----------|------|-------------|
| Python | pyright + ruff | Sim (ruff) |
| PHP | intelephense (built-in) | Sim |
| Go | gopls (built-in) | Sim |
| Rust | rust-analyzer (built-in) | Sim |
| JS/TS/JSX/TSX | typescript-language-server | Sim |
| HTML/CSS/JSON | vscode-*-language-server | Sim |
| SQL | sqls | Não |
| YAML | yaml-language-server | Sim |
| TOML | taplo | Sim |
| Markdown | marksman | Não |

### Configurar conexão SQL

Edite `~/.config/helix/languages.toml`:

```toml
[language-server.sqls]
command = "sqls"
config = { sqls = { connections = [
  { driver = "postgresql", dataSourceName = "host=127.0.0.1 port=5432 user=SEU_USUARIO dbname=SEU_BANCO sslmode=disable" },
] } }
```

> **Nunca** commite credenciais reais. Use placeholders e variáveis de ambiente no seu ambiente local.

### Override por projeto

Para config específica de um projeto, crie `.helix/languages.toml`:

```toml
# meu-projeto/.helix/languages.toml
[[language]]
name = "python"
language-servers = ["pyright", "ruff"]
auto-format = true
```

### Testar LSP após configurar

```bash
cd ~/seu-projeto
hx --health python    # deve mostrar ✓ para pyright e ruff
hx .                # abrir projeto — LSP inicia automaticamente
```

Dentro do Helix, abra um arquivo `.py` e teste:
- `Ctrl+x` (insert mode) → autocomplete
- `gd` → goto definition
- `Space k` → hover

---

## Parte 7 — Opções do editor configuradas

| Configuração | Valor | Efeito |
|--------------|-------|--------|
| `theme` | `catppuccin_mocha` | Tema escuro |
| `line-number` | `relative` | Números relativos |
| `auto-save` | `true` | Salva automaticamente |
| `auto-format` | `true` | Formata ao salvar |
| `cursorline` | `true` | Destaca linha do cursor |
| `display-inlay-hints` | `true` | Tipos inline do LSP |
| `auto-signature-help` | `true` | Assinatura de função ao digitar `(` |
| `scrolloff` | `8` | Margem de scroll |
| `completion-trigger-len` | `2` | Autocomplete após 2 chars |

---

## Parte 8 — Checklist pós-instalação

```
[ ] hx --version funciona
[ ] ~/.config/helix/config.toml copiado
[ ] ~/.config/helix/languages.toml copiado
[ ] PATH configurado (~/.local/bin, ~/go/bin, ~/.cargo/bin)
[ ] hx --health python → ✓
[ ] hx --health go → ✓
[ ] hx --health typescript → ✓
[ ] :config-reload dentro do Helix
[ ] Autocomplete funciona (Ctrl+x em insert mode)
[ ] Goto definition funciona (gd)
```

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| `hx: command not found` | Reinstale ou adicione ao PATH |
| LSP `✘ not found in $PATH` | Instale o binário; verifique PATH |
| LSP não inicia no projeto | Confirme marcador de raiz (`go.mod`, `package.json`, etc.) |
| Snap não vê LSPs | Snap isola PATH — use binário em `/usr/local/bin` ou ajuste `PATH` no `.bashrc` |
| Cores erradas no macOS | `true-color = true` + terminal com suporte (iTerm2, WezTerm, Terminal.app) |
| Formatação não funciona | `auto-format = true` + formatter configurado em `languages.toml` |
| Atalho não funciona | Conflito com terminal — veja [manual 15](./15-dicas-workflow.md) |

---

## Próximo passo

[00 — Roadmap e Pré-requisitos](../markdown/00-roadmap.md) · [03 — Filosofia Modal](./03-filosofia-modal.md) · [Trilha interativa](../iterativo/02%20-%20Instalação%20e%20Configuração.html) · [06 — Atalhos Essenciais](./06-atalhos-essenciais.md) · [08 — LSP e Inteligência](./08-lsp-e-inteligencia.md)
