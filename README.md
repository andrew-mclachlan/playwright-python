# playwright-python

PyTest example using Playwright to test a website

## Prerequisites

- Python 3.x must be installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- Node.js 20.x or greater must be installed on your machine. You can use the instructions found on <https://nodejs.org/en/download/package-manager> to install Node.js.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/andrew-mclachlan/playwright-python.git
   cd playwright-python
   ```

2. Create a virtual environment:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required modules:

   ```sh
   pip install -r requirements.txt
   playwright install
   ```

## Build and run the Web App

1. Install dependencies

```sh
   cd nextjs-blog
   npm install
```

1. Launch the Web App

```sh
   npm run dev
```

## Running Tests

To run the tests with `pytest`, open a terminal and use the following command:

```sh
pytest
```

## Debugging Tests

Debugging Tests with VS Code
Open the project in Visual Studio Code.
Ensure you have the Python extension installed.
Set breakpoints in your test code.
Go to the Run and Debug view (Ctrl+Shift+D) and select "Python: Run Pytest".
Click the green play button to start debugging.

## Debugging Tests with Playwright UI

```sh
PWDEBUG=1 pytest -s e2e-tests/test_example.py
```
