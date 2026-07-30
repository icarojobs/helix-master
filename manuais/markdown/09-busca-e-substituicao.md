# 09 — Busca e Substituição

## Busca local (no buffer)

### Iniciar busca

| Tecla | Ação |
|-------|------|
| `/` | Buscar regex para frente |
| `?` | Buscar regex para trás |
| `*` | Buscar palavra sob cursor (com word boundaries) |
| `Alt-*` | Buscar seleção exata (sem word boundaries) |

A busca usa o registro `/` por padrão. Para outro registro: `"/a` + regex.

### Navegar resultados

| Tecla | Ação |
|-------|------|
| `n` | Próximo match |
| `N` | Match anterior |

No select mode, `n`/`N` podem adicionar matches às seleções em vez de substituir.

### Seleção por regex

| Tecla | Ação |
|-------|------|
| `s` + regex | Selecionar todos os matches dentro das seleções atuais |
| `S` + regex | Dividir seleções nos matches |
| `K` + regex | Manter apenas seleções que casam |
| `Alt-K` + regex | Remover seleções que casam |

## Busca global (workspace)

```
Space /     → busca fuzzy em todo o workspace
```

- Resultados aparecem em um picker.
- `Enter` — abrir arquivo no match.
- `Ctrl-s` — abrir em split horizontal.
- `Ctrl-v` — abrir em split vertical.
- `Space '` — reabrir o último picker de busca.

A busca global respeita `editor.file-search.ignore` (`.git`, `node_modules`, etc.).

## Substituição via command mode

### Substituir no buffer atual

```
:%s/padrão/substituição/g
```

Exemplos:

```
:%s/foo/bar/g           → substituir todas as ocorrências
:%s/foo/bar/gc          → substituir com confirmação
:5,10s/foo/bar/g        → substituir nas linhas 5-10
```

### Substituir em seleção

Com uma seleção ativa, o comando de substituição opera apenas sobre ela.

## Substituição com seleções múltiplas

Workflow poderoso do Helix:

```
1. /padrão          → buscar
2. n n n            → navegar e adicionar matches (em select mode)
3. c                → change todas as seleções simultaneamente
4. Esc              → confirmar
```

Ou:

```
1. s/padrão         → selecionar todos os matches
2. c novo_texto     → substituir todos de uma vez
```

## Regex no Helix

O Helix usa regex Rust (similar a PCRE):

| Padrão | Significado |
|--------|-------------|
| `\d` | Dígito |
| `\w` | Word character |
| `\s` | Whitespace |
| `.` | Qualquer caractere |
| `*` | Zero ou mais |
| `+` | Um ou mais |
| `?` | Zero ou um |
| `{n,m}` | Quantificador |
| `(group)` | Grupo de captura |
| `(?:group)` | Grupo não-capturante |
| `\1` | Backreference |

## Busca e replace com shell

Para transformações complexas, use shell pipe:

```
|sed 's/foo/bar/g'    → pipe seleção por sed
!grep pattern         → executar grep e inserir output
```

## Dicas

1. **Use `*` para busca rápida** de variável/função sob cursor.
2. **Busca global com `Space /`** é mais rápida que `grep` no terminal para navegação.
3. **Select mode + `n`** permite seleção iterativa de matches.
4. **Registros** — salve padrões frequentes: `"/ay` + yank do padrão.

## Próximo passo

[10 — Buffers, Janelas e Splits](./10-buffers-janelas-splits.md)
