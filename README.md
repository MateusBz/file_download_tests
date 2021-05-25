## Setup
1. Clone repository and go to 'selenium_web_testing' folder
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
pytest -v test_chrome.py --book_title 'The Complete GDPR Guidebook'
```
or
```
pytest -v test_ff.py --book_title 'The Complete GDPR Guidebook'
```