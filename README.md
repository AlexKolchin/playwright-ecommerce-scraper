# Playwright Async E-Commerce Scraper

Production-ready asynchronous web scraper for e-commerce catalog data built with Python, Playwright, and Pydantic. Designed with scalable SDET standards, comprehensive logging, typed data validation, and unit/integration testing with network mocking.

---

## Features

- Asynchronous Architecture: High-performance data extraction built on asyncio and playwright.async_api.
- Data Validation: Strict schema enforcement and type checking via Pydantic v2.
- Pagination Handling: Dynamic catalog traversal until end-of-catalog or target depth.
- Robust Logging: Dual-destination formatted output (Console & File loggers) using the Singleton pattern.
- Network Mocking: Fully isolated unit and integration tests using mocked Playwright network routes without external dependency.
- Developer Experience (DX): Unified command orchestration via Makefile.
- Containerization: Fully dockerized setup using official Microsoft Playwright images.

---

## Project Structure

- config/ # Logging configuration (Singleton pattern)
- data/ # Scraped JSON data storage (gitignored)
- logs/ # Application execution logs (gitignored)
- models/ # Pydantic data models & validation schemas
- scrapers/ # Base & concrete scraper implementations
- tests/ # Unit & network-mocked integration tests
- utils/ # File management & helper functions
- Dockerfile # Container build specification
- Makefile # CLI automation commands
- main.py # Application entry point
- pytest.ini # Pytest execution settings
- requirements.txt # Locked dependencies

---

## Prerequisites

- Python: 3.11+ (or WSL Ubuntu environment)
- Docker: (Optional, for containerized execution)
- Make: (Optional, for running automated CLI shortcuts)

---

## Quick Start & Local Setup

### 1. Repository Setup & Environment Installation

Clone the repository and set up your virtual environment along with Playwright dependencies:

Using Makefile (Recommended):
  make setup

Or manually:
  python3 -m venv venv_playwright
  source venv_playwright/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  playwright install-deps
  playwright install chromium

### 2. Execution

Run the catalog scraper locally:

Using Makefile:
  make run

Or manually:
  python main.py

Scraped results will be validated and exported to data/products.json.

---

## Testing & Quality Assurance

The test suite covers Pydantic data schema validations as well as catalog scraping logic. Network requests are intercepted using Playwright route mocking to guarantee fast, deterministic, and isolated execution.

Run the test suite:

Using Makefile:
  make test

Or manually:
  pytest -v

---

## Running with Docker

You can build and run the scraper inside an isolated Docker container without configuring local Python or browser binaries:

Build the Image:
  docker build -t playwright-scraper .

Run the Container:
To extract the scraped products.json file back to your host machine, mount the data directory as a volume:
  docker run --rm -v $(pwd)/data:/app/data playwright-scraper

---

## Utility Commands (Makefile)

If you have make installed, you can use these shortcuts:

- make help — Show all available project CLI commands.
- make setup — Install all Python packages and Playwright browser binaries.
- make run — Execute the main scraping script.
- make test — Execute the full test suite via Pytest.
- make clean — Remove generated cache, log files, and scraped JSON data.
