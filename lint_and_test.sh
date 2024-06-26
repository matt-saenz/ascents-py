#!/usr/bin/env bash
set -e

black --check --diff src tests
isort --check --diff --only-sections --profile black src tests
mypy --strict src tests
flake8 --extend-ignore E501 src tests
pip install --quiet .
pytest --quiet tests
