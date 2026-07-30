# Manuais Helix Master

Duas trilhas complementares para domínio total do [Helix Editor](https://helix-editor.com/):

| Trilha | Pasta | Formato | Quando usar |
|--------|-------|---------|-------------|
| **Markdown** | [`markdown/`](./markdown/README.md) | Referência escrita | Consulta, busca, leitura offline |
| **Interativo** | [`iterativo/`](./iterativo/README.md) | Slides HTML | Estudo guiado teoria + mão na massa |

## Ordem recomendada

Siga **00 → 17** na trilha interativa. Use o Markdown como apoio e referência.

```
manuais/iterativo/00 - Roadmap e Pré-requisitos.html   ← comece aqui
manuais/iterativo/01 - Introdução ao Helix.html
...
manuais/iterativo/17 - Terminal e Sessões Persistentes.html
```

## Setup rápido

```bash
# Configs e LSPs
bash exemplos/install-lsps-linux.sh    # ou install-lsps-macos.sh
cp exemplos/config.toml ~/.config/helix/
cp exemplos/languages.toml ~/.config/helix/

# Abrir trilha interativa
xdg-open manuais/iterativo/00\ -\ Roadmap\ e\ Pré-requisitos.html   # Linux
open manuais/iterativo/00\ -\ Roadmap\ e\ Pré-requisitos.html      # macOS
```

## Regenerar slides HTML

```bash
python3 scripts/gerar_iterativo.py
```
