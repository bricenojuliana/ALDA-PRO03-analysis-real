#!/bin/bash

echo "🔍 Running tests with coverage..."

PYTHONPATH=$(pwd) pytest --cov=src --cov-report=term-missing --cov-report=html

echo "📁 HTML report generated at htmlcov/index.html"