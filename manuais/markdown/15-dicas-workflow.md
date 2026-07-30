# 15 — Dicas e Workflow

## Workflow diário recomendado

### Iniciar sessão de trabalho

```bash
cd ~/projects/meu-projeto
hx .
```

O `.` abre o file picker na raiz do projeto.

### Fluxo de edição típico

```
1. Space f          → abrir arquivo
2. /função          → buscar função
3. gd               → ir à definição
4. Space k          → ler documentação
5. c                → editar
6. Esc              → confirmar (auto-save salva)
7. Ctrl-o           → voltar ao arquivo anterior
```

### Revisar erros

```
Space d             → picker de diagnósticos
]d ]d ]d            → navegar entre erros
Space a             → aplicar quick fix
```

### Refatorar

```
Space r             → rename symbol
Space h             → selecionar todas as referências
c                   → editar todas simultaneamente
```

## Dicas de produtividade

### 1. Domine o Space mode

`Space` é o atalho mais importante. Memorize:

```
Space f    → arquivos
Space b    → buffers
Space k    → hover
Space a    → code action
Space r    → rename
Space /    → busca global
Space ?    → command palette
```

### 2. Use textobjects em vez de movimentos manuais

```
mif    → função inteira (em vez de V%kd)
mi"    → dentro de aspas (em vez de f"vf")
mac    → classe inteira
```

### 3. Tree-sitter para seleção estrutural

```
Alt-o  → expandir para nó pai (função → classe → módulo)
Alt-i  → contrair
Alt-n  → próximo irmão (próximo método)
```

### 4. Jumplist é seu histórico de navegação

Após `gd`, `gr`, `Space /` → `Enter`:
```
Ctrl-o  → voltar
Ctrl-i  → avançar
Space j → ver histórico visual
```

### 5. Múltiplas seleções para edição em massa

```
s/padrão     → selecionar todos os matches
c novo       → substituir todos de uma vez
```

### 6. Shell pipe para transformações

```
|sort        → ordenar
|uniq        → deduplicar
|jq .        → formatar JSON
|sed 's/a/b' → substituir
```

### 7. Auto-save elimina `:w`

Com `auto-save = true`, foque em editar. `Ctrl+s` ainda funciona para salvar manualmente.

### 8. Desabilite setas no insert mode

Quando confortável com modal editing, desabilite no config.toml:

```toml
[keys.insert]
up = "no_op"
down = "no_op"
left = "no_op"
right = "no_op"
```

Isso força o uso de `Esc` + movimento + `i/a`, acelerando a edição.

## Adaptação do Vim

| Hábito Vim | Equivalente Helix |
|------------|-------------------|
| `dd` | `xd` |
| `ciw` | `w c` |
| `yy` | `xy` |
| `vip` | `map` |
| `ci"` | `mi" c` |
| `:%s/old/new/g` | `:%s/old/new/g` (igual) |
| `:terminal` | Use tmux — veja [manual 17](./17-terminal-e-sessoes-persistentes.md) |
| Plugins | Não existe — use LSP nativo |

## Troubleshooting comum

| Problema | Solução |
|----------|---------|
| Atalho não funciona | Conflito com terminal — veja [wiki do Helix](https://github.com/helix-editor/helix/wiki/Terminal-alternate-keys) |
| LSP lento | Aumente `timeout` em languages.toml |
| LSP não inicia | `hx --health <lang>` — verifique binário e root markers |
| Tema com cores erradas | `true-color = true` + terminal com suporte a true color |
| Auto-format quebra código | Desabilite por linguagem: `auto-format = false` |
| Snap não encontra LSP | Verifique PATH — snap pode ter PATH limitado |
| Helix não vê `~/go/bin` | Reinicie terminal após editar `.bashrc` |

### Conflitos de terminal (Pop!_OS / GNOME Terminal)

| Tecla | Conflito | Solução |
|-------|----------|---------|
| `Ctrl-Shift` | Atalhos do terminal | Remapear no terminal ou usar alternativas |
| `Ctrl-h` | Backspace em alguns terminais | Use `Ctrl-w h` (window mode) |

## Helix + tmux

O Helix não tem terminal embutido. Use **tmux** para manter sessões vivas, splits de terminal e restaurar layout após reboot.

Guia completo: **[17 — Terminal e Sessões Persistentes](./17-terminal-e-sessoes-persistentes.md)**

Resumo rápido:

```bash
tmux new -s dev       # criar sessão
hx .                  # abrir Helix dentro do tmux
Ctrl+b d              # detach (sessão continua)
tmux a -t dev         # reconectar
```

## Helix + Git

```
Space g             → changed files picker
:!git diff          → ver diff no terminal
:!git status        → status
```

Para diff visual, use ferramenta externa ou:

```
:diff-toggle        → ativar diff entre buffers
```

## Aprendizado progressivo

### Semana 1 — Fundamentos
- Modos (normal, insert, select)
- Movimentos básicos (`h j k l w b e`)
- Edição (`x d c y p u`)
- Salvar e sair (`Ctrl+s`, `:q`)

### Semana 2 — Navegação
- Goto mode (`gd`, `gr`, `gg`, `ge`)
- Space mode (`Space f`, `Space b`, `Space k`)
- Busca (`/`, `n`, `Space /`)

### Semana 3 — Produtividade
- Textobjects (`mif`, `mi"`, `mac`)
- Tree-sitter (`Alt-o`, `Alt-i`)
- LSP (`Space a`, `Space r`, `]d`)
- Splits (`Ctrl-w v`, `Ctrl-w s`)

### Semana 4 — Maestria
- Múltiplas seleções
- Shell pipe (`|sort`, `|jq`)
- Configuração avançada
- Macros
- Terminal e tmux ([manual 17](./17-terminal-e-sessoes-persistentes.md))

## Recursos externos

| Recurso | URL |
|---------|-----|
| Documentação oficial | https://docs.helix-editor.com/ |
| GitHub | https://github.com/helix-editor/helix |
| Keymap interativo | `:tutor` (dentro do Helix) |
| Wiki | https://github.com/helix-editor/helix/wiki |
| Matrix chat | #helix-editor:matrix.org |

## Próximo passo

[17 — Terminal e Sessões Persistentes](./17-terminal-e-sessoes-persistentes.md)
