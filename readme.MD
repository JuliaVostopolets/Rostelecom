#!/usr/bin/python3
-*- encoding=utf8 -*-
conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.
pages/base.py contains PageObject pattern implementation for Python.
pages/elements.py contains helper class to define web elements on web pages.
tests/test_auth_page.py contains several tests for Rostelekom (https://docs.google.com/spreadsheets/d/16HH0QCCBFG_51Ny2F1XUBoYkSeHF70iviwsp27Gh_to/edit#gid=358071179)
pages/auth_page contains Web-elements (locators) for Rostelecom
pages/settings contains valid data for authorisation
pages/pytest.ini contains information about marks for testing
requirements.txt contains info about necessary libraries, that need to be installed


Test_auth_page:
 You can find very simple example of the usage Selenium with PyTest in this file.

 More info about pytest-selenium:
    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html

 How to run:
  1) Download driver for Chrome here:
     https://chromedriver.chromium.org/downloads
  2) Install all requirements:
     pip install -r requirements.txt
  3) Run tests:
     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
   Remote:
  export SELENIUM_HOST=<moon host>
  export SELENIUM_PORT=4444
  pytest -v --driver Remote --capability browserName chrome tests/*

 