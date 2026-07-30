# Helix Master

Documentação completa em **português do Brasil** para domínio total do [Helix Editor](https://helix-editor.com/).

## Duas trilhas

| Trilha | Pasta | Formato |
|--------|-------|---------|
| **Interativa** (recomendada) | [`manuais/iterativo/`](./manuais/iterativo/README.md) | Slides HTML — teoria + mão na massa |
| **Markdown** | [`manuais/markdown/`](./manuais/markdown/README.md) | Referência escrita |

**Comece aqui:** abra `manuais/iterativo/00 - Roadmap e Pré-requisitos.html` no navegador.

## Setup rápido

```bash
# Helix
sudo snap install helix --classic    # Linux Debian/Ubuntu/Pop!_OS
brew install helix                   # macOS

# LSPs + configs
bash exemplos/install-lsps-linux.sh  # ou install-lsps-macos.sh
mkdir -p ~/.config/helix
cp exemplos/config.toml exemplos/languages.toml ~/.config/helix/

# Verificar
hx --health python && hx .
```

## Estrutura

```
helix-master/
├── manuais/
│   ├── iterativo/     # 18 aulas HTML (00–17)
│   └── markdown/      # 18 manuais MD (00–17)
├── exemplos/          # config.toml, languages.toml, scripts LSP
└── scripts/           # gerar_iterativo.py
```

## Stack coberta

Python · PHP · Go · Rust · HTML · CSS · JavaScript · TypeScript · React · SQL · YAML · TOML · Markdown

## Licença

MIT — veja [LICENSE](./LICENSE).
