# 08 — LSP e Inteligência

> **Setup completo:** se ainda não instalou os language servers e o `languages.toml`, siga [02 — Instalação e Configuração](./02-instalacao-e-configuracao.md) (Partes 3 e 6) e use os arquivos em [`exemplos/`](../exemplos/).

## O que é LSP?

O **Language Server Protocol** permite que o editor se comunique com servidores de linguagem que fornecem:

- Autocomplete inteligente
- Diagnósticos (erros e warnings)
- Goto definition / references / implementation
- Hover (documentação inline)
- Rename symbol
- Code actions (quick fixes)
- Formatação
- Inlay hints (dicas de tipo inline)

No Helix, o LSP é **nativo** — não precisa de plugins.

## Verificar saúde do LSP

```bash
hx --health python
hx --health go
hx --health rust
```

Saída esperada: `✓` verde para cada language server configurado.

## Autocomplete

| Contexto | Atalho |
|----------|--------|
| Insert mode | `Ctrl-x` |
| Ao digitar | Automático após `completion-trigger-len` caracteres |

### Menu de completion

| Tecla | Ação |
|-------|------|
| `Tab` / `Ctrl-n` / `↓` | Próximo item |
| `Shift-Tab` / `Ctrl-p` / `↑` | Item anterior |
| `Enter` | Aceitar |
| `Ctrl-c` | Rejeitar |
| Qualquer outra tecla | Aceita e insere a tecla |

## Hover (documentação)

```
Space k     → popup com documentação do item sob cursor
```

No popup: `Ctrl-u` / `Ctrl-d` para scroll.

## Goto (navegação de código)

| Atalho | Ação | LSP request |
|--------|------|-------------|
| `gd` | Goto definition | `textDocument/definition` |
| `gy` | Goto type definition | `textDocument/typeDefinition` |
| `gr` | Goto references | `textDocument/references` |
| `gi` | Goto implementation | `textDocument/implementation` |
| `gf` | Abrir arquivo | — |

Após um goto, use `Ctrl-o` para voltar.

## Diagnósticos

Diagnósticos aparecem no gutter (coluna esquerda) e na statusline.

| Atalho | Ação |
|--------|------|
| `]d` | Próximo diagnóstico |
| `[d` | Diagnóstico anterior |
| `]D` | Último diagnóstico do documento |
| `[D` | Primeiro diagnóstico do documento |
| `{` / `}` | Diagnóstico anterior / próximo (custom) |
| `Space d` | Picker de diagnósticos do documento |
| `Space D` | Picker de diagnósticos do workspace |

A statusline mostra contagem de erros/warnings/info no workspace.

## Rename symbol

```
Space r     → renomear símbolo sob cursor em todo o projeto
```

Confirme com `Enter`. O LSP propaga a mudança a todos os arquivos afetados.

## Code actions

```
Space a     → lista de ações disponíveis para a seleção/cursor
```

Exemplos de code actions:
- Importar módulo faltante
- Remover import não usado
- Aplicar quick fix de lint
- Extrair função/variável

## Symbol picker

| Atalho | Escopo |
|--------|--------|
| `Space s` | Símbolos do documento atual |
| `Space S` | Símbolos de todo o workspace |

Navegue com fuzzy search. `Enter` para ir ao símbolo.

## Select references

```
Space h     → seleciona todas as referências ao símbolo sob cursor
```

Útil para ver/editar todas as ocorrências simultaneamente.

## Formatação

| Atalho | Escopo |
|--------|--------|
| `=` | Formatar seleção |
| `F` (custom) / `:format` | Formatar arquivo inteiro |

Com `auto-format = true`, formata ao salvar.

## Inlay hints

Com `display-inlay-hints = true` (configurado), o LSP mostra dicas inline:
- Tipos de parâmetros
- Tipos de variáveis inferidos
- Nomes de parâmetros em chamadas de função

## Signature help

Com `auto-signature-help = true`, ao digitar `(` em uma chamada de função, aparece popup com assinatura:
- `Alt-p` — assinatura anterior (overload)
- `Alt-n` — próxima assinatura

## Múltiplos language servers

O Helix pode usar vários LSPs por linguagem. Exemplo Python:

```toml
[[language]]
name = "python"
language-servers = ["pyright", "ruff"]
```

- **pyright** — tipos, autocomplete, goto
- **ruff** — linting rápido, formatação

Features como diagnostics e completion são **mescladas** de todos os LSPs ativos.

## LSP roots (raízes de projeto)

O Helix detecta a raiz do projeto por marcadores:

| Linguagem | Marcador |
|-----------|----------|
| Python | `pyproject.toml`, `setup.py`, `requirements.txt` |
| Go | `go.mod` |
| Rust | `Cargo.toml` |
| JS/TS | `package.json` |
| PHP | `composer.json` |

Se o LSP não iniciar, verifique se o marcador existe no diretório raiz.

## Troubleshooting LSP

| Problema | Solução |
|----------|---------|
| LSP não inicia | `hx --health <lang>` — instale binário faltante |
| Autocomplete vazio | Aguarde indexação; verifique `roots` |
| Diagnósticos errados | Verifique versão do LSP; reinicie com `:lsp-restart` |
| Goto não funciona | Confirme que o LSP suporta a feature |
| Lento em monorepo | Configure `workspace-lsp-roots` em `.helix/config.toml` |

## Próximo passo

[09 — Busca e Substituição](./09-busca-e-substituicao.md)
