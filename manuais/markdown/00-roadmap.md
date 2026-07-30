# 00 — Roadmap e Pré-requisitos

## Duas trilhas, um objetivo

Este repositório oferece **duas formas** de aprender o Helix:

| Trilha | Onde | Ideal para |
|--------|------|------------|
| **Interativa** | `manuais/iterativo/*.html` | Estudo guiado com slides (teoria + mão na massa) |
| **Markdown** | `manuais/markdown/*.md` | Consulta e referência escrita |

Recomendação: siga a trilha **interativa na ordem 00→17** e use o Markdown como apoio.

## Estrutura da trilha (18 aulas)

| Aulas | Módulo |
|-------|--------|
| 00–02 | Instalação e fundamentos |
| 03–05 | Modal, movimentação e edição |
| 06–08 | Atalhos, goto e LSP |
| 09–11 | Busca, buffers e comandos |
| 12–14 | Config avançada, linguagens e macros |
| 15–17 | Workflow, referência e tmux |

## Pré-requisitos

### Sistemas operacionais suportados

- **Linux:** Debian, Ubuntu, Pop!_OS, Mint e derivados
- **macOS:** com Homebrew

### Ferramentas necessárias

| Ferramenta | Linux | macOS |
|------------|-------|-------|
| Terminal | `Ctrl+Alt+T` | Terminal.app / iTerm2 |
| Python 3 + pip | `apt install python3-pip` | `brew install python@3` |
| Node.js + npm | nodejs.org ou nvm | `brew install node` |
| Go | go.dev/dl | `brew install go` |
| Rust (opcional) | rustup.rs | `brew install rust` |
| Git | `apt install git` | `brew install git` |

### Permissões

- Instalar pacotes (`sudo` no Linux)
- Escrever em `~/.config/helix/`

## Metodologia (trilha interativa)

Cada aula HTML segue:

1. **O que é?** — conceito
2. **Quando usar?** — contexto real
3. **Como usar?** — atalhos e exemplos
4. **Mão na massa** — comandos completos no terminal
5. **Dicas profissionais**
6. **Recapitulando**
7. **Próxima aula**

## Como começar

```bash
git clone https://github.com/icarojobs/helix-master.git
cd helix-master

# Abra a Aula 00 no navegador
xdg-open "manuais/iterativo/00 - Roadmap e Pré-requisitos.html"   # Linux
open "manuais/iterativo/00 - Roadmap e Pré-requisitos.html"        # macOS
```

## Arquivos de apoio

```
helix-master/
├── exemplos/
│   ├── config.toml              # atalhos + editor
│   ├── languages.toml           # LSPs
│   ├── install-lsps-linux.sh
│   └── install-lsps-macos.sh
├── manuais/
│   ├── markdown/                # esta trilha
│   └── iterativo/               # slides HTML
└── scripts/
    └── gerar_iterativo.py       # regenerar slides
```

## Próximo passo

- Interativo: [01 - Introdução ao Helix.html](../iterativo/01%20-%20Introdução%20ao%20Helix.html)
- Markdown: [01 — Introdução](./01-introducao.md)
