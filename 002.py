from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)

driver.get("https://www.google.com/search?q=selenium+prettyprint+source")
anchors = driver.find_elements(By.TAG_NAME, "a")
for anchor in anchors:
    url = anchor.get_attribute("href")
    if url:
        parsed_url = urlparse(url)
        if "google" not in parsed_url.netloc:
            root_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            print(root_url)


input("Press any key to exit...")


driver.quit()
