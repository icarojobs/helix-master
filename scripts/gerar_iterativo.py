#!/usr/bin/env python3
"""Gera slides HTML interativos do curso Helix Master (padrão cursos-youtube)."""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "manuais" / "iterativo"
CSS_JS = (Path(__file__).resolve().parent / "nucleo_template.html").read_text(encoding="utf-8")

CURSO = "Helix Master"
MARCA = "Icaro William"
REPO = "https://github.com/icarojobs/helix-master"


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slide_titulo(kicker: str, titulo: str, subtitulo: str, hint: bool = True) -> str:
    hint_html = (
        '<p class="hint">Use ← → ou espaço para navegar · F = tela cheia</p>'
        if hint
        else ""
    )
    return f"""
  <section class="slide">
    <div class="wrap" style="text-align:center">
      <p class="kicker reveal">{kicker}</p>
      <h1 class="type">{titulo}</h1>
      <p class="subtitle reveal">{subtitulo}</p>
    </div>
    {hint_html}
  </section>"""


def slide_lista(titulo: str, itens: list[str], dica: str | None = None) -> str:
    lis = "\n".join(f'        <li class="reveal">{item}</li>' for item in itens)
    dica_html = f'<div class="tip reveal">{dica}</div>' if dica else ""
    return f"""
  <section class="slide">
    <div class="wrap">
      <h2>{titulo}</h2>
      <ul class="list">
{lis}
      </ul>
      {dica_html}
    </div>
  </section>"""


def slide_term(titulo: str, barra: str, codigo: str) -> str:
    return f"""
  <section class="slide">
    <div class="wrap">
      <h2>{titulo}</h2>
      <div class="term reveal">
        <div class="term-bar"><i></i><i></i><i></i><span>{barra}</span></div>
        <pre><code>{codigo}</code></pre>
      </div>
    </div>
  </section>"""


def slide_tabela(titulo: str, cabecalho: tuple[str, str], linhas: list[tuple[str, str]]) -> str:
    rows = "\n".join(f"          <tr><td>{a}</td><td>{b}</td></tr>" for a, b in linhas)
    return f"""
  <section class="slide">
    <div class="wrap">
      <h2>{titulo}</h2>
      <div class="reveal">
        <table>
          <tr><th>{cabecalho[0]}</th><th>{cabecalho[1]}</th></tr>
{rows}
        </table>
      </div>
    </div>
  </section>"""


def slide_dicas(titulos_dicas: list[str]) -> str:
    blocos = "\n".join(f'      <div class="tip reveal">{d}</div>' for d in titulos_dicas)
    return f"""
  <section class="slide">
    <div class="wrap">
      <h2>Dicas profissionais 💡</h2>
{blocos}
    </div>
  </section>"""


def slide_recap(itens: list[str]) -> str:
    return slide_lista("Recapitulando 📌", itens)


def slide_final(proxima: str) -> str:
    return f"""
  <section class="slide">
    <div class="wrap" style="text-align:center">
      <span class="badge reveal">Próxima aula</span>
      <h1 class="reveal" style="font-size:clamp(2rem,3.4vw,4rem)">{proxima}</h1>
      <p class="subtitle reveal">Siga na ordem — cada aula constrói sobre a anterior.</p>
      <div class="contact">
        <p class="reveal"><b>{MARCA}</b> · Arquiteto de Software</p>
        <p class="reveal">🐙 <a href="{REPO}">github.com/icarojobs/helix-master</a></p>
      </div>
    </div>
  </section>"""


def montar_html(meta: dict) -> str:
    partes = CSS_JS.split("/* __SLIDES__ */")
    if len(partes) != 2:
        raise RuntimeError("Template inválido: marcador /* __SLIDES__ */ ausente")
    head, tail = partes
    head = head.replace("{{TITLE}}", meta["title"])
    head = head.replace("{{ACCENT}}", meta["accent"])
    tail = tail.replace("{{BRAND}}", CURSO)
    return head + "\n".join(meta["slides"]) + tail


# ---------------------------------------------------------------------------
# Conteúdo das aulas (teoria → mão na massa → recapitulando)
# ---------------------------------------------------------------------------

AULAS: list[dict] = []

def aula(num: str, nome: str, accent: str, slides: list[str], proxima: str) -> None:
    AULAS.append({
        "num": num,
        "nome": nome,
        "accent": accent,
        "title": f"Aula {num} — {nome} | {CURSO}",
        "slides": slides + [slide_final(proxima)],
        "arquivo": f"{num} - {nome}.html",
    })


# 00 — Roadmap
aula("00", "Roadmap e Pré-requisitos", "#00ff9c", [
    slide_titulo(CURSO, "Aula 00 — Roadmap e Pré-requisitos",
                 "Do zero ao domínio total do Helix Editor — trilha guiada para Debian/macOS."),
    slide_lista("O que é este curso? 🤔", [
        "Trilha <b>iterativa</b> (slides + terminal) paralela aos manuais em Markdown;",
        "18 aulas em ordem — da instalação à maestria com tmux;",
        "Cada aula segue: <b>teoria → mão na massa → recapitulando</b>;",
        "Foco em desenvolvimento full-stack: Python, Go, Rust, PHP, Web, SQL;",
        "Funciona em <b>Debian/Ubuntu/Pop!_OS</b> e <b>macOS</b>.",
    ]),
    slide_tabela("Estrutura da trilha 🗺️", ("Aulas", "Módulo"), [
        ("00–02", "Instalação e fundamentos"),
        ("03–05", "Modal, movimentação e edição"),
        ("06–08", "Atalhos, goto e LSP"),
        ("09–11", "Busca, buffers e comandos"),
        ("12–14", "Config avançada, linguagens e macros"),
        ("15–17", "Workflow, referência e tmux"),
    ]),
    slide_lista("O que você precisa? 🛠️", [
        "Terminal (Linux: <span class='kbd'>Ctrl+Alt+T</span> · macOS: Terminal.app ou iTerm2);",
        "Conta de usuário com permissão de instalar pacotes (sudo no Linux);",
        "Conexão com internet para baixar Helix e language servers;",
        "Editor de texto qualquer para editar configs (o Helix será instalado na Aula 02).",
    ], "<b>💡 Dica:</b> abra os slides no monitor 2 e execute os comandos no monitor 1."),
    slide_lista("Metodologia 📋", [
        "<b>O que é?</b> — conceito direto, sem enrolação;",
        "<b>Quando usar?</b> — situações reais do dia a dia;",
        "<b>Como usar?</b> — exemplos e atalhos;",
        "<b>Mão na massa</b> — comandos completos no terminal;",
        "<b>Recapitulando</b> — fixação antes da próxima aula.",
    ]),
    slide_term("Mão na massa — 1/2: clonar o repositório 📦", "terminal", """<span class="cm"># Clone o material de apoio</span>
git clone git@github.com:icarojobs/helix-master.git
cd helix-master
ls manuais/markdown manuais/iterativo exemplos"""),
    slide_term("Mão na massa — 2/2: abrir a trilha interativa 🖥️", "navegador ou terminal", """<span class="cm"># Abra o índice dos slides (Linux)</span>
xdg-open manuais/iterativo/README.md

<span class="cm"># macOS</span>
open manuais/iterativo/README.md

<span class="cm"># Ou abra direto a Aula 00 no navegador</span>
firefox "manuais/iterativo/00 - Roadmap e Pré-requisitos.html\""""),
    slide_recap([
        "18 aulas ordenadas — siga do 00 ao 17;",
        "Manuais Markdown em <code class='inline'>manuais/markdown/</code>;",
        "Slides interativos em <code class='inline'>manuais/iterativo/</code>;",
        "Configs prontas em <code class='inline'>exemplos/</code>;",
        "Próximo passo: instalar o Helix na Aula 02.",
    ]),
], "01 — Introdução ao Helix")

# 01 — Introdução
aula("01", "Introdução ao Helix", "#00ff9c", [
    slide_titulo(CURSO, "Aula 01 — Introdução ao Helix",
                 "Editor modal em Rust: seleção primeiro, LSP nativo, zero plugins."),
    slide_lista("O que é o Helix? 🤔", [
        "Editor de texto <b>modal</b> escrito em Rust;",
        "Inspirado no <b>Kakoune</b> (seleção → ação) e no Vim;",
        "<b>Tree-sitter</b> nativo para syntax e textobjects;",
        "<b>LSP embutido</b> — autocomplete, diagnósticos, goto, rename;",
        "Funciona out-of-the-box — configuração é opcional e poderosa.",
    ]),
    slide_tabela("Helix vs Vim/Neovim 🎯", ("Aspecto", "Helix"), [
        ("Modelo", "Seleção → ação (Kakoune)"),
        ("Plugins", "Não suporta — tudo embutido"),
        ("Config", "TOML simples"),
        ("LSP", "Nativo, de primeira classe"),
        ("Curva", "Moderada (menor que Neovim)"),
    ]),
    slide_lista("Quando usar o Helix? 🎯", [
        "Quer editor <b>rápido</b> sem gerenciar dezenas de plugins;",
        "Valoriza <b>LSP</b> e tree-sitter desde o primeiro dia;",
        "Gosta de edição modal mas prefere modelo Kakoune;",
        "Trabalha com múltiplas linguagens (backend + frontend + infra).",
    ]),
    slide_lista("Conceitos fundamentais 🛠️", [
        "<b>Modos:</b> normal (comandar), insert (digitar), select (estender);",
        "<b>Seleções:</b> toda operação age sobre uma região de texto;",
        "<b>Sub-modos:</b> <span class='kbd'>g</span> goto, <span class='kbd'>Space</span> pickers, <span class='kbd'>m</span> match;",
        "<b>Comandos:</b> <span class='kbd'>:</span> para salvar, sair, configurar.",
    ]),
    slide_term("Mão na massa — 1/2: verificar se hx existe 🔍", "terminal", """<span class="cm"># Se ainda não instalou, pule para a Aula 02</span>
which hx
hx --version

<span class="cm"># Abrir arquivo de teste</span>
echo 'print("hello helix")' > /tmp/teste.py
hx /tmp/teste.py"""),
    slide_term("Mão na massa — 2/2: primeiros comandos no Helix ⌨️", "dentro do hx", """<span class="cm"># Modo normal (padrão ao abrir)</span>
<span class="kw">i</span>          <span class="cm"># insert — digite algo</span>
<span class="kw">Esc</span>        <span class="cm"># volta ao normal</span>
<span class="kw">x</span>          <span class="cm"># seleciona linha</span>
<span class="kw">d</span>          <span class="cm"># deleta seleção</span>
<span class="kw">u</span>          <span class="cm"># undo</span>
<span class="kw">:q</span>         <span class="cm"># sair</span>"""),
    slide_dicas([
        "<b>💡 Não lute contra o Vim:</b> no Helix você seleciona primeiro, depois age (<span class='kbd'>xd</span> em vez de <span class='kbd'>dd</span>).",
        "<b>📖 Documentação oficial:</b> docs.helix-editor.com",
        "<b>⌨️ Ajuda interna:</b> digite <span class='kbd'>:help</span> dentro do Helix.",
    ]),
    slide_recap([
        "Helix = modal + seleção primeiro + LSP nativo + tree-sitter;",
        "Três modos: normal, insert, select;",
        "Sem plugins — tudo embutido;",
        "Próximo: instalação completa em Debian e macOS.",
    ]),
], "02 — Instalação e Configuração")

# 02 — Instalação (long lesson with hands-on for both OS)
aula("02", "Instalação e Configuração", "#00ff9c", [
    slide_titulo(CURSO, "Aula 02 — Instalação e Configuração",
                 "Helix + LSPs + atalhos — setup completo para Debian e macOS."),
    slide_lista("O que vamos instalar? 🤔", [
        "<b>Helix</b> — o editor (<span class='kbd'>hx</span>);",
        "<b>Language servers</b> — inteligência por linguagem;",
        "<b>config.toml</b> — tema, editor e atalhos;",
        "<b>languages.toml</b> — mapeamento LSP por linguagem.",
    ]),
    slide_term("Mão na massa — 1/6: Helix no Linux 🐧", "Debian / Ubuntu / Pop!_OS", """<span class="cm"># Opção A — Snap (recomendada)</span>
sudo snap install helix --classic
hx --version

<span class="cm"># Opção B — Homebrew no Linux</span>
<span class="cm"># brew install helix</span>"""),
    slide_term("Mão na massa — 2/6: Helix no macOS 🍎", "macOS + Homebrew", """<span class="cm"># Instalar Homebrew se necessário: https://brew.sh</span>
brew install helix
hx --version

<span class="cm"># Atualizar depois</span>
brew upgrade helix"""),
    slide_term("Mão na massa — 3/6: instalar LSPs (Linux) 🧠", "dentro do repositório helix-master", """cd ~/projects/icarojobs/helix-master
bash exemplos/install-lsps-linux.sh
source ~/.bashrc"""),
    slide_term("Mão na massa — 4/6: instalar LSPs (macOS) 🧠", "dentro do repositório helix-master", """cd ~/projects/icarojobs/helix-master
bash exemplos/install-lsps-macos.sh
source ~/.zshrc"""),
    slide_term("Mão na massa — 5/6: copiar configs ⚙️", "terminal", """mkdir -p ~/.config/helix
cp exemplos/config.toml ~/.config/helix/
cp exemplos/languages.toml ~/.config/helix/

<span class="cm"># Edite conexões SQL depois (use placeholders)</span>
nano ~/.config/helix/languages.toml"""),
    slide_term("Mão na massa — 6/6: validar tudo ✅", "terminal", """hx --health python
hx --health go
hx --health typescript
hx --health rust

<span class="cm"># Esperado: ✓ verde para cada LSP</span>
hx ."""),
    slide_tabela("Atalhos configurados 🎯", ("Atalho", "Ação"), [
        ("Ctrl+s", "Salvar"),
        ("Ctrl+Shift+s", "Salvar e sair"),
        ("Ctrl+h/j/k/l", "Navegar splits"),
        ("{ / }", "Diagnóstico anterior/próximo"),
        ("F", "Formatar arquivo"),
    ]),
    slide_recap([
        "Helix via snap (Linux) ou brew (macOS);",
        "LSPs via scripts em exemplos/;",
        "Configs em ~/.config/helix/;",
        "Valide com hx --health <lang>;",
        "Recarregue com :config-reload.",
    ]),
], "03 — Filosofia Modal")

# 03 — Filosofia Modal
aula("03", "Filosofia Modal", "#00d9ff", [
    slide_titulo(CURSO, "Aula 03 — Filosofia Modal",
                 "Seleção → ação: o paradigma Kakoune que muda tudo."),
    slide_lista("O que é edição modal? 🤔", [
        "Você alterna entre <b>modos</b> em vez de ficar sempre digitando;",
        "<b>Normal</b> — navegar e comandar (padrão);",
        "<b>Insert</b> — digitar texto;",
        "<b>Select</b> — estender seleção com movimentos.",
    ]),
    slide_lista("Seleção → ação (Kakoune) 🎯", [
        "<b>Vim:</b> <span class='kbd'>d</span> depois <span class='kbd'>w</span> — ação + movimento;",
        "<b>Helix:</b> <span class='kbd'>w</span> depois <span class='kbd'>d</span> — seleciona, depois age;",
        "Você <b>vê</b> o que será afetado antes de deletar/alterar;",
        "Exemplo: <span class='kbd'>xd</span> = seleciona linha + deleta (Vim: <span class='kbd'>dd</span>).",
    ]),
    slide_term("Mão na massa — 1/3: ciclo normal → insert 🔄", "dentro do hx", """<span class="kw">i</span>     <span class="cm"># insert antes da seleção</span>
<span class="cm"># digite: hello helix</span>
<span class="kw">Esc</span>   <span class="cm"># volta ao normal (undo checkpoint)</span>
<span class="kw">a</span>     <span class="cm"># append depois da seleção</span>
<span class="kw">o</span>     <span class="cm"># abre linha abaixo</span>
<span class="kw">O</span>     <span class="cm"># abre linha acima</span>"""),
    slide_term("Mão na massa — 2/3: seleção e ação ✂️", "dentro do hx", """<span class="kw">x</span>     <span class="cm"># seleciona linha</span>
<span class="kw">y</span>     <span class="cm"># yank (copia)</span>
<span class="kw">p</span>     <span class="cm"># cola depois</span>
<span class="kw">d</span>     <span class="cm"># deleta</span>
<span class="kw">c</span>     <span class="cm"># change (deleta + insert)</span>
<span class="kw">u</span>     <span class="cm"># undo</span>
<span class="kw">U</span>     <span class="cm"># redo</span>"""),
    slide_term("Mão na massa — 3/3: select mode 📐", "dentro do hx", """<span class="kw">v</span>     <span class="cm"># entra em select mode</span>
<span class="kw">w w w</span> <span class="cm"># estende seleção por palavras</span>
<span class="kw">d</span>     <span class="cm"># deleta tudo selecionado</span>
<span class="kw">Esc</span>   <span class="cm"># volta ao normal</span>"""),
    slide_dicas([
        "<b>💡 Esc é seu melhor amigo</b> — volte ao normal mode sempre que não estiver digitando.",
        "<b>🔄 Ctrl+s no insert</b> — cria checkpoint de undo sem sair do insert.",
        "<b>📋 Registros:</b> <span class='kbd'>\"ay</span> yank para registro a, <span class='kbd'>\"ap</span> colar.",
    ]),
    slide_recap([
        "Três modos: normal, insert, select;",
        "Padrão: selecionar → agir;",
        "xd ≈ dd, wc ≈ ciw no Vim;",
        "Mudanças entram no undo ao sair do insert.",
    ]),
], "04 — Movimentação e Navegação")

# 04-17 — I'll add remaining lessons with good content but slightly more compact for 04-16, full for 06, 08, 17

aula("04", "Movimentação e Navegação", "#00d9ff", [
    slide_titulo(CURSO, "Aula 04 — Movimentação e Navegação", "Domine h j k l, palavras, find e jumplist."),
    slide_lista("O que é? 🤔", ["Movimentação eficiente sem sair do teclado.", "h j k l — básico.", "w b e — palavras.", "f F t T — find char.", "gg ge G — arquivo.", "Ctrl-o/i — jumplist."]),
    slide_term("Mão na massa — 1/2: movimentos básicos 🏃", "hx arquivo.py", """<span class="kw">h j k l</span>   <span class="cm"># caracteres</span>
<span class="kw">w b e</span>     <span class="cm"># palavras</span>
<span class="kw">f</span>o<span class="kw">;</span>       <span class="cm"># find 'o' — Alt+. repete</span>
<span class="kw">gg</span>        <span class="cm"># início do arquivo</span>
<span class="kw">G</span>         <span class="cm"># fim (ou G42 para linha 42)</span>"""),
    slide_term("Mão na massa — 2/2: scroll e jumplist 📍", "hx", """<span class="kw">zz</span>        <span class="cm"># centraliza linha</span>
<span class="kw">Ctrl-d/u</span>  <span class="cm"># meia página</span>
<span class="kw">gd</span>        <span class="cm"># goto definition (LSP)</span>
<span class="kw">Ctrl-o</span>    <span class="cm"># volta no jumplist</span>
<span class="kw">Ctrl-i</span>    <span class="cm"># avança no jumplist</span>"""),
    slide_recap(["hjkl + wbef + find + gg/ge.", "zz para centralizar.", "Ctrl-o volta após gd.", "Alt-. repete último movimento."]),
], "05 — Edição e Seleções")

aula("05", "Edição e Seleções", "#00d9ff", [
    slide_titulo(CURSO, "Aula 05 — Edição e Seleções", "Yank, paste, surround, textobjects e tree-sitter."),
    slide_lista("O que é? 🤔", ["Operações sobre seleções.", "Surround: ms\" md\".", "Textobjects: mif mac mi\".", "Tree-sitter: Alt-o expandir, Alt-i contrair."]),
    slide_term("Mão na massa — 1/2: surround e textobjects 🎯", "hx", """<span class="kw">x</span>         <span class="cm"># seleciona linha</span>
<span class="kw">ms(</span>       <span class="cm"># surround com parênteses</span>
<span class="kw">mif</span>       <span class="cm"># inside function (TS)</span>
<span class="kw">mi\"</span>      <span class="cm"># inside aspas duplas</span>
<span class="kw">mac</span>       <span class="cm"># around class</span>"""),
    slide_term("Mão na massa — 2/2: múltiplas seleções 🔀", "hx", """<span class="kw">s</span>/pattern  <span class="cm"># seleciona matches regex</span>
<span class="kw">C</span>          <span class="cm"># cursor na linha abaixo</span>
<span class="kw">,</span>          <span class="cm"># mantém só seleção primária</span>
<span class="kw">|sort</span>      <span class="cm"># pipe shell na seleção</span>"""),
    slide_recap(["ms/md/mr para surround.", "mi/ma + textobject.", "s/regex para multi-select.", "Shell pipe | é poderoso."]),
], "06 — Atalhos Essenciais")

aula("06", "Atalhos Essenciais", "#bd93f9", [
    slide_titulo(CURSO, "Aula 06 — Atalhos Essenciais", "Configure e domine todos os keymaps."),
    slide_lista("O que são atalhos personalizados? 🤔", [
        "Helix usa TOML em <code class='inline'>~/.config/helix/config.toml</code>;",
        "Seções: <code class='inline'>[keys.normal]</code>, <code class='inline'>[keys.insert]</code>, <code class='inline'>[keys.select]</code>;",
        "Convenção: <span class='kbd'>C-s</span> = Ctrl+s, <span class='kbd'>A-x</span> = Alt+x;",
        "Use <code class='inline'>no_op</code> para desabilitar teclas.",
    ]),
    slide_term("Mão na massa — 1/3: abrir config ⚙️", "dentro do hx", """:config-open
<span class="cm"># ou no terminal:</span>
nano ~/.config/helix/config.toml"""),
    slide_term("Mão na massa — 2/3: atalhos no config 📝", "config.toml", """[keys.normal]
C-s = ":w"
C-S = ":wq"
C-q = ":q"
C-h = "jump_view_left"
"{" = "goto_prev_diag"
"}" = "goto_next_diag"
F = ":format"
S = "extend_to_line_bounds"

[keys.insert]
C-s = [":w", "normal_mode"]"""),
    slide_term("Mão na massa — 3/3: recarregar e testar ✅", "hx", """:config-reload

<span class="cm"># Teste:</span>
<span class="kw">Ctrl+s</span>   <span class="cm"># salvar</span>
<span class="kw">{</span> <span class="kw">}</span>    <span class="cm"># diagnósticos</span>
<span class="kw">F</span>        <span class="cm"># formatar</span>"""),
    slide_tabela("Atalhos nativos essenciais", ("Atalho", "Ação"), [
        ("Space f", "File picker"), ("Space k", "Hover"), ("Space a", "Code action"),
        ("Space r", "Rename"), ("gd", "Goto definition"), ("Ctrl+c", "Comentar"),
    ]),
    slide_recap(["Config em ~/.config/helix/config.toml.", "Copie exemplos/config.toml.", ":config-reload após mudanças.", "Space mode = centro de comando."]),
], "07 — Modo Goto e Space")

aula("07", "Modo Goto e Space", "#bd93f9", [
    slide_titulo(CURSO, "Aula 07 — Modo Goto e Space", "Sub-modos g e Space — navegação e pickers."),
    slide_lista("Modo Goto (g) 🤔", ["gg ge — arquivo.", "gd gy gr gi — LSP.", "gn gp — buffers.", "gw — goto word com labels."]),
    slide_lista("Modo Space 🤔", ["Space f — files.", "Space b — buffers.", "Space k/a/r — LSP.", "Space / — busca global.", "Space ? — command palette."]),
    slide_term("Mão na massa — 1/1: praticar sub-modos 🎮", "hx projeto/", """<span class="kw">Space f</span>   <span class="cm"># abrir arquivo</span>
<span class="kw">Space k</span>   <span class="cm"># hover</span>
<span class="kw">gd</span>        <span class="cm"># goto definition</span>
<span class="kw">Ctrl-o</span>    <span class="cm"># voltar</span>
<span class="kw">Space /</span>   <span class="cm"># busca global</span>
<span class="kw">Space '</span>   <span class="cm"># reabrir último picker</span>"""),
    slide_recap(["g = goto, Space = pickers/LSP.", "Space ' reabre último picker.", "gd + Ctrl-o = navegar e voltar.", "Space ? lista todos os comandos."]),
], "08 — LSP e Inteligência")

aula("08", "LSP e Inteligência", "#bd93f9", [
    slide_titulo(CURSO, "Aula 08 — LSP e Inteligência", "Autocomplete, diagnósticos, rename e code actions."),
    slide_lista("O que é LSP? 🤔", [
        "Language Server Protocol — inteligência por linguagem;",
        "Autocomplete, erros, goto, hover, rename, format;",
        "No Helix é <b>nativo</b> — sem plugins;",
        "Configure em <code class='inline'>languages.toml</code>.",
    ]),
    slide_term("Mão na massa — 1/4: health check 🏥", "terminal", """hx --health python
hx --health go
hx --health typescript
hx --health php
hx --health sql"""),
    slide_term("Mão na massa — 2/4: autocomplete 💬", "insert mode em .py ou .go", """<span class="kw">i</span>          <span class="cm"># insert mode</span>
<span class="cm"># digite: imp</span>
<span class="kw">Ctrl-x</span>     <span class="cm"># autocomplete</span>
<span class="kw">Tab</span>        <span class="cm"># próximo item</span>
<span class="kw">Enter</span>      <span class="cm"># aceitar</span>"""),
    slide_term("Mão na massa — 3/4: goto e hover 🔍", "normal mode", """<span class="kw">gd</span>         <span class="cm"># goto definition</span>
<span class="kw">gr</span>         <span class="cm"># references</span>
<span class="kw">Space k</span>    <span class="cm"># hover / documentação</span>
<span class="kw">]d</span> <span class="kw">[d</span>     <span class="cm"># próximo/anterior diagnóstico</span>"""),
    slide_term("Mão na massa — 4/4: rename e code action 🔧", "normal mode", """<span class="kw">Space r</span>    <span class="cm"># rename symbol</span>
<span class="kw">Space a</span>    <span class="cm"># code action (quick fix)</span>
<span class="kw">Space s</span>    <span class="cm"># symbols do documento</span>
<span class="kw">=</span>          <span class="cm"># formatar seleção</span>
<span class="kw">F</span>          <span class="cm"># formatar arquivo (custom)</span>"""),
    slide_dicas([
        "<b>💡 Comunidade Reddit:</b> use <span class='kbd'>hx --health</span> sempre que LSP falhar — é o primeiro passo.",
        "<b>🔧 :lsp-restart</b> — reinicia language servers sem fechar o editor.",
        "<b>📁 roots:</b> LSP precisa de go.mod, package.json ou pyproject.toml na raiz.",
    ]),
    slide_recap(["LSP nativo no Helix.", "hx --health para diagnosticar.", "Space k/a/r/s para LSP.", "languages.toml define servidores."]),
], "09 — Busca e Substituição")

aula("09", "Busca e Substituição", "#ffa657", [
    slide_titulo(CURSO, "Aula 09 — Busca e Substituição", "Busca local, global, regex e replace."),
    slide_lista("Comandos de busca 🤔", ["/ regex — buscar.", "? — buscar para trás.", "* — palavra sob cursor.", "n N — próximo/anterior.", "Space / — busca global no workspace."]),
    slide_term("Mão na massa — 1/2: busca local 🔎", "hx", """<span class="kw">/func</span>      <span class="cm"># buscar 'func'</span>
<span class="kw">n</span> <span class="kw">N</span>       <span class="cm"># próximo / anterior</span>
<span class="kw">*</span>          <span class="cm"># buscar palavra sob cursor</span>
<span class="kw">:%s/old/new/g</span>  <span class="cm"># substituir tudo</span>"""),
    slide_term("Mão na massa — 2/2: busca global 🌐", "hx projeto/", """<span class="kw">Space /</span>   <span class="cm"># busca em todo workspace</span>
<span class="cm"># digite termo, Enter abre arquivo</span>
<span class="kw">Space '</span>   <span class="cm"># reabre resultados</span>"""),
    slide_recap(["/ e n/N para local.", "Space / para global.", "s/regex + c para multi-replace.", ":%s para substituir no buffer."]),
], "10 — Buffers e Janelas")

aula("10", "Buffers e Janelas", "#ffa657", [
    slide_titulo(CURSO, "Aula 10 — Buffers e Janelas", "Splits, buffers e layouts."),
    slide_lista("Conceitos 🤔", ["Buffer = conteúdo.", "View = exibição.", "Window = área na tela.", "Ctrl-w v/s — splits.", "Space b — buffer picker."]),
    slide_term("Mão na massa — 1/1: splits e buffers 🪟", "hx", """<span class="kw">Ctrl-w v</span>  <span class="cm"># split vertical</span>
<span class="kw">Ctrl-w s</span>  <span class="cm"># split horizontal</span>
<span class="kw">Ctrl-h/j/k/l</span>  <span class="cm"># navegar (custom)</span>
<span class="kw">Space b</span>   <span class="cm"># buffer picker</span>
<span class="kw">gn gp</span>     <span class="cm"># próximo/anterior buffer</span>"""),
    slide_recap(["Ctrl-w para janelas.", "Space b para buffers.", "Ctrl-h/j/k/l navega splits.", "auto-save salva automaticamente."]),
], "11 — Comandos e Pickers")

aula("11", "Comandos e Pickers", "#ffa657", [
    slide_titulo(CURSO, "Aula 11 — Comandos e Pickers", "Command mode, palette e file picker."),
    slide_lista("Command mode (:) 🤔", [":w :wq :q — salvar/sair.", ":config-open — config.", ":format — formatar.", ":lsp-restart — reiniciar LSP.", "Space ? — command palette com fuzzy search."]),
    slide_term("Mão na massa — 1/1: comandos essenciais 📟", "hx", """:config-open
:config-reload
:format
:help
Space ?
<span class="cm"># Tab para autocomplete de comandos</span>"""),
    slide_recap([": para comandos.", "Space ? = palette completa.", "Pickers: f b j s d.", "Tab autocompleta no prompt."]),
], "12 — Configuração Avançada")

aula("12", "Configuração Avançada", "#ffe066", [
    slide_titulo(CURSO, "Aula 12 — Configuração Avançada", "Temas, statusline, monorepo e overrides."),
    slide_lista("O que configurar? 🤔", ["theme, true-color.", "editor.* — auto-save, scrolloff.", "editor.lsp — inlay hints.", "editor.statusline.", ".helix/ por projeto.", "workspace-lsp-roots para monorepo."]),
    slide_term("Mão na massa — 1/2: tema e reload 🎨", "hx", """:theme
<span class="cm"># escolha catppuccin_mocha, onedark, gruvbox...</span>
:config-reload"""),
    slide_term("Mão na massa — 2/2: config por projeto 📁", "terminal", """mkdir -p meu-projeto/.helix
cp exemplos/languages.toml meu-projeto/.helix/
<span class="cm"># overrides mesclados automaticamente</span>"""),
    slide_recap(["Global: ~/.config/helix/.", "Projeto: .helix/ na raiz.", ":theme para trocar tema.", "pkill -USR1 hx recarrega tudo."]),
], "13 — Linguagens de Programação")

aula("13", "Linguagens de Programação", "#ffe066", [
    slide_titulo(CURSO, "Aula 13 — Linguagens de Programação", "Python, Go, Rust, PHP, Web, SQL — LSP por stack."),
    slide_tabela("Stack configurada", ("Linguagem", "LSP"), [
        ("Python", "pyright + ruff"), ("Go", "gopls"), ("Rust", "rust-analyzer"),
        ("PHP", "intelephense"), ("JS/TS/React", "typescript-language-server"),
        ("SQL", "sqls"), ("YAML/TOML", "yaml-language-server + taplo"),
    ]),
    slide_term("Mão na massa — 1/2: testar por linguagem 🧪", "terminal", """hx --health python && hx --health php
hx --health go && hx --health rust
hx --health typescript && hx --health tsx
hx --health sql"""),
    slide_term("Mão na massa — 2/2: abrir projeto real 🚀", "terminal", """cd ~/seu-projeto-go   <span class="cm"># precisa go.mod</span>
hx .
<span class="cm"># teste gd, Space k, =</span>"""),
    slide_recap(["Um LSP (ou mais) por linguagem.", "roots: go.mod, package.json, etc.", "Python: pyright + ruff.", "SQL: configure conexões em languages.toml."]),
], "14 — Macros e Automação")

aula("14", "Macros e Automação", "#ffe066", [
    slide_titulo(CURSO, "Aula 14 — Macros e Automação", "Macros, shell pipe e automação."),
    slide_lista("Ferramentas 🤔", ["Q/q — gravar/reproduzir macro.", "| cmd — pipe shell.", "! cmd — inserir output.", "s/regex + c — multi-replace.", ":sh — shell interativo."]),
    slide_term("Mão na massa — 1/1: shell pipe 🔧", "hx dados.json", """<span class="kw">%</span>          <span class="cm"># selecionar tudo</span>
<span class="kw">|jq .</span>      <span class="cm"># formatar JSON</span>
<span class="kw">|sort</span>      <span class="cm"># ordenar linhas</span>
<span class="kw">|uniq</span>      <span class="cm"># remover duplicatas</span>"""),
    slide_recap(["| para transformar seleção.", "Macros Q/q experimentais.", "s/regex + c = edição em massa.", "Combine com múltiplas seleções."]),
], "15 — Dicas e Workflow")

aula("15", "Dicas e Workflow", "#ff5555", [
    slide_titulo(CURSO, "Aula 15 — Dicas e Workflow", "Fluxo diário, produtividade e troubleshooting."),
    slide_lista("Workflow diário 🎯", [
        "1. <span class='kbd'>tmux new -s dev</span> — sessão persistente;",
        "2. <span class='kbd'>hx .</span> — abrir projeto;",
        "3. <span class='kbd'>Space f</span> — arquivos, <span class='kbd'>gd</span> — navegar;",
        "4. <span class='kbd'>Space d</span> — erros, <span class='kbd'>Space a</span> — fix;",
        "5. <span class='kbd'>Ctrl+b d</span> — detach tmux.",
    ]),
    slide_dicas([
        "<b>💡 Domine Space mode</b> — 80% da produtividade está em Space f/k/a/r.",
        "<b>⌨️ Desabilite setas no insert</b> — force modal editing puro.",
        "<b>🔧 hx --health</b> — primeiro passo quando LSP falha.",
        "<b>📖 Comunidade:</b> r/helixeditor no Reddit — dicas de usuários avançados.",
    ]),
    slide_recap(["tmux + hx = workflow profissional.", "Space mode é o centro.", "Auto-save + auto-format.", "Próximo: cheatsheet e referência."]),
], "16 — Referência Rápida")

aula("16", "Referência Rápida", "#ff5555", [
    slide_titulo(CURSO, "Aula 16 — Referência Rápida", "Cheatsheet de uma página — consulta diária."),
    slide_tabela("Modos e navegação", ("Atalho", "Ação"), [
        ("i a o O", "Insert"), ("x d c y p", "Editar"), ("v", "Select mode"),
        ("gd gr", "LSP goto"), ("Space f/k/a/r", "Pickers/LSP"), ("/ Space /", "Busca"),
    ]),
    slide_tabela("Custom shortcuts", ("Atalho", "Ação"), [
        ("Ctrl+s", "Salvar"), ("Ctrl+h/j/k/l", "Splits"), ("{ }", "Diagnósticos"), ("F", "Formatar"),
    ]),
    slide_lista("Consulta completa 📌", [
        "Markdown: <code class='inline'>manuais/markdown/16-referencia-rapida.md</code>;",
        "Imprima ou mantenha aberto ao lado do monitor;",
        "Próxima aula: terminal e tmux — sessões que sobrevivem a reboot.",
    ]),
    slide_recap(["Cheatsheet mental: modos → Space → LSP.", "Ctrl+s, gd, Space k são os 3 mais usados.", "Manual MD tem tabela completa.", "Aula 17 fecha com tmux."]),
], "17 — Terminal e Sessões Persistentes")

aula("17", "Terminal e Sessões Persistentes", "#00ff9c", [
    slide_titulo(CURSO, "Aula 17 — Terminal e Sessões Persistentes",
                 "Terminal, tmux e restauração após reboot — a peça que faltava."),
    slide_lista("Por que tmux? 🤔", [
        "Helix <b>não tem terminal embutido</b>;",
        "<b>tmux</b> mantém sessões vivas se SSH cair ou terminal fechar;",
        "Melhor que screen para DevOps/backend;",
        "<b>tmux-continuum</b> restaura layout após reboot do PC.",
    ]),
    slide_lista("Abrir terminal 🖥️", [
        "Linux (Pop/Ubuntu): <span class='kbd'>Ctrl+Alt+T</span>;",
        "macOS: Terminal.app, iTerm2 ou <span class='kbd'>Cmd+Space</span> → Terminal;",
        "Recomendado: terminal com true color (WezTerm, Alacritty).",
    ]),
    slide_term("Mão na massa — 1/5: instalar tmux 📦", "Linux", "sudo apt update && sudo apt install -y tmux\ntmux -V"),
    slide_term("Mão na massa — 2/5: instalar tmux (macOS) 🍎", "macOS", "brew install tmux\ntmux -V"),
    slide_term("Mão na massa — 3/5: sessão básica 🔄", "terminal", """tmux new -s dev
hx .
<span class="cm"># Ctrl+b c  — nova janela</span>
<span class="cm"># Ctrl+b %  — split vertical</span>
<span class="cm"># Ctrl+b d  — detach</span>
tmux attach -t dev"""),
    slide_term("Mão na massa — 4/5: plugins resurrect 💾", "terminal", """git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
<span class="cm"># Adicione ao ~/.tmux.conf:</span>
<span class="cm"># set -g @plugin 'tmux-plugins/tmux-resurrect'</span>
<span class="cm"># set -g @plugin 'tmux-plugins/tmux-continuum'</span>
<span class="cm"># set -g @continuum-restore 'on'</span>
<span class="cm"># Dentro do tmux: Ctrl+b I (instalar plugins)</span>"""),
    slide_term("Mão na massa — 5/5: workflow completo 🏆", "terminal", """Ctrl+Alt+T
tmux new -s dev || tmux attach -t dev
cd ~/projects/meu-projeto && hx .
<span class="cm"># Após reboot: tmux (continuum restaura)</span>"""),
    slide_recap([
        "Helix + tmux = setup profissional;",
        "Ctrl+b d detach, tmux attach reconecta;",
        "continuum + resurrect = sobrevive a reboot;",
        "<b>Parabéns!</b> Você completou a trilha Helix Master.",
    ]),
], "🏆 Trilha concluída — continue praticando!")

def main() -> None:
    SAIDA.mkdir(parents=True, exist_ok=True)
    for meta in AULAS:
        html = montar_html(meta)
        dest = SAIDA / meta["arquivo"]
        dest.write_text(html, encoding="utf-8")
        print(f"✓ {dest.name}")
    print(f"\n{len(AULAS)} aulas geradas em {SAIDA}")


if __name__ == "__main__":
    main()
