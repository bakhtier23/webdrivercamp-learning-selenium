from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_basics.components.base import Base
from selenium_basics.components.base import assert_text
from selenium_basics.components.filter import LeftFilter

def test_search_and_verify(driver, search_param, first_two=True):
    title_base, price_base, title_item, price_item = [], [], [], []
    panel.select_option(search_param)

    # Define a range for looping
    index_range = range(0, 2) if first_two else range(-2, 0)

    for i in index_range:
        # Adjust locators based on whether we are getting the first or last two items
        offset = f"[{i + 1}]" if first_two else f"[last()-{-i}]"

        title_path = f"//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view]{offset}//span[@role='heading']"
        price_path = f"//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view]{offset}//span[@class='s-item__price']"

        # Store and compare titles and prices from main and item pages
        title_base.append(page.get_text(title_path))
        price_base.append(page.get_text(price_path))

        if first_two:
            page.click((By.XPATH, title_path))
            driver.switch_to.window(driver.window_handles[i + 1])

            # Item page locators
            title_item.append(page.get_text("//h1[@class='x-item-title__mainTitle']/span"))
            price_item.append(page.get_text("//div[@class='x-price-primary']/span"))

            driver.switch_to.window(driver.window_handles[0])

            # Assertions
            assert_text(search_param.lower(), title_base[i].lower())
            assert_text(title_base[i], title_item[i])
            assert_text(price_base[i], price_item[i])
        else:
            # For last two elements, only verify the title contains search_param2
            assert_text(search_param, title_base[i].lower())

driver = webdriver.Chrome()
main_page_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(main_page_url)

page = Base(driver)
panel = LeftFilter(driver)

# Test 1: Rolex title and price verification
test_search_and_verify(driver, "Rolex", first_two=True)

# Uncheck Rolex option
panel.select_option("Rolex", negate=True)

# Test 2: Casio title verification
test_search_and_verify(driver, "Casio", first_two=False)

driver.quit()