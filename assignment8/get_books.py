# Task 3.1: Import required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import json

# Task 3.2: Load the Durham Library search pages

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(url)

# Task 3.3: Find all search result li elements
books = driver.find_elements(
    By.CSS_SELECTOR,
    "li.row.cp-search-result-item"
)
print("Number of books:", len(books))

# Task 3.4: Create an empty results list
results = []

# Task 3.5: Extract data from each search result

for book in books:
    title = book.find_element(
    By.CSS_SELECTOR,
    "span.title-content"
).text
    
    authors = book.find_elements(
        By.CSS_SELECTOR,
        "a.author-link"
    )
    author_names = [author.text for author in authors]
    author_text = "; ".join(author_names)

    format_year_container = book.find_element(
    By.CSS_SELECTOR,
    "div.cp-format-info"
)
    format_year = format_year_container.find_element(
    By.CSS_SELECTOR,
    "span.display-info-primary"
).text
    book_data = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }
    results.append(book_data)

# Task 3.6: Create and print the DataFrame

df = pd.DataFrame(results)

print(df)
print(title)
print(author_text)
print(format_year)



# Task 4.1: Write DataFrame to CSV
df.to_csv("get_books.csv",index=False)

# Task 4.2: Write results to JSON

with open("get_books.json", "w") as file:
    json.dump(results, file, indent=4)

input("Press Enter to close the browser...")
