# 10 — Buffers, Janelas e Splits

## Conceitos

| Termo | Significado |
|-------|-------------|
| **Buffer** | Conteúdo de um arquivo na memória |
| **View** | Como um buffer é exibido na tela |
| **Window** | Área da tela contendo uma view |
| **Workspace** | Conjunto de janelas visíveis |

Um buffer pode ter múltiplas views (splits). Fechar uma view não fecha o buffer.

## Abrir arquivos

```bash
hx arquivo.py              # abrir arquivo
hx .                       # abrir diretório (file picker)
hx arquivo1.py arquivo2.go # múltiplos arquivos
```

Dentro do Helix:

| Atalho | Ação |
|--------|------|
| `Space f` | File picker (raiz LSP) |
| `Space F` | File picker (cwd) |
| `gf` | Abrir arquivo sob cursor |
| `:o arquivo.py` | Abrir arquivo |

## Buffer picker

```
Space b     → lista todos os buffers abertos
```

- Fuzzy search por nome.
- `Enter` — alternar para o buffer.
- `Ctrl-s` — abrir em split horizontal.
- `Ctrl-v` — abrir em split vertical.

## Navegar entre buffers

| Atalho | Ação |
|--------|------|
| `gn` | Próximo buffer |
| `gp` | Buffer anterior |
| `ga` | Último arquivo acessado |
| `gm` | Último arquivo modificado |

## Splits (janelas)

### Criar splits

| Atalho | Ação |
|--------|------|
| `Ctrl-w s` | Split horizontal (abaixo) |
| `Ctrl-w v` | Split vertical (direita) |
| `Ctrl-w f` | Abrir arquivo em split horizontal |
| `Ctrl-w F` | Abrir arquivo em split vertical |

### Navegar entre splits

| Atalho | Ação |
|--------|------|
| `Ctrl-w h` | Split à esquerda |
| `Ctrl-w j` | Split abaixo |
| `Ctrl-w k` | Split acima |
| `Ctrl-w l` | Split à direita |
| `Ctrl-h/j/k/l` **(custom)** | Mesmo que acima |

### Gerenciar splits

| Atalho | Ação |
|--------|------|
| `Ctrl-w q` | Fechar janela atual |
| `Ctrl-w o` | Manter apenas janela atual |
| `Ctrl-w w` | Rotacionar para próxima janela |
| `Ctrl-w H/J/K/L` | Trocar posição de janelas |

## Layouts comuns

### Editar código + documentação

```
1. Abrir arquivo principal
2. Ctrl-w v          → split vertical
3. Space f           → abrir doc no split direito
4. Ctrl-w l          → focar split direito
```

### Comparar dois arquivos

```
1. hx arquivo1.py arquivo2.py
2. Ctrl-w v          → lado a lado
3. :diff-toggle      → ativar diff
```

### Terminal + editor

O Helix não tem terminal embutido. Use um terminal externo (tmux, wezterm) com splits:

```bash
# tmux exemplo
tmux split-window -h 'hx arquivo.py'
```

## Fechar e salvar

| Comando | Ação |
|---------|------|
| `:w` | Salvar buffer atual |
| `:wa` | Salvar todos os buffers |
| `:q` | Fechar view (fecha buffer se última view) |
| `:qa` | Fechar tudo |
| `:q!` | Fechar sem salvar |
| `:wq` | Salvar e fechar |
| `Ctrl+s` **(custom)** | Salvar |
| `Ctrl+Shift+s` **(custom)** | Salvar e sair |

Com `auto-save = true`, o buffer salva automaticamente ao perder foco ou fechar.

## Jumplist entre buffers

`Ctrl-o` e `Ctrl-i` funcionam entre buffers — ao fazer `gd` (goto definition) em outro arquivo, `Ctrl-o` volta ao arquivo e posição anteriores.

```
Space j     → jumplist picker (histórico visual de saltos)
```

## Changed files picker

```
Space g     → arquivos modificados (git)
```

Útil para revisar mudanças antes de commit.

## Dicas

1. **Use `Space b`** em vez de abrir muitos arquivos — alterne entre buffers.
2. **Splits verticais** (`Ctrl-w v`) são mais úteis em monitores widescreen.
3. **`Ctrl-w o`** limpa splits desnecessários rapidamente.
4. **`ga`** volta ao arquivo anterior — equivalente a Alt+Tab entre buffers.

## Próximo passo

[11 — Comandos e Pickers](./11-comandos-e-pickers.md)
