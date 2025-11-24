Playwright + Pytest + Page Object Model for SauceDemo








🚀 Overview

This project is a Playwright UI automation framework in Python designed to test the SauceDemo application using:

Playwright (Python)

Pytest

Page Object Model (POM)

Pytest fixtures

Allure reporting

GitHub Actions CI pipeline

It demonstrates a clean, scalable, interview-ready automation architecture suitable for professional SDET portfolios.

📁 Project Structure
playwright-saucedemo-python/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_overview_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_checkout_flow.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

🧪 Features
✔ Playwright Python

Browser automation using Chromium, Firefox, and WebKit

Native trace viewer

Headless/headed mode

Slow-motion runs (--slowmo)

✔ Pytest Test Framework

Fixtures (page, login_page)

Test parametrization

Test grouping and tagging

✔ Page Object Model (POM)

Each page is represented as a class

Clean separation of locators, actions, and assertions

✔ Full E2E Flow Included

Login

Add item to cart

Checkout

Validate order success

✔ Allure Reporting

Beautiful report UI + dashboards

Auto-attach traces, screenshots, steps

GitHub Actions-compatible

🏃‍♂️ Getting Started
1️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Install Playwright browsers
playwright install

▶ Running Tests
Headed + slow motion (recommended)
pytest --headed --slowmo 500

Normal run
pytest

📊 Allure Reporting
Install Allure (Windows)

Download Allure from:
https://github.com/allure-framework/allure2/releases

Unzip and add allure/bin to your system PATH.

Verify:

allure --version

Run tests with Allure
pytest --alluredir=allure-results

Generate report locally
allure serve allure-results

🔁 GitHub Actions CI (Playwright + Pytest + Allure)

This project includes a ready-to-run GitHub Actions workflow that:

Installs Python

Installs Playwright browsers

Runs tests

Uploads Allure results as an artifact

Runs tests on every push + PR

🧬 Roadmap / Future Enhancements

Add reporting screenshots & videos

Add Docker support

Extend POM to cover all SauceDemo pages

Add API + UI combo tests

📜 License

This project is licensed under the MIT License.
