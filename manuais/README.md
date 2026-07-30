# Manuais do Helix Editor

Documentação completa em **português do Brasil** para domínio total do [Helix Editor](https://helix-editor.com/).

## Índice

| # | Manual | Conteúdo |
|---|--------|----------|
| 01 | [Introdução](./01-introducao.md) | O que é o Helix, filosofia, comparação com Vim/Neovim |
| 02 | [Instalação e Configuração](./02-instalacao-e-configuracao.md) | Instalação Debian/macOS, LSPs, atalhos, configs |
| 03 | [Filosofia Modal](./03-filosofia-modal.md) | Modos (normal, insert, select), paradigma Kakoune |
| 04 | [Movimentação e Navegação](./04-movimentacao-e-navegacao.md) | Movimentos, jumplist, scroll, goto |
| 05 | [Edição e Seleções](./05-edicao-e-selecoes.md) | Modelo de seleção, yank/paste, surround, textobjects |
| 06 | [Atalhos Essenciais](./06-atalhos-essenciais.md) | Tabela completa + como configurar keymaps |
| 07 | [Modo Goto e Space](./07-modo-goto-e-espaco.md) | Sub-modos `g`, `Space`, LSP rápido |
| 08 | [LSP e Inteligência](./08-lsp-e-inteligencia.md) | Autocomplete, diagnósticos, rename, code actions |
| 09 | [Busca e Substituição](./09-busca-e-substituicao.md) | Busca local, global, regex, substituição |
| 10 | [Buffers, Janelas e Splits](./10-buffers-janelas-splits.md) | Splits, troca de buffer, layout |
| 11 | [Comandos e Pickers](./11-comandos-e-pickers.md) | Command mode, palette, file picker |
| 12 | [Configuração Avançada](./12-configuracao-avancada.md) | config.toml, languages.toml, temas, keymaps |
| 13 | [Linguagens de Programação](./13-linguagens-de-programacao.md) | Python, PHP, Go, Rust, Web, SQL |
| 14 | [Macros e Automação](./14-macros-e-automacao.md) | Macros, shell pipe, comandos externos |
| 15 | [Dicas e Workflow](./15-dicas-workflow.md) | Fluxo diário, produtividade, troubleshooting |
| 16 | [Referência Rápida](./16-referencia-rapida.md) | Cheatsheet de uma página |
| 17 | [Terminal e Sessões Persistentes](./17-terminal-e-sessoes-persistentes.md) | Abrir terminal, tmux, sobreviver a reboot |

## Início rápido

```bash
# Abrir arquivo
hx arquivo.py

# Abrir diretório (file picker)
hx .

# Verificar saúde dos LSPs
hx --health python

# Recarregar configuração (dentro do Helix)
:config-reload
```

## Arquivos de configuração

| Arquivo | Caminho |
|---------|---------|
| Config principal | `~/.config/helix/config.toml` |
| Language servers | `~/.config/helix/languages.toml` |
| Config por projeto | `.helix/config.toml` e `.helix/languages.toml` |
| **Exemplos prontos** | [`exemplos/`](../exemplos/) neste repositório |

## Setup rápido

```bash
# 1. Instalar Helix
sudo snap install helix --classic          # Linux
brew install helix                         # macOS

# 2. Instalar LSPs
bash exemplos/install-lsps-linux.sh        # Linux
bash exemplos/install-lsps-macos.sh        # macOS

# 3. Copiar configs
mkdir -p ~/.config/helix
cp exemplos/config.toml ~/.config/helix/
cp exemplos/languages.toml ~/.config/helix/

# 4. Verificar
hx --health python
```
