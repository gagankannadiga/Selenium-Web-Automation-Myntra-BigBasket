  # 🧪 Selenium Automation Testing
  
  This repository contains Selenium automation test scripts written in Python to test **Myntra** and **BigBasket** websites.  
  
  ## 📌 Features
  - Automates browser actions using **Selenium WebDriver**
  - Uses **ChromeDriver** via `webdriver_manager`
  - Includes test cases such as:
    - Opening and navigating web pages
    - Maximizing/minimizing windows
    - Searching for products
    - Scrolling
    - Navigating categories
    - Adding products to cart
    - Simulating login/signup flows
  - Organized with Python **unittest framework** (for BigBasket tests)
  
  ---
  
  ## 📂 Project Structure
  selenium-project/
  │── myntra_test.py # Myntra website automation
  │── bigbasket_test.py # BigBasket website automation (unittest)
  │── requirements.txt # Required dependencies
  │── README.md # Documentation
  
  python -m venv venv
  source venv/bin/activate   # macOS/Linux
  venv\Scripts\activate      # Windows
  
  pip install -r requirements.txt
  
  Requirements
  
  Add this to requirements.txt:
  
  selenium
  webdriver-manager
  unittest2
  
  Run Myntra test:
  python myntra_test.py
  
  Run BigBasket tests:
  python -m unittest bigbasket_test.py
