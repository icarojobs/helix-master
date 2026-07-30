#!/usr/bin/env bash
# Instala language servers para Helix — macOS
# Uso: bash exemplos/install-lsps-macos.sh
# Pré-requisito: Homebrew (https://brew.sh)
set -euo pipefail

echo "==> Verificando Homebrew..."
command -v brew >/dev/null || { echo "Instale Homebrew: https://brew.sh"; exit 1; }

echo "==> Instalando ferramentas base via Homebrew..."
brew install node go python@3 rust

echo "==> Python (pyright + ruff)..."
pip3 install --user ruff pyright

echo "==> Node.js (TS, PHP, Web, YAML)..."
npm install -g \
  typescript \
  typescript-language-server \
  vscode-langservers-extracted \
  intelephense \
  yaml-language-server

echo "==> Go (gopls + sqls)..."
go install golang.org/x/tools/gopls@latest
go install github.com/sqls-server/sqls@latest

echo "==> Rust (rust-analyzer + taplo)..."
rustup component add rust-analyzer 2>/dev/null || brew install rust-analyzer
cargo install taplo-cli --locked

echo "==> Markdown (marksman)..."
brew install marksman 2>/dev/null || {
  MARKSMAN_VER="2026-02-08"
  ARCH="$(uname -m)"
  case "${ARCH}" in
    arm64)  MARKSMAN_ARCH="arm64" ;;
    x86_64) MARKSMAN_ARCH="x64" ;;
    *) echo "Arquitetura não suportada: ${ARCH}"; exit 1 ;;
  esac
  curl -fsSL "https://github.com/artempyanykh/marksman/releases/download/${MARKSMAN_VER}/marksman-macos-${MARKSMAN_ARCH}" \
    -o "${HOME}/.local/bin/marksman"
  chmod +x "${HOME}/.local/bin/marksman"
}

echo "==> Configurando PATH no ~/.zshrc (macOS padrão)..."
SHELL_RC="${HOME}/.zshrc"
for line in \
  'export PATH="$HOME/.local/bin:$PATH"' \
  'export PATH="$PATH:$HOME/go/bin"' \
  'export PATH="$(brew --prefix)/opt/python@3/libexec/bin:$PATH"' \
  '. "$HOME/.cargo/env"'; do
  grep -qF "${line}" "${SHELL_RC}" 2>/dev/null || echo "${line}" >> "${SHELL_RC}"
done

echo ""
echo "✓ Instalação concluída. Reinicie o terminal e execute:"
echo "  hx --health python"
echo "  hx --health go"
echo "  hx --health typescript"
