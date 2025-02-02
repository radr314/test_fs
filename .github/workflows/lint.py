name: lint

on: 
  push:
    branches: ["*"]

jobs:
    lint:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3

        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: "3.10"
        - name: Install dependencies
            run: |
                python -m pip install --upgrade pip
                pip install flake8
        - name: Lint with flake8
            run: |
                # stop the build if there are Python syntax errors or undefined names
                flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
