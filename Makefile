# Makefile for MCP Sample Binary Application

.PHONY: help install build test clean run-example

help: ## Show this help message
	@echo "MCP Sample Binary Application"
	@echo "============================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install the application in development mode
	pip install -e .

build: ## Build standalone binary executable
	python build_binary.py

test: ## Run basic tests
	@echo "Running basic functionality tests..."
	@python main.py --text "Hello World" --encode
	@echo "✅ Encode test passed"
	@python main.py --text "01001000 01100101 01101100 01101100 01101111" --decode
	@echo "✅ Decode test passed"

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.spec __pycache__/ *.pyc *.egg-info/

run-example: ## Run example commands
	@echo "Example 1: Encode text to binary"
	python main.py --text "Hello MCP!" --encode
	@echo ""
	@echo "Example 2: Decode binary to text"
	python main.py --text "01001000 01100101 01101100 01101100 01101111" --decode
	@echo ""
	@echo "Example 3: Show help"
	python main.py --help

dev-install: ## Install development dependencies
	pip install pyinstaller pytest black flake8 mypy

format: ## Format code with black
	black *.py

lint: ## Lint code with flake8
	flake8 *.py

type-check: ## Type check with mypy
	mypy *.py
