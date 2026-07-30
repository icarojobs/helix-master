# 06 — Atalhos Essenciais

Referência consolidada dos atalhos mais usados no dia a dia. Atalhos marcados com **(custom)** foram adicionados na configuração desta máquina.

## Arquivo e sessão

| Atalho | Ação |
|--------|------|
| `Ctrl+s` **(custom)** | Salvar |
| `Ctrl+Shift+s` **(custom)** | Salvar e sair |
| `Ctrl+q` **(custom)** | Sair |
| `:w` | Salvar |
| `:wq` | Salvar e sair |
| `:q` | Sair |
| `:q!` | Sair sem salvar |
| `:config-open` | Abrir config.toml |
| `:config-reload` | Recarregar configuração |
| `:theme` | Escolher tema |

## Movimentação

| Atalho | Ação |
|--------|------|
| `h j k l` | Esquerda / baixo / cima / direita |
| `w b e` | Palavra próxima / anterior / fim |
| `f F t T` + char | Find / till char |
| `gg` | Início do arquivo |
| `G` + N | Linha N |
| `ge` | Fim do arquivo |
| `Ctrl-o` | Voltar jumplist |
| `Ctrl-i` | Avançar jumplist |
| `zz` | Centralizar linha |

## Edição

| Atalho | Ação |
|--------|------|
| `i a o O` | Insert / append / open line |
| `x` | Selecionar linha |
| `d` | Deletar seleção |
| `c` | Change (deletar + insert) |
| `y` | Yank (copiar) |
| `p P` | Colar depois / antes |
| `u U` | Undo / redo |
| `Ctrl+c` | Comentar/descomentar |
| `>` `<` | Indentar / desindentar |
| `=` | Formatar seleção |
| `F` **(custom)** | Formatar arquivo |

## Seleção e textobjects

| Atalho | Ação |
|--------|------|
| `v` | Select mode (estender) |
| `%` | Selecionar tudo |
| `S` **(custom)** | Selecionar linha inteira |
| `mif` | Inside function |
| `mac` | Around class |
| `mi"` | Inside quotes |
| `Alt-o` | Expandir para nó pai (TS) |
| `Alt-i` | Contrair seleção (TS) |

## LSP

| Atalho | Ação |
|--------|------|
| `gd` | Goto definition |
| `gy` | Goto type definition |
| `gr` | Goto references |
| `gi` | Goto implementation |
| `Space k` | Hover (documentação) |
| `Space a` | Code action |
| `Space r` | Rename symbol |
| `Space s` | Symbol picker (documento) |
| `Space S` | Symbol picker (workspace) |
| `Space d` | Diagnostics picker |
| `Space h` | Select references |
| `]d` `[d` | Próximo / anterior diagnóstico |
| `{` `}` **(custom)** | Diagnóstico anterior / próximo |
| `Ctrl-x` (insert) | Autocomplete |

## Busca

| Atalho | Ação |
|--------|------|
| `/` | Buscar regex |
| `?` | Buscar anterior |
| `n N` | Próximo / anterior match |
| `*` | Buscar palavra sob cursor |
| `Space /` | Busca global no workspace |

## Buffers e janelas

| Atalho | Ação |
|--------|------|
| `Space f` | File picker (LSP root) |
| `Space F` | File picker (cwd) |
| `Space b` | Buffer picker |
| `gn gp` | Próximo / anterior buffer |
| `Ctrl-w v` | Split vertical |
| `Ctrl-w s` | Split horizontal |
| `Ctrl-w q` | Fechar janela |
| `Ctrl-w o` | Apenas esta janela |
| `Ctrl+h/j/k/l` **(custom)** | Navegar splits |

## Shell

| Atalho | Ação |
|--------|------|
| `\|` | Pipe seleção por comando shell |
| `!` | Executar shell, inserir output |
| `$` | Pipe seleção, manter se exit 0 |

## Insert mode

| Atalho | Ação |
|--------|------|
| `Esc` | Voltar ao normal mode |
| `Ctrl+s` | Checkpoint de undo |
| `Ctrl-x` | Autocomplete |
| `Ctrl-w` | Deletar palavra anterior |
| `Ctrl-u` | Deletar até início da linha |
| `Ctrl-k` | Deletar até fim da linha |
| `Ctrl+j` / `Enter` | Nova linha |

## Próximo passo

[07 — Modo Goto e Space](./07-modo-goto-e-espaco.md)
