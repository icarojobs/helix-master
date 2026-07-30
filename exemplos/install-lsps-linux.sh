#!/usr/bin/env bash
# Instala language servers para Helix — Linux (Debian/Ubuntu/Pop!_OS)
# Uso: bash exemplos/install-lsps-linux.sh
set -euo pipefail

echo "==> Verificando pré-requisitos..."
command -v python3 >/dev/null || { echo "Instale: sudo apt install python3 python3-pip"; exit 1; }
command -v npm    >/dev/null || { echo "Instale Node.js: https://nodejs.org ou nvm"; exit 1; }
command -v go     >/dev/null || { echo "Instale Go: https://go.dev/dl/"; exit 1; }
command -v cargo  >/dev/null || { echo "Instale Rust: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"; exit 1; }

PREFIX="${HOME}/.local"
export PATH="${PREFIX}/bin:${HOME}/.cargo/bin:${HOME}/go/bin:${PATH}"

echo "==> Python (pyright + ruff)..."
pip3 install --user ruff pyright

echo "==> Node.js (TS, PHP, Web, YAML)..."
npm install -g --prefix "${PREFIX}" \
  typescript \
  typescript-language-server \
  vscode-langservers-extracted \
  intelephense \
  yaml-language-server

echo "==> Go (gopls + sqls)..."
go install golang.org/x/tools/gopls@latest
go install github.com/sqls-server/sqls@latest

echo "==> Rust (rust-analyzer + taplo)..."
rustup component add rust-analyzer 2>/dev/null || true
cargo install taplo-cli --locked

echo "==> Markdown (marksman)..."
MARKSMAN_VER="2026-02-08"
ARCH="$(uname -m)"
case "${ARCH}" in
  x86_64)  MARKSMAN_ARCH="x64" ;;
  aarch64) MARKSMAN_ARCH="arm64" ;;
  *) echo "Arquitetura não suportada: ${ARCH}"; exit 1 ;;
esac
curl -fsSL "https://github.com/artempyanykh/marksman/releases/download/${MARKSMAN_VER}/marksman-linux-${MARKSMAN_ARCH}" \
  -o "${PREFIX}/bin/marksman"
chmod +x "${PREFIX}/bin/marksman"

echo "==> Configurando PATH no ~/.bashrc (se ainda não existir)..."
for line in \
  'export PATH="$HOME/.local/bin:$PATH"' \
  'export PATH="$PATH:/usr/local/go/bin:$HOME/go/bin"' \
  '. "$HOME/.cargo/env"'; do
  grep -qF "${line}" "${HOME}/.bashrc" 2>/dev/null || echo "${line}" >> "${HOME}/.bashrc"
done

echo ""
echo "✓ Instalação concluída. Reinicie o terminal e execute:"
echo "  hx --health python"
echo "  hx --health go"
echo "  hx --health typescript"
