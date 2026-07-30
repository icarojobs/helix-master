# Trilha Interativa — Helix Master

Slides HTML no padrão **cursos-youtube**: teoria → mão na massa → recapitulando.

## Como usar

1. Abra os slides no **navegador** (monitor 2)
2. Execute os comandos no **terminal** (monitor 1)
3. Navegue com **← →** ou **Espaço** · **F** = tela cheia

```bash
# Linux
xdg-open "manuais/iterativo/00 - Roadmap e Pré-requisitos.html"

# macOS
open "manuais/iterativo/00 - Roadmap e Pré-requisitos.html"
```

## Aulas (siga nesta ordem)

| # | Arquivo | Módulo | Cor |
|---|---------|--------|-----|
| 00 | [Roadmap e Pré-requisitos](./00%20-%20Roadmap%20e%20Pré-requisitos.html) | Fundamentos | Verde |
| 01 | [Introdução ao Helix](./01%20-%20Introdução%20ao%20Helix.html) | Fundamentos | Verde |
| 02 | [Instalação e Configuração](./02%20-%20Instalação%20e%20Configuração.html) | Fundamentos | Verde |
| 03 | [Filosofia Modal](./03%20-%20Filosofia%20Modal.html) | Edição | Ciano |
| 04 | [Movimentação e Navegação](./04%20-%20Movimentação%20e%20Navegação.html) | Edição | Ciano |
| 05 | [Edição e Seleções](./05%20-%20Edição%20e%20Seleções.html) | Edição | Ciano |
| 06 | [Atalhos Essenciais](./06%20-%20Atalhos%20Essenciais.html) | Atalhos/LSP | Roxo |
| 07 | [Modo Goto e Space](./07%20-%20Modo%20Goto%20e%20Space.html) | Atalhos/LSP | Roxo |
| 08 | [LSP e Inteligência](./08%20-%20LSP%20e%20Inteligência.html) | Atalhos/LSP | Roxo |
| 09 | [Busca e Substituição](./09%20-%20Busca%20e%20Substituição.html) | Busca | Laranja |
| 10 | [Buffers e Janelas](./10%20-%20Buffers%20e%20Janelas.html) | Busca | Laranja |
| 11 | [Comandos e Pickers](./11%20-%20Comandos%20e%20Pickers.html) | Busca | Laranja |
| 12 | [Configuração Avançada](./12%20-%20Configuração%20Avançada.html) | Avançado | Amarelo |
| 13 | [Linguagens de Programação](./13%20-%20Linguagens%20de%20Programação.html) | Avançado | Amarelo |
| 14 | [Macros e Automação](./14%20-%20Macros%20e%20Automação.html) | Avançado | Amarelo |
| 15 | [Dicas e Workflow](./15%20-%20Dicas%20e%20Workflow.html) | Maestria | Vermelho |
| 16 | [Referência Rápida](./16%20-%20Referência%20Rápida.html) | Maestria | Vermelho |
| 17 | [Terminal e Sessões Persistentes](./17%20-%20Terminal%20e%20Sessões%20Persistentes.html) | Maestria | Verde |

## Referência escrita

Consulte [`manuais/markdown/`](../markdown/README.md) para a versão em texto.

## Regenerar slides

```bash
python3 scripts/gerar_iterativo.py
```

O template CSS/JS segue o núcleo intocável de `cursos-youtube`.
