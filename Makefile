# Makefile for setting up and running the woltest-automation-framework

.PHONY: setup test clean allure-report

setup:
	pip install -e .
	pip install pytest playwright pytest-playwright allure-pytest
	playwright install

test:
	pytest tests/ -v --alluredir=./allure-results

clean:
	rm -rf ./allure-results
	rm -rf ./logs
	find . -type d -name "__pycache__" -exec rm -rf {} +

allure-report:
	allure generate ./allure-results -o ./allure-report --clean
	allure open ./allure-report
