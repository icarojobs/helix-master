# 07 — Modo Goto e Space

## Modo Goto (`g`)

Pressione `g` no normal mode para acessar atalhos de navegação rápida. Cada tecla subsequente executa um comando e retorna ao normal mode.

### Navegação no arquivo

```
gg    → início do arquivo
ge    → fim do arquivo (última linha)
gh    → início da linha
gl    → fim da linha
gs    → primeiro caractere não-branco
g|    → coluna N (ou início da linha)
```

### Navegação na viewport

```
gt    → topo da tela
gc    → centro da tela
gb    → base da tela
```

### Navegação entre buffers

```
gn    → próximo buffer
gp    → buffer anterior
ga    → último arquivo acessado
gm    → último arquivo modificado
g.    → última modificação no arquivo atual
```

### Goto LSP

```
gd    → goto definition
gy    → goto type definition
gr    → goto references
gi    → goto implementation
```

### Goto arquivo e palavra

```
gf    → abrir arquivo sob cursor/seleção
gw    → goto word (labels em cada palavra visível)
```

### Movimento textual

```
gj    → linha textual abaixo (ignora soft-wrap visual)
gk    → linha textual acima
```

## Modo Space (`Space`)

O Space mode é o "centro de comando" do Helix — pickers, LSP e utilitários.

### Arquivos e buffers

| Tecla | Ação |
|-------|------|
| `Space f` | File picker (raiz LSP do workspace) |
| `Space F` | File picker (diretório atual) |
| `Space b` | Buffer picker |
| `Space j` | Jumplist picker |
| `Space g` | Changed files picker |
| `Space '` | Reabrir último picker |

### LSP e inteligência

| Tecla | Ação |
|-------|------|
| `Space k` | Hover — documentação sob cursor |
| `Space a` | Code action |
| `Space r` | Rename symbol |
| `Space s` | Document symbol picker |
| `Space S` | Workspace symbol picker |
| `Space d` | Document diagnostics picker |
| `Space D` | Workspace diagnostics picker |
| `Space h` | Select references to symbol |

### Edição e clipboard

| Tecla | Ação |
|-------|------|
| `Space c` | Toggle comentário |
| `Space C` | Toggle comentário de bloco |
| `Space Alt-c` | Toggle comentário de linha |
| `Space y` | Yank para clipboard do sistema |
| `Space Y` | Yank primário para clipboard |
| `Space p` | Colar do clipboard (depois) |
| `Space P` | Colar do clipboard (antes) |
| `Space R` | Substituir seleções pelo clipboard |

### Busca e comandos

| Tecla | Ação |
|-------|------|
| `Space /` | Busca global no workspace |
| `Space ?` | Command palette |

### Janelas

| Tecla | Ação |
|-------|------|
| `Space w` | Entrar em window mode (`Ctrl-w`) |

## Modo Match (`m`)

| Tecla | Ação |
|-------|------|
| `mm` | Ir para bracket correspondente |
| `ms<char>` | Surround com caractere |
| `mr<old><new>` | Substituir surround |
| `md<char>` | Remover surround |
| `mi<obj>` | Inside textobject |
| `ma<obj>` | Around textobject |

## Modo Window (`Ctrl-w`)

| Tecla | Ação |
|-------|------|
| `Ctrl-w v` | Split vertical (direita) |
| `Ctrl-w s` | Split horizontal (abaixo) |
| `Ctrl-w h/j/k/l` | Mover para split |
| `Ctrl-w q` | Fechar janela atual |
| `Ctrl-w o` | Manter apenas janela atual |
| `Ctrl-w f` | Abrir arquivo em split horizontal |
| `Ctrl-w F` | Abrir arquivo em split vertical |
| `Ctrl-w H/J/K/L` | Trocar posição de janelas |

## Workflow recomendado com Space

```
Space f     → abrir arquivo do projeto
Space b     → alternar entre buffers abertos
Space k     → ver documentação de função
Space a     → aplicar quick fix do LSP
Space r     → renomear variável em todo projeto
Space /     → buscar texto em todo workspace
Space ?     → qualquer comando via palette
```

## Próximo passo

[08 — LSP e Inteligência](./08-lsp-e-inteligencia.md)
