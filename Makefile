# Makefile for setting up and running the woltest-automation-framework

setup:
	@echo "Creating virtual environment..."
	python -m venv venv
	@echo "Activating virtual environment..."
	source venv/bin/activate
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "Installing Playwright browsers..."
	python -m playwright install

test:
	@echo "Running tests with Pytest..."
	pytest

allure-report:
	@echo "Generating Allure report..."
	allure serve /tmp/my_allure_results

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache

.PHONY: setup test allure-report clean
