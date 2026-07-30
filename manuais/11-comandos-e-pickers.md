# 11 — Comandos e Pickers

## Command mode (`:`)

Pressione `:` no normal mode para entrar no command mode. Digite o comando e pressione `Enter`.

### Comandos essenciais

| Comando | Ação |
|---------|------|
| `:w` | Salvar |
| `:wa` | Salvar todos |
| `:wq` | Salvar e sair |
| `:q` | Sair |
| `:q!` | Sair sem salvar |
| `:qa` | Sair de todos os buffers |
| `:o <arquivo>` | Abrir arquivo |
| `:new` | Novo buffer |
| `:reload` | Recarregar arquivo do disco |
| `:earlier` | Voltar no histórico de undo |
| `:later` | Avançar no histórico de undo |

### Configuração

| Comando | Ação |
|---------|------|
| `:config-open` | Abrir config.toml no editor |
| `:config-reload` | Recarregar configuração |
| `:theme` | Escolher tema interativamente |
| `:set` | Ver/alterar opções |

### LSP e formatação

| Comando | Ação |
|---------|------|
| `:format` | Formatar arquivo inteiro |
| `:lsp-restart` | Reiniciar language servers |
| `:lsp-stop` | Parar language servers |

### Busca e substituição

| Comando | Ação |
|---------|------|
| `:/padrão` | Buscar |
| `:?padrão` | Buscar para trás |
| `:%s/old/new/g` | Substituir globalmente |

### Utilitários

| Comando | Ação |
|---------|------|
| `:help` | Ajuda interativa |
| `:sh` | Shell interativo |
| `:pipe <cmd>` | Pipe buffer por comando shell |
| `:vsplit` | Split vertical |
| `:hsplit` | Split horizontal |
| `:wclose` | Fechar janela |
| `:quit-all` | Fechar tudo |
| `:write-quit-all` | Salvar e fechar tudo |
| `:quit!` | Forçar saída |
| `:cquit` | Sair com código de erro |

## Command palette

```
Space ?     → palette de comandos com fuzzy search
```

A palette lista **todos** os comandos disponíveis. Digite para filtrar e `Enter` para executar.

Útil quando você não lembra o atalho exato.

## Pickers

Pickers são interfaces fuzzy-search para listas.

### File picker

```
Space f     → arquivos na raiz LSP do workspace
Space F     → arquivos no diretório atual
```

| Tecla no picker | Ação |
|-----------------|------|
| `Enter` | Abrir |
| `Ctrl-s` | Abrir em split horizontal |
| `Ctrl-v` | Abrir em split vertical |
| `Alt-Enter` | Abrir em background |
| `Ctrl-t` | Toggle preview |
| `Escape` | Fechar |

### Buffer picker

```
Space b     → buffers abertos
```

### Jumplist picker

```
Space j     → histórico de saltos
```

### Symbol pickers

```
Space s     → símbolos do documento
Space S     → símbolos do workspace
```

### Diagnostics pickers

```
Space d     → diagnósticos do documento
Space D     → diagnósticos do workspace
```

### Changed files picker

```
Space g     → arquivos modificados (git)
```

### Reabrir último picker

```
Space '     → reabrir o último picker usado
```

Muito útil após busca global (`Space /`) — abre arquivo e `Space '` traz resultados de volta.

## Prompt (dentro de pickers e comandos)

| Tecla | Ação |
|-------|------|
| `Ctrl-p` / `↑` | Histórico anterior |
| `Ctrl-n` / `↓` | Próximo no histórico |
| `Ctrl-a` / `Home` | Início da linha |
| `Ctrl-e` / `End` | Fim da linha |
| `Ctrl-w` | Deletar palavra anterior |
| `Ctrl-u` | Deletar até início |
| `Ctrl-k` | Deletar até fim |
| `Tab` | Próximo completion |
| `Enter` | Confirmar |
| `Escape` | Cancelar |

## Autocomplete no command mode

O command mode tem autocomplete — pressione `Tab` para completar comandos e argumentos.

## Dicas

1. **`Space ?`** é seu melhor amigo quando esquece um atalho.
2. **`Space '`** economiza tempo ao navegar resultados de busca.
3. **Preview** (`Ctrl-t` no picker) permite ver conteúdo antes de abrir.
4. **Histórico** no prompt — `Ctrl-p` repete comandos anteriores.

## Próximo passo

[12 — Configuração Avançada](./12-configuracao-avancada.md)
