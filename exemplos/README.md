# Arquivos de exemplo — Helix Master

Copie estes arquivos para configurar o Helix com atalhos e LSPs completos.

## Uso

```bash
# 1. Instalar language servers
bash install-lsps-linux.sh    # Debian/Ubuntu/Pop!_OS
bash install-lsps-macos.sh  # macOS (requer Homebrew)

# 2. Copiar configs
mkdir -p ~/.config/helix
cp config.toml    ~/.config/helix/
cp languages.toml ~/.config/helix/

# 3. Verificar
hx --health python
hx --health go
hx --health typescript
```

## Arquivos

| Arquivo | Destino | Conteúdo |
|---------|---------|----------|
| `config.toml` | `~/.config/helix/config.toml` | Tema, editor, atalhos personalizados |
| `languages.toml` | `~/.config/helix/languages.toml` | LSPs para Python, PHP, Go, Rust, Web, SQL |
| `install-lsps-linux.sh` | — | Instala todos os LSPs no Linux |
| `install-lsps-macos.sh` | — | Instala todos os LSPs no macOS |

Documentação completa: [`manuais/02-instalacao-e-configuracao.md`](../manuais/02-instalacao-e-configuracao.md)
