# 04 — Movimentação e Navegação

## Movimentos básicos

| Tecla | Ação |
|-------|------|
| `h` / `←` | Caractere à esquerda |
| `j` / `↓` | Linha visual abaixo |
| `k` / `↑` | Linha visual acima |
| `l` / `→` | Caractere à direita |

> No Helix, `j`/`k` movem por **linhas visuais** (respeitam soft-wrap), não por linhas lógicas do arquivo.

## Movimentos por palavra

| Tecla | Ação |
|-------|------|
| `w` | Início da próxima palavra |
| `b` | Início da palavra anterior |
| `e` | Fim da próxima palavra |
| `W` | Início da próxima WORD (espaços) |
| `B` | Início da WORD anterior |
| `E` | Fim da próxima WORD |

## Movimentos por caractere (find)

| Tecla | Ação |
|-------|------|
| `f` + char | Encontrar próximo caractere |
| `F` + char | Encontrar caractere anterior |
| `t` + char | Até (antes de) próximo caractere |
| `T` + char | Até (depois de) caractere anterior |
| `Alt-.` | Repetir último movimento (f, t, m, [, ]) |

> Diferente do Vim: `f`/`t` **não** ficam restritos à linha atual.

## Movimentos por linha

| Tecla | Ação |
|-------|------|
| `0` / `Home` | Início da linha |
| `$` / `End` | Fim da linha |
| `^` / `gs` | Primeiro caractere não-branco |
| `G` + número | Ir para linha N |
| `gg` | Início do arquivo |
| `ge` | Fim do arquivo |

## Scroll e viewport

### Modo View (`z`)

| Tecla | Ação |
|-------|------|
| `zz` / `zc` | Centralizar linha na tela |
| `zt` | Alinhar linha ao topo |
| `zb` | Alinhar linha à base |
| `zj` / `Ctrl-d` | Meia página abaixo |
| `zk` / `Ctrl-u` | Meia página acima |
| `Ctrl-f` / `PageDown` | Página inteira abaixo |
| `Ctrl-b` / `PageUp` | Página inteira acima |

### Modo View sticky (`Z`)

Igual ao `z`, mas **persiste** até pressionar `Esc`. Útil para leitura prolongada.

## Jumplist (histórico de saltos)

| Tecla | Ação |
|-------|------|
| `Ctrl-o` | Voltar no jumplist |
| `Ctrl-i` | Avançar no jumplist |
| `Ctrl-s` | Salvar seleção atual no jumplist |

O jumplist registra saltos de `gd` (goto definition), buscas, e navegação entre arquivos.

## Modo Goto (`g`)

| Tecla | Ação |
|-------|------|
| `gg` | Início do arquivo |
| `ge` | Fim do arquivo |
| `gh` | Início da linha |
| `gl` | Fim da linha |
| `gs` | Primeiro não-branco da linha |
| `gt` | Topo da viewport |
| `gc` | Centro da viewport |
| `gb` | Base da viewport |
| `gn` | Próximo buffer |
| `gp` | Buffer anterior |
| `ga` | Último arquivo acessado |
| `gm` | Último arquivo modificado |
| `g.` | Última modificação no arquivo |
| `gw` | Goto word (labels na tela) |

### Goto LSP (requer language server)

| Tecla | Ação |
|-------|------|
| `gd` | Goto definition |
| `gy` | Goto type definition |
| `gr` | Goto references |
| `gi` | Goto implementation |

## Navegação estrutural (Tree-sitter)

Requer grammar tree-sitter para o tipo de arquivo.

| Tecla | Ação |
|-------|------|
| `Alt-o` / `Alt+↑` | Expandir seleção para nó pai |
| `Alt-i` / `Alt+↓` | Contrair seleção |
| `Alt-p` / `Alt+←` | Nó irmão anterior |
| `Alt-n` / `Alt+→` | Próximo nó irmão |
| `Alt-a` | Todos os irmãos |
| `Alt-I` | Todos os filhos |
| `Alt-e` | Fim do nó pai |
| `Alt-b` | Início do nó pai |

## Navegação por função/tipo (unimpaired)

| Tecla | Ação |
|-------|------|
| `]f` / `[f` | Próxima / anterior função |
| `]t` / `[t` | Próximo / anterior tipo/classe |
| `]a` / `[a` | Próximo / anterior parâmetro |
| `]c` / `[c` | Próximo / anterior comentário |
| `]T` / `[T` | Próximo / anterior teste |
| `]p` / `[p` | Próximo / anterior parágrafo |
| `]g` / `[g` | Próxima / anterior mudança |
| `]d` / `[d` | Próximo / anterior diagnóstico LSP |

## Dicas de navegação

1. **Combine `f` com repetição** — `f;` não existe; use `Alt-.` para repetir.
2. **Use `gw` para saltos rápidos** — mostra labels em cada palavra visível.
3. **`Ctrl-o` é seu amigo** — sempre volte de onde veio após `gd`.
4. **Números relativos** — com `line-number = "relative"`, `5j` pula 5 linhas visualmente.

## Próximo passo

[05 — Edição e Seleções](./05-edicao-e-selecoes.md)
