# 03 — Filosofia Modal

## O paradigma Kakoune

O Helix segue o modelo **seleção → ação** do Kakoune, diferente do Vim (ação → movimento):

```
Vim:     d w     → "delete word" (ação depois movimento)
Helix:   w d     → seleciona palavra, depois deleta
         ou:     x d  → seleciona linha, deleta
```

Isso torna as operações **visuais e previsíveis**: você sempre vê o que será afetado antes de agir.

## Os três modos principais

### Normal mode (padrão)

- Ativado ao abrir o Helix ou ao pressionar `Esc`.
- Usado para navegar, selecionar e comandar.
- **Não digita texto** — apenas comanda.

### Insert mode

- Entrada: `i` (antes da seleção), `a` (depois), `o` (linha abaixo), `O` (linha acima).
- Saída: `Esc` → volta ao normal mode.
- Mudanças só entram no histórico de undo ao sair do insert mode.

> **Dica:** `Ctrl+s` no insert mode cria um checkpoint de undo (commit).

### Select mode (extend)

- Entrada: `v` no normal mode.
- Movimentos **estendem** a seleção em vez de substituí-la.
- Útil para seleções complexas com precisão.

## Fluxo mental recomendado

```
1. Navegue até o alvo        (h j k l, w, b, f, g...)
2. Selecione o que precisa   (x, X, v, Alt+o, textobjects)
3. Aja sobre a seleção       (d, y, c, =, Ctrl+c)
4. Volte ao normal mode      (Esc)
```

## Seleção primária vs múltiplas seleções

- O Helix suporta **múltiplas seleções** (cursors).
- A seleção **primária** é a principal; as outras são secundárias.
- `,` — mantém apenas a seleção primária.
- `Alt-,` — remove a seleção primária.
- `C` — copia seleção para linha abaixo (multi-cursor).
- `Alt-C` — copia seleção para linha acima.

## Sub-modos (camadas de atalhos)

Sub-modos são prefixos que abrem um menu temporário de comandos:

| Tecla | Sub-modo | Persistência |
|-------|----------|--------------|
| `g` | Goto | Uma tecla |
| `m` | Match / surround / textobject | Uma tecla |
| `z` | View (scroll) | Uma tecla |
| `Z` | View sticky | Até `Esc` |
| `Space` | Pickers e LSP | Uma tecla |
| `Ctrl-w` | Janelas | Uma tecla |
| `:` | Command mode | Até `Enter` |

## Undo e histórico

| Atalho | Ação |
|--------|------|
| `u` | Desfazer |
| `U` | Refazer |
| `Alt-u` | Voltar no histórico (earlier) |
| `Alt-U` | Avançar no histórico (later) |

No insert mode, `Ctrl+s` cria um checkpoint — útil para desfazer blocos de digitação sem sair do insert mode.

## Registers (registros)

Registros armazenam texto copiado (yank):

```
"ay     → yank para registro 'a'
"ap     → colar do registro 'a'
"       → escolher registro interativamente
```

O registro `/` é usado para busca. O `"` sem sufixo abre seletor de registro.

## Por que modal editing é mais rápido

1. **Menos teclas** — `ci"` muda dentro de aspas; no editor comum são muitos cliques.
2. **Sem sair do teclado** — mãos permanecem na home row.
3. **Operações compostas** — seleção + ação é um padrão repetível.
4. **Menos erros** — você vê a seleção antes de deletar/alterar.

## Adaptação para quem vem do Vim

| Vim | Helix | Nota |
|-----|-------|------|
| `dd` | `xd` | Seleciona linha, deleta |
| `ciw` | `w c` | Seleciona palavra, change |
| `yy` | `xy` | Seleciona linha, yank |
| `p` | `p` | Paste (igual) |
| `u` | `u` | Undo (igual) |
| `v` (visual) | `v` (select/extend) | Comportamento diferente |
| `gd` | `gd` | Goto definition (igual!) |

## Próximo passo

[04 — Movimentação e Navegação](./04-movimentacao-e-navegacao.md)
