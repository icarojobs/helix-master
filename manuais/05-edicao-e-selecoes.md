# 05 — Edição e Seleções

## Modelo de seleção

No Helix, **toda operação de edição requer uma seleção**. Mesmo um cursor de um caractere é uma seleção mínima.

### Selecionar linha

| Tecla | Ação |
|-------|------|
| `x` | Selecionar linha atual; se já selecionada, estende para baixo |
| `X` | Seleção linha-inteira (line-wise) |
| `S` | Selecionar linha inteira (atalho customizado) |
| `%` | Selecionar arquivo inteiro |

### Estender seleção

| Tecla | Ação |
|-------|------|
| `v` | Entrar em select mode (movimentos estendem) |
| `Shift+J` | Estender seleção uma linha abaixo |
| `Shift+K` | Estender seleção uma linha acima |

## Operações sobre seleção

| Tecla | Ação |
|-------|------|
| `d` | Deletar seleção (yank implícito) |
| `Alt-d` | Deletar sem yank |
| `c` | Change — deletar e entrar em insert mode |
| `Alt-c` | Change sem yank |
| `y` | Yank (copiar) seleção |
| `p` | Colar depois da seleção |
| `P` | Colar antes da seleção |
| `r` + char | Substituir por caractere |
| `R` | Substituir por conteúdo do yank |
| `~` | Alternar maiúscula/minúscula |
| `` ` `` | Converter para minúsculas |
| `Alt+`` ` `` | Converter para maiúsculas |
| `>` | Indentar seleção |
| `<` | Remover indentação |
| `=` | Formatar seleção (LSP) |
| `J` | Juntar linhas selecionadas |
| `Alt-J` | Juntar linhas (com espaço selecionado) |

## Inserção de texto

| Tecla | Ação |
|-------|------|
| `i` | Insert antes da seleção |
| `a` | Append depois da seleção |
| `I` | Insert no início da linha |
| `A` | Append no final da linha |
| `o` | Abrir linha abaixo |
| `O` | Abrir linha acima |
| `.` | Repetir último insert |

## Comentários

| Tecla | Ação |
|-------|------|
| `Ctrl+c` | Toggle comentário (linha ou seleção) |
| `Space c` | Toggle comentário |
| `Space C` | Toggle comentário de bloco |
| `Space Alt-c` | Toggle comentário de linha |

## Surround (modo `m`)

| Comando | Ação |
|---------|------|
| `ms<char>` | Surround seleção com `<char>` |
| `mr<old><new>` | Substituir surround |
| `md<char>` | Remover surround `<char>` |

Exemplos:

```
ms"     → envolve seleção com aspas duplas
ms(     → envolve com parênteses (adiciona fechamento)
md"     → remove aspas ao redor
mr"'    → troca aspas simples por duplas
```

## Textobjects (modo `m`)

| Comando | Ação |
|---------|------|
| `mi<obj>` | Inside textobject |
| `ma<obj>` | Around textobject |

Textobjects comuns (requerem tree-sitter):

| Objeto | Descrição |
|--------|-----------|
| `f` / `function` | Função |
| `c` / `class` | Classe |
| `a` / `argument` | Argumento |
| `t` / `type` | Tipo |
| `d` / `comment` | Comentário |
| `T` / `test` | Teste |
| `p` / `paragraph` | Parágrafo |
| `i` / `indentation` | Indentação |
| `g` / `change` | Mudança (diff) |
| `(` `)` `[` `]` `{` `}` | Parênteses, colchetes, chaves |
| `"` `'` `` ` `` | Aspas |

Exemplos:

```
mif     → seleciona inside de função
mac     → seleciona around de classe
mi"     → seleciona dentro de aspas duplas
ma(     → seleciona parênteses incluindo os chars
```

## Seleção por regex

| Tecla | Ação |
|-------|------|
| `s` + regex | Selecionar matches de regex dentro das seleções |
| `S` + regex | Dividir seleções nos matches |
| `Alt-s` | Dividir seleções em novas linhas |
| `K` + regex | Manter seleções que casam |
| `Alt-K` + regex | Remover seleções que casam |

## Alinhamento e manipulação

| Tecla | Ação |
|-------|------|
| `&` | Alinhar seleções em colunas |
| `_` | Trim whitespace da seleção |
| `;` | Colapsar seleção em cursor único |
| `Alt-;` | Inverter cursor e âncora |
| `Alt-:` | Garantir seleção em direção forward |
| `,` | Manter apenas seleção primária |
| `Alt-,` | Remover seleção primária |
| `(` / `)` | Rotacionar seleção primária |

## Incremento/decremento

| Tecla | Ação |
|-------|------|
| `Ctrl-a` | Incrementar número sob cursor |
| `Ctrl-x` | Decrementar número sob cursor |

## Clipboard do sistema

| Tecla | Ação |
|-------|------|
| `Space y` | Yank para clipboard do sistema |
| `Space Y` | Yank seleção primária para clipboard |
| `Space p` | Colar do clipboard depois |
| `Space P` | Colar do clipboard antes |
| `Space R` | Substituir seleções pelo clipboard |

## Próximo passo

[06 — Atalhos Essenciais](./06-atalhos-essenciais.md)
