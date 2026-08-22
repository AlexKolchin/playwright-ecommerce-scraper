.PHONY: help setup run test clean

help: ## Show available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$'$(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1,$$2}'

setup: ## Install dependencies and Playwright browsers
	python3 -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt
	./.venv/bin/playwright install chromium

run: ## Execute scraper main script
	python main.py

test: ## Run pytest test suite
	pytest -v

clean: ## Remove generated logs, cache and output data
	rm -rf __pycache__ .pytest_cache logs/*.log data/*.json
