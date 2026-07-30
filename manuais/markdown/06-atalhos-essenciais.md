# 06 — Atalhos Essenciais

Referência consolidada dos atalhos do Helix — nativos e personalizados. Para **instalar e configurar** todos os atalhos, veja [02 — Instalação e Configuração](./02-instalacao-e-configuracao.md#parte-5--setup-completo-de-atalhos).

## Como configurar atalhos personalizados

1. Copie o arquivo de exemplo:

```bash
mkdir -p ~/.config/helix
cp exemplos/config.toml ~/.config/helix/config.toml
```

2. Edite `~/.config/helix/config.toml` na seção `[keys.normal]`, `[keys.insert]` ou `[keys.select]`.

3. Recarregue: `:config-reload` dentro do Helix.

### Estrutura de keymaps

```toml
[keys.normal]     # Modo normal (navegação e comandos)
C-s = ":w"        # Ctrl+s → salvar

[keys.insert]     # Modo insert (digitação)
C-s = [":w", "normal_mode"]

[keys.select]     # Modo select (estender seleção)
C-s = ":w"
```

### Convenções de nomes de teclas

| Tecla | Nome no config |
|-------|----------------|
| `Ctrl+s` | `C-s` |
| `Ctrl+Shift+s` | `C-S` |
| `Alt+x` | `A-x` |
| `Shift+x` | `S-x` |
| `{` | `"{"` (entre aspas) |
| `Space` | `space` |

### Múltiplos comandos em sequência

```toml
C-s = [":w", "normal_mode"]   # salva e volta ao normal mode
```

### Desabilitar atalho

```toml
[keys.insert]
up = "no_op"
down = "no_op"
```

---

## Atalhos personalizados (config recomendada)

Estes atalhos estão em `exemplos/config.toml` e devem ser copiados para `~/.config/helix/config.toml`:

| Atalho | Modo | Ação |
|--------|------|------|
| `Ctrl+s` | normal | Salvar |
| `Ctrl+Shift+s` | normal | Salvar e sair |
| `Ctrl+q` | normal | Sair |
| `Ctrl+s` | insert | Salvar e voltar ao normal |
| `Ctrl+h/j/k/l` | normal | Navegar entre splits |
| `{` / `}` | normal | Diagnóstico anterior / próximo |
| `F` | normal | Formatar arquivo |
| `S` | normal | Selecionar linha inteira |

---

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
| `:wa` | Salvar todos os buffers |
| `:config-open` | Abrir config.toml |
| `:config-reload` | Recarregar configuração |
| `:theme` | Escolher tema |
| `:help` | Ajuda interativa |

## Movimentação

| Atalho | Ação |
|--------|------|
| `h j k l` | Esquerda / baixo / cima / direita |
| `w b e` | Palavra próxima / anterior / fim |
| `W B E` | WORD próxima / anterior / fim |
| `f F t T` + char | Find / till char |
| `gg` | Início do arquivo |
| `G` + N | Ir para linha N |
| `ge` | Fim do arquivo |
| `Ctrl-o` | Voltar jumplist |
| `Ctrl-i` | Avançar jumplist |
| `Ctrl-s` | Salvar seleção no jumplist |
| `zz` / `zt` / `zb` | Centralizar / topo / base da tela |

## Edição

| Atalho | Ação |
|--------|------|
| `i a o O I A` | Insert / append / open line |
| `x` | Selecionar linha |
| `d` | Deletar seleção |
| `Alt-d` | Deletar sem yank |
| `c` | Change (deletar + insert) |
| `y` | Yank (copiar) |
| `p P` | Colar depois / antes |
| `u U` | Undo / redo |
| `Alt-u Alt-U` | Earlier / later no histórico |
| `Ctrl+c` | Comentar/descomentar |
| `>` `<` | Indentar / desindentar |
| `=` | Formatar seleção (LSP) |
| `F` **(custom)** | Formatar arquivo |
| `r` + char | Substituir por caractere |
| `~` | Alternar maiúscula/minúscula |
| `J` | Juntar linhas |

## Seleção e textobjects

| Atalho | Ação |
|--------|------|
| `v` | Select mode (estender) |
| `%` | Selecionar tudo |
| `S` **(custom)** | Selecionar linha inteira |
| `X` | Seleção linha-inteira |
| `mif` | Inside function |
| `mac` | Around class |
| `mi"` | Inside quotes |
| `ma(` | Around parênteses |
| `ms"` / `md"` | Surround / delete surround |
| `Alt-o` | Expandir para nó pai (TS) |
| `Alt-i` | Contrair seleção (TS) |
| `Alt-p/n` | Irmão anterior/próximo (TS) |
| `s` + regex | Selecionar por regex |

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
| `Space d` | Diagnostics picker (documento) |
| `Space D` | Diagnostics picker (workspace) |
| `Space h` | Select references |
| `]d` `[d` | Próximo / anterior diagnóstico |
| `]D` `[D` | Último / primeiro diagnóstico |
| `{` `}` **(custom)** | Diagnóstico anterior / próximo |
| `Ctrl-x` (insert) | Autocomplete |

## Busca

| Atalho | Ação |
|--------|------|
| `/` | Buscar regex |
| `?` | Buscar anterior |
| `n N` | Próximo / anterior match |
| `*` | Buscar palavra sob cursor |
| `Alt-*` | Buscar seleção exata |
| `Space /` | Busca global no workspace |

## Buffers e janelas

| Atalho | Ação |
|--------|------|
| `Space f` | File picker (LSP root) |
| `Space F` | File picker (cwd) |
| `Space b` | Buffer picker |
| `Space j` | Jumplist picker |
| `Space g` | Changed files (git) |
| `gn gp` | Próximo / anterior buffer |
| `Ctrl-w v` | Split vertical |
| `Ctrl-w s` | Split horizontal |
| `Ctrl-w q` | Fechar janela |
| `Ctrl-w o` | Apenas esta janela |
| `Ctrl-w h/j/k/l` | Navegar splits (window mode) |
| `Ctrl+h/j/k/l` **(custom)** | Navegar splits (direto) |

## Shell

| Atalho | Ação |
|--------|------|
| `\|` + cmd | Pipe seleção por comando shell |
| `Alt-\|` + cmd | Pipe ignorando output |
| `!` + cmd | Executar shell, inserir output antes |
| `Alt-!` + cmd | Executar shell, inserir output depois |
| `$` + cmd | Pipe, manter se exit 0 |

## Insert mode

| Atalho | Ação |
|--------|------|
| `Esc` | Voltar ao normal mode |
| `Ctrl+s` | Checkpoint de undo / salvar (custom) |
| `Ctrl-x` | Autocomplete |
| `Ctrl-r` | Inserir conteúdo de registro |
| `Ctrl-w` | Deletar palavra anterior |
| `Ctrl-u` | Deletar até início da linha |
| `Ctrl-k` | Deletar até fim da linha |
| `Ctrl-j` / `Enter` | Nova linha |

## Unimpaired (navegação estrutural)

| Atalho | Ação |
|--------|------|
| `]f` `[f` | Próxima / anterior função |
| `]t` `[t` | Próximo / anterior tipo |
| `]a` `[a` | Próximo / anterior parâmetro |
| `]c` `[c` | Próximo / anterior comentário |
| `]T` `[T` | Próximo / anterior teste |
| `]g` `[g` | Próxima / anterior mudança |

## Próximo passo

[07 — Modo Goto e Space](./07-modo-goto-e-espaco.md)
