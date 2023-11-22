from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_basics.components.base import Base
from selenium_basics.components.base import assert_text
from selenium_basics.components.filter import LeftFilter

# Initialize browser and variables
driver = webdriver.Chrome()
main_page_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(main_page_url)
search_param1 = "Rolex"
search_param2 = "Casio"
page = Base(driver)
panel = LeftFilter(driver)

# Function to process search options
def process_search_option(search_param):
    # Select search option
    panel.select_option(search_param)

    # Get and save base page data
    title_base = []
    price_base = []
    for i in range(2):
        title_path = f"//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view][{i+1}]//span[@role='heading']"
        price_path = f"//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view][{i+1}]//span[@class='s-item__price']"
        title_base.append(page.get_text(title_path))
        price_base.append(page.get_text(price_path))

    # Check item titles and prices
    for i in range(2):
        assert_text(search_param.lower(), title_base[i].lower(), "Option not in title")
        page.click((By.XPATH, title_path))
        driver.switch_to.window(driver.window_handles[i + 1])

        title_item = page.get_text("//h1[@class='x-item-title__mainTitle']/span")
        price_item = page.get_text("//div[@class='x-price-primary']/span")

        assert_text(title_base[i], title_item, "Title mismatch")
        assert_text(price_base[i], price_item, "Price mismatch")

        driver.switch_to.window(driver.window_handles[0])
        page.click((By.XPATH, title_path))

    # Unselect search option
    panel.select_option(search_param)

# Process search options
process_search_option(search_param1)
process_search_option(search_param2)

# Close browser
driver.quit()