# 16 — Referência Rápida (Cheatsheet)

## Modos

| Modo | Entrada | Saída |
|------|---------|-------|
| Normal | `Esc` / padrão | — |
| Insert | `i a o O I A` | `Esc` |
| Select | `v` | `Esc` |
| Command | `:` | `Enter` / `Esc` |
| Goto | `g` | próxima tecla |
| Space | `Space` | próxima tecla |
| Window | `Ctrl-w` | próxima tecla |
| View | `z` / `Z` | próxima tecla / `Esc` |
| Match | `m` | próxima tecla |

## Movimentação

```
h j k l       mover
w b e         palavra
f F t T       find char
gg ge         início/fim arquivo
G N           linha N
Ctrl-o/i      jumplist
zz            centralizar
```

## Edição

```
i a o O       insert/append/open
x             selecionar linha
d c y         delete/change/yank
p P           paste
u U           undo/redo
> <           indent
=             formatar seleção
Ctrl+c        comentar
r R           replace
J             juntar linhas
.             repetir insert
```

## Seleção

```
v             select mode
%             tudo
S             linha inteira
mif mac mi"   textobjects
ms" md"       surround
Alt-o/i       expand/shrink (TS)
s regex       selecionar matches
```

## Goto (`g`)

```
gg ge         início/fim
gh gl         início/fim linha
gn gp         buffer +/- 
gd gy gr gi   LSP goto
ga gm         último acessado/modificado
```

## Space

```
Space f F     file picker
Space b       buffers
Space k       hover
Space a       code action
Space r       rename
Space s S     symbols doc/ws
Space d D     diagnostics doc/ws
Space h       references
Space /       busca global
Space ?       command palette
Space c C     comentar
Space y p     clipboard
Space '       último picker
```

## LSP

```
gd            definition
gy            type definition
gr            references
gi            implementation
Space k       hover
Space a       code action
Space r       rename
]d [d         diag +/-
{ }           diag +/- (custom)
Ctrl-x        autocomplete (insert)
F             formatar arquivo
```

## Busca

```
/ ?           buscar
n N           próximo/anterior
*             palavra sob cursor
Space /       busca global
:%s/o/n/g     substituir
```

## Janelas

```
Ctrl-w v s    split V/H
Ctrl-w h/j/k/l  navegar
Ctrl-w q o    fechar/só esta
Ctrl-h/j/k/l  navegar (custom)
```

## Shell

```
| cmd         pipe seleção
! cmd         inserir output
$ cmd         pipe (exit 0)
:sh           shell
```

## Comandos

```
:w :wq :q    salvar/sair
:config-open  abrir config
:config-reload recarregar
:theme        escolher tema
:format       formatar
:lsp-restart  reiniciar LSP
:help         ajuda
```

## Custom (esta máquina)

```
Ctrl+s        salvar
Ctrl+Shift+s  salvar e sair
Ctrl+q        sair
Ctrl+h/j/k/l  navegar splits
{ }           diagnósticos
F             formatar arquivo
S             selecionar linha
```

## LSPs instalados

```
python     pyright + ruff
php        intelephense
go         gopls
rust       rust-analyzer
js/ts/jsx  typescript-language-server
html/css   vscode-*-language-server
json       vscode-json-language-server
sql        sqls
yaml       yaml-language-server
toml       taplo
markdown   marksman
```

## Verificar saúde

```bash
hx --health <linguagem>
hx --version
:config-reload
```

## tmux (sessões persistentes)

```
Ctrl+Alt+T          abrir terminal (Pop!_OS)
tmux new -s dev     nova sessão
tmux a -t dev       reconectar
Ctrl+b d            detach
Ctrl+b % "          split V/H
Ctrl+b c n p        janela nova/próx/anterior
```

Ver [manual 17](./17-terminal-e-sessoes-persistentes.md) para restaurar sessões após reboot.

---

**Imprima esta página e mantenha ao lado do monitor durante as primeiras semanas.**

[← Voltar ao índice](./README.md) · [17 — Terminal e Sessões Persistentes](./17-terminal-e-sessoes-persistentes.md)
