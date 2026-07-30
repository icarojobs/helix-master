.PHONY: iterativo help

help:
	@echo "Alvos:"
	@echo "  make iterativo  — regenera slides HTML em manuais/iterativo/"

iterativo:
	python3 scripts/gerar_iterativo.py
