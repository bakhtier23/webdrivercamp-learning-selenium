
#!/usr/bin/env python3
from selenium import webdriver
from components.filter import LeftFilter

def print_available_attr(obj):
    for attr in dir(obj):
        print(attr)

driver = webdriver.Chrome
left_filter = LeftFilter(driver)

print_available_attr(left_filter)