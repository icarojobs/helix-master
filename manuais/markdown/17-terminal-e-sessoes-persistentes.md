# 17 — Terminal e Sessões Persistentes

O Helix **não possui terminal embutido**. Para compilar, rodar testes, servidores e Git, você trabalha com um **terminal externo** — idealmente dentro de **tmux**, que mantém suas sessões vivas mesmo se o terminal fechar ou a conexão SSH cair.

> **Por que tmux e não screen?** Para o perfil de desenvolvimento backend/DevOps (Go, Python, Docker, servidores remotos), o **tmux** é o padrão da indústria: mais ativo, melhor documentação, plugins maduros e integração natural com workflows modernos. O `screen` ainda funciona, mas o tmux oferece mais controle com menos fricção.

---

## Parte 1 — Abrindo o terminal

### Pop!_OS / Ubuntu (seu SO)

| Método | Como |
|--------|------|
| Atalho de teclado | `Ctrl + Alt + T` |
| Menu de aplicativos | Tecla `Super` (Windows) → digite **Terminal** → Enter |
| Launcher | `Super + /` → busque "Terminal" |
| Dentro do VS Code/Cursor | `` Ctrl + ` `` (crase) — terminal integrado |

### Terminais recomendados

| Terminal | Quando usar |
|----------|-------------|
| **Terminal do sistema** (padrão Pop!_OS) | Uso geral, já vem instalado |
| **Alacritty** | Leve, GPU-accelerated, minimalista |
| **Wezterm** | Moderno, splits nativos, Lua config |
| **Kitty** | Performance, imagens no terminal |

Para Helix + tmux, qualquer terminal com suporte a **256 cores / true color** funciona.

### Verificar cores no terminal

```bash
echo $TERM
# Esperado: xterm-256color ou tmux-256color (dentro do tmux)

# Teste rápido de cores
for i in {0..15}; do printf "\e[48;5;${i}m  \e[0m"; done; echo
```

---

## Parte 2 — Conceitos do tmux

| Termo | Significado |
|-------|-------------|
| **Session** | Grupo de janelas — sua "mesa de trabalho" |
| **Window** | Aba dentro da sessão (ex: editor, servidor, logs) |
| **Pane** | Divisão dentro de uma janela (split) |
| **Prefix** | Tecla que precede comandos tmux — padrão: `Ctrl+b` |

### Fluxo mental

```
tmux session "dev"
├── window 0: helix (editor)
├── window 1: servidor (make up / go run)
├── window 2: logs (docker logs -f)
└── window 3: shell livre (git, testes)
```

---

## Parte 3 — Instalação

```bash
# Ubuntu / Pop!_OS / Debian
sudo apt update && sudo apt install -y tmux

# Verificar
tmux -V
# tmux 3.2a (ou superior)
```

---

## Parte 4 — Comandos essenciais

### Sessões

| Comando / Atalho | Ação |
|------------------|------|
| `tmux` | Nova sessão |
| `tmux new -s dev` | Nova sessão nomeada "dev" |
| `tmux ls` | Listar sessões ativas |
| `tmux attach -t dev` | Reconectar à sessão "dev" |
| `tmux kill-session -t dev` | Encerrar sessão |
| `Ctrl+b d` | **Detach** — sai do tmux sem matar a sessão |

### Janelas (windows)

| Atalho | Ação |
|--------|------|
| `Ctrl+b c` | Nova janela |
| `Ctrl+b n` | Próxima janela |
| `Ctrl+b p` | Janela anterior |
| `Ctrl+b 0`–`9` | Ir para janela N |
| `Ctrl+b ,` | Renomear janela atual |
| `Ctrl+b &` | Fechar janela (confirma) |

### Panes (splits)

| Atalho | Ação |
|--------|------|
| `Ctrl+b %` | Split vertical (lado a lado) |
| `Ctrl+b "` | Split horizontal (empilhado) |
| `Ctrl+b set` | Alternar layout |
| `Ctrl+b o` | Próximo pane |
| `Ctrl+b ;` | Último pane |
| `Ctrl+b x` | Fechar pane atual |
| `Ctrl+b z` | Zoom toggle (fullscreen do pane) |
| `Ctrl+b {` / `}` | Mover pane |
| `Ctrl+b h/j/k/l` | Navegar entre panes |

### Scroll e cópia

| Atalho | Ação |
|--------|------|
| `Ctrl+b [` | Modo cópia (scroll) — `q` para sair |
| `Ctrl+b ]` | Colar buffer |
| `Ctrl+b PgUp` | Scroll up (em versões recentes) |

---

## Parte 5 — Workflow Helix + tmux

### Layout recomendado para desenvolvimento

```bash
# Criar sessão de desenvolvimento
tmux new-session -s dev -n editor

# Dentro do tmux — abrir Helix
hx .

# Nova janela para servidor/testes
# Ctrl+b c
make test
# ou: go test ./...
# ou: docker compose up

# Nova janela para Git/shell
# Ctrl+b c
git status
```

### Layout com split (editor + terminal lado a lado)

```bash
tmux new-session -s dev -n code

# Split vertical: editor à esquerda, shell à direita
# Ctrl+b %
hx .          # no pane esquerdo
# Ctrl+b o    # focar pane direito
make watch    # ou qualquer comando
```

### Sair sem perder nada

```
Ctrl+b d      → detach (sessão continua rodando em background)
```

Reconectar depois:

```bash
tmux attach -t dev
# ou atalho:
tmux a -t dev
```

---

## Parte 6 — Sessões que sobrevivem a reinício

> **Importante:** o tmux sozinho **não sobrevive a um reboot** — o processo morre com o sistema. Para restaurar sessões após reinício, use **tmux-resurrect** + **tmux-continuum**.

### Instalar plugins (TPM — Tmux Plugin Manager)

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

### Configurar `~/.tmux.conf`

```bash
cat >> ~/.tmux.conf << 'EOF'
# ── Básico ──────────────────────────────────────────────────
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"
set -g mouse on
set -g history-limit 50000
set -g base-index 1
setw -g pane-base-index 1

# Renumerar janelas ao fechar
set -g renumber-windows on

# Vim-style pane navigation
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Split com diretório atual
bind '"' split-window -v -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"
bind c new-window -c "#{pane_current_path}"

# ── Plugins ─────────────────────────────────────────────────
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# Restaurar sessões automaticamente ao iniciar tmux
set -g @continuum-restore 'on'

# Salvar a cada 15 minutos (padrão)
set -g @continuum-save-interval '15'

# Restaurar processos (cuidado: não salve senhas em comandos)
set -g @resurrect-processes 'false'

# Iniciar TPM (manter no final)
run '~/.tmux/plugins/tpm/tpm'
EOF
```

### Instalar plugins

```bash
tmux source ~/.tmux.conf
# Dentro do tmux:
# Ctrl+b I    → instalar plugins
```

### Como funciona após reboot

1. Computador reinicia.
2. Você abre o terminal e digita `tmux`.
3. **tmux-continuum** restaura automaticamente a última sessão salva.
4. Janelas, panes e diretórios voltam — comandos em execução **não** são restaurados (por segurança).

### Salvar manualmente

```
Ctrl+b Ctrl+s    → salvar sessão agora (tmux-resurrect)
```

### Restaurar manualmente

```
Ctrl+b Ctrl+r    → restaurar última sessão salva
```

---

## Parte 7 — Auto-iniciar tmux ao abrir terminal (opcional)

Para sempre cair dentro do tmux ao abrir o terminal:

```bash
# Adicione ao ~/.bashrc (apenas se quiser tmux automático)
if command -v tmux &>/dev/null && [ -z "$TMUX" ] && [[ $- == *i* ]]; then
  tmux attach-session -t main 2>/dev/null || tmux new-session -s main
fi
```

> **Atenção:** isso pode confundir no início. Recomendamos dominar o tmux manualmente antes de ativar.

---

## Parte 8 — Servidor remoto (SSH + tmux)

Para desenvolvimento em servidor remoto (VPS, máquina de dev):

```bash
# Conectar ao servidor
ssh usuario@servidor

# Criar ou reconectar sessão
tmux new -s dev || tmux attach -t dev

# Dentro: abrir Helix
hx ~/projects/meu-projeto
```

Se a conexão SSH cair, a sessão tmux **continua rodando no servidor**. Reconecte com `ssh` + `tmux attach -t dev`.

### Dica: alias no `~/.bashrc` local

```bash
alias sdev='ssh usuario@servidor -t "tmux attach -t dev || tmux new -s dev"'
```

---

## Parte 9 — tmux vs screen (referência rápida)

| Recurso | tmux | screen |
|---------|------|--------|
| Atividade do projeto | Ativo | Legado |
| Plugins | TPM (rico) | Limitado |
| Splits | Nativo, flexível | Básico |
| Config | `~/.tmux.conf` | `~/.screenrc` |
| Restaurar após reboot | tmux-continuum | Não nativo |
| Padrão DevOps | **Sim** | Raro em projetos novos |

**Veredito:** use **tmux**. O `screen` só faz sentido em sistemas muito antigos onde o tmux não está disponível.

---

## Parte 10 — Troubleshooting

| Problema | Solução |
|----------|---------|
| Cores erradas no Helix | `set -g default-terminal "tmux-256color"` no `.tmux.conf` |
| `tmux: command not found` | `sudo apt install tmux` |
| Sessão não restaura após reboot | Verifique se TPM e continuum estão instalados (`Ctrl+b I`) |
| Scroll não funciona | `set -g mouse on` no `.tmux.conf` |
| Prefix `Ctrl+b` conflita | Remapeie: `unbind C-b; set -g prefix C-a` |
| Plugin não instala | `git clone` do TPM em `~/.tmux/plugins/tpm` |

---

## Workflow completo recomendado

```bash
# 1. Abrir terminal
Ctrl+Alt+T

# 2. Entrar ou criar sessão tmux
tmux new -s dev    # primeira vez
tmux a -t dev      # próximas vezes

# 3. Abrir Helix no projeto
cd ~/projects/meu-projeto && hx .

# 4. Split para testes (Ctrl+b ")
make test

# 5. Sair sem matar nada
Ctrl+b d

# 6. Após reboot do PC
tmux               # continuum restaura automaticamente
```

## Próximo passo

[← Voltar ao índice](./README.md) · [16 — Referência Rápida](./16-referencia-rapida.md)
