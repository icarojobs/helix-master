# Helix Master

Documentação completa em **português do Brasil** para domínio total do [Helix Editor](https://helix-editor.com/), com guias de instalação (Linux e macOS), atalhos, LSP, terminal e sessões persistentes (tmux).

## Conteúdo

Todos os manuais estão em [`manuais/`](./manuais/README.md).

| # | Manual | Tópico |
|---|--------|--------|
| **02** | [Instalação e Configuração](./manuais/02-instalacao-e-configuracao.md) | **Debian/macOS, LSPs, atalhos, configs** |
| 01–16 | Fundamentos → Referência | Modos, atalhos, LSP, busca, splits |
| **17** | [Terminal e Sessões Persistentes](./manuais/17-terminal-e-sessoes-persistentes.md) | tmux, sobrevivência a reboot |

## Setup rápido

```bash
# Instalar Helix
sudo snap install helix --classic    # Linux (Debian/Ubuntu/Pop!_OS)
brew install helix                   # macOS

# Instalar language servers
bash exemplos/install-lsps-linux.sh  # Linux
bash exemplos/install-lsps-macos.sh  # macOS

# Copiar configuração (atalhos + LSP)
mkdir -p ~/.config/helix
cp exemplos/config.toml ~/.config/helix/
cp exemplos/languages.toml ~/.config/helix/

# Verificar
hx --health python
hx .
```

## Arquivos de exemplo

| Arquivo | Conteúdo |
|---------|----------|
| [`exemplos/config.toml`](./exemplos/config.toml) | Tema, editor, **todos os atalhos** |
| [`exemplos/languages.toml`](./exemplos/languages.toml) | **Todos os LSPs** da stack full-stack |
| [`exemplos/install-lsps-linux.sh`](./exemplos/install-lsps-linux.sh) | Script de instalação LSP (Linux) |
| [`exemplos/install-lsps-macos.sh`](./exemplos/install-lsps-macos.sh) | Script de instalação LSP (macOS) |

## Stack coberta

Python · PHP · Go · Rust · HTML · CSS · JavaScript · TypeScript · React · SQL · YAML · TOML · Markdown

## Licença

MIT — veja [LICENSE](./LICENSE).
