from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')
print(browser.title)
assert 'Welcome to Django' in browser.title
