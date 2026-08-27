# Task 6.2: Import required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Task 6.2: Load the OWASP Top 10 page

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://owasp.org/Top10/2021/")

# Task 6.3: Find the OWASP Top 10 vulnerabilities

vulnerabilities = driver.find_elements(
    By.XPATH,
    "/html/body/div[3]/main/div/div[3]/article/ol/li/a"
)

print("Number of vulnerabilities:", len(vulnerabilities))

# Task 6.3: Create a list for the vulnerability data

results = []
for vulnerability in vulnerabilities:
        title = vulnerability.text
        href = vulnerability.get_attribute("href")
        vulnerability_data = {
        "Title": title,
        "href": href
    }
        results.append(vulnerability_data)


print(results)

# Task 6.4: Write results to CSV

df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)

input("Press Enter to close the browser...")