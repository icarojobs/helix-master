# 14 — Macros e Automação

## Macros (experimental)

O Helix suporta gravação e reprodução de macros.

| Tecla | Ação |
|-------|------|
| `Q` | Iniciar/parar gravação de macro no registro selecionado |
| `q` | Reproduzir macro do registro selecionado |

### Workflow

```
1. "aQ          → iniciar gravação no registro 'a'
2. (executar sequência de comandos)
3. Q            → parar gravação
4. "aq          → reproduzir macro do registro 'a'
```

### Exemplo: envolver linhas com console.log

```
"aQ            → gravar no registro 'a'
x             → selecionar linha
ms(           → surround com parênteses
i             → insert
console.log   → digitar
Esc           → normal mode
Q             → parar gravação

"j"aq         → repetir macro 10 vezes (se suportado via comando)
```

> Macros são experimentais — comportamento pode mudar entre versões.

## Shell pipe

Uma das features mais poderosas do Helix: pipe seleções por comandos shell.

| Tecla | Ação |
|-------|------|
| `\|` + cmd | Pipe seleção por comando, substituir com output |
| `Alt-\|` + cmd | Pipe seleção por comando, ignorar output |
| `!` + cmd | Executar comando, inserir output antes da seleção |
| `Alt-!` + cmd | Executar comando, inserir output depois da seleção |
| `$` + cmd | Pipe seleção, manter apenas se exit code = 0 |

### Exemplos

```
|sort              → ordenar linhas selecionadas
|uniq              → remover duplicatas
|wc -l             → contar linhas
|jq .              → formatar JSON
|sed 's/foo/bar/'  → substituir via sed
|tr '[:lower:]' '[:upper:]'  → converter para maiúsculas
```

### Workflow: formatar JSON

```
1. %              → selecionar arquivo
2. |jq .          → formatar com jq
```

## Comandos shell via command mode

```
:sh               → shell interativo
:pipe jq .        → pipe buffer inteiro
:!git status      → executar comando e ver output
```

## Automação com múltiplas seleções

Combine seleção por regex com shell pipe:

```
1. s/\d+          → selecionar todos os números
2. |bc            → calcular expressões
3. c              → substituir resultados
```

Ou com change:

```
1. /TODO:         → buscar todos os TODOs
2. (select mode) n n n  → adicionar matches
3. cDONE:         → substituir todos simultaneamente
```

## Integração com Git

Via command mode:

```
:!git diff
:!git status
:!git log --oneline -10
```

Via shell pipe em seleção:

```
|git hash-object --stdin    → gerar hash git do conteúdo
```

## Snippets via LSP

Com `snippet = true` no LSP config, o autocomplete pode inserir snippets:

```
Ctrl-x          → autocomplete
(selecionar snippet com Tab)
(Tab entre placeholders)
```

Snippets vêm do language server (ex: rust-analyzer, intelephense).

## Automação externa

### Abrir Helix com arquivo e posição

```bash
hx +42 arquivo.py          # abrir na linha 42
hx -- vsplit arquivo.py    # abrir em split
```

### Recarregar config de todos os processos

```bash
pkill -USR1 hx
```

### Script para abrir projeto

```bash
#!/bin/bash
cd ~/projects/meu-projeto && hx .
```

## Dicas

1. **Shell pipe é subestimado** — `|sort`, `|uniq`, `|jq` resolvem 80% das transformações.
2. **Múltiplas seleções + change** substitui macros para muitos casos.
3. **Use `!` para inserir output** de comandos como `git log`, `curl`, etc.
4. **Macros são para sequências repetitivas** que não envolvem regex.

## Próximo passo

[15 — Dicas e Workflow](./15-dicas-workflow.md)
