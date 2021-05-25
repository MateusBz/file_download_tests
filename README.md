# Testing file download
## General Info
This repository contains my test case and ebook download scripts from the site.
The test site and test cases are in English. Technologies: Python, Selenium WebDriver, Pytest.
## Project Structure
- [locators](https://github.com/MateusBz/file_download_tests/tree/main/locators)  - there are locators of web elements
- [pages](https://github.com/MateusBz/file_download_tests/tree/main/pages) - there are sets of method for each test step
- [tests](https://github.com/MateusBz/file_download_tests/tree/main/tests) - there are sets of tests
- [drivers](https://github.com/MateusBz/file_download_tests/tree/main/drivers) - there are drivers for each browser
- [books](https://github.com/MateusBz/file_download_tests/blob/main/books.json) - list of books titles
- [test data](https://github.com/MateusBz/file_download_tests/blob/main/test_data.json) - test dataset 
- [test case](https://github.com/MateusBz/file_download_tests/blob/main/test_case) - test case for these tests  
## Setup
1. Clone repository and go to 'file_download_tests' folder
```
 git clone https://github.com/MateusBz/file_download_tests.git

 cd file_download_tests/
```
2. Install pipenv if you don't have one
```
pip install pipenv
```
3. Install dependencies
```
pipenv install
```
4. Activate a virtual environment
```
pipenv shell
```
5. Run all tests, add the book title in quotes
```
pytest -v --book_title 'The Complete GDPR Guidebook'
```

6. Run selected test, add the book title in quotes
```
pytest -vk test_chrome.py --book_title 'The Complete GDPR Guidebook'
```
or
```
pytest -vk test_ff.py --book_title 'The Complete GDPR Guidebook'
```