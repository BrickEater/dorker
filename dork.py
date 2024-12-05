from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import re

# Init----------------------------------------------------------------
options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(2)

# Variables-----------------------------------------------------------
subdomains = set()
excluded_subdomains = set()
previous_subdomains = set()
primary_domain = "site%3Amozilla.com"
subdomains_found = True
token = "+-"
exclude = ""
query = f"https://www.google.com/search?q={primary_domain}{exclude}"


# Main Loop-----------------------------------------------------------


while subdomains_found:
    print(f"Query: {query}")
    driver.get(query)
    cite_tags = driver.find_elements(By.TAG_NAME, "cite")

    if cite_tags:
        for cite in cite_tags:
            cite_content = cite.text
            parsed_cite = urlparse(cite_content)
            cite_scheme = re.sub(r"[^ -~]", "", parsed_cite.scheme)
            cite_netloc = (re.sub(r"[^ -~]", "", parsed_cite.netloc)).split(" ")[0]

            if cite_scheme and cite_netloc:
                joined_url = f"{cite_scheme}://{cite_netloc}"
                parts = cite_netloc.split(".")
                if len(parts) > 2:
                    excluded_subdomains.add(parts[0])
                subdomains.add(joined_url)

    else:
        subdomains_found = False
        break

    for domain in subdomains:
        print(domain)

    # for domain in excluded_subdomains:
    #     print(domain)

    if excluded_subdomains:
        exclude = token + token.join(excluded_subdomains)
        query = f"https://www.google.com/search?q={primary_domain}{exclude}"

    if subdomains == previous_subdomains:
        break

    previous_subdomains = subdomains.copy()


input("Press any key to exit...")


driver.quit()
