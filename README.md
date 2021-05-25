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
### Book Titles
- 'Data Ethics & Customer Preference Management'
- 'The Ultimate marketer's guide to Customer Data Platforms'
- 'AI Product Recommendation Engines: SALESmanago vs Benchmarks'
- 'Cookbook of marketing automation in eCommerce'
- 'Kamasutra of eMail Marketing Deliverability'
- 'The Complete Guide to Marketing Automation in Ecommerce'
- 'Online Consumer Trends 2020'
- 'How Marketing Automation is changed by AI and Data Science'
- 'How Live Chat is redefined by AI, Machine Learning, Deep Learning and Bots'
- '10 success stories of Europes biggest brands implementing marketing automation'
- 'Complete Marketing Automation Product Profile'
- '2018 European Digital Marketing Survey'
- 'The Complete GDPR Guidebook'
- 'Unique Selling Proposition Ebook'
- '12 ideas for Omnichannel Marketing'
- 'Marketing Automation in Ecommerce for beginners'
- 'Social Media Guide for Ecommerce'
- '5 Ecommerce problems and how to solve them using Marketing Automation Platform Part 2'
- 'The Great Book of Generating Leads for Ecommerce'
- 'The Ultimate Guide to PUSH Notifications'
- 'Ebook - Customer Value Marketing'
- 'Digital Marketer's Pocket Dictionary'
- 'The Crisis of Inbound and the new Push Marketing'
- 'Winning the Zero Moment of Truth with Marketing Automation'
- 'Switch from Email Marketing to Marketing Automation'
- 'Turn Visitors into Loyal Customers'
- 'Mobile Marketing Automation'
- 'Amazing Shopping Experience'
- 'Buyer Persona in Marketing Automation'
- 'Internet of Things'
- 'The Ultimate Guide to Marketing Automation'
- 'Engagement Marketing'
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