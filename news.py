from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NewsSearch:
    def __init__(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://news.google.com")

    def search_news(self, query):
        # Wait for the page to load
        time.sleep(2)

        # Locate the search bar, enter the query, and execute the search
        search_box = self.driver.find_element(By.NAME, "q")  # Google News search box uses 'q' as the name
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(3)

        # Print the title of the page to confirm search execution
        print("Page title after search:", self.driver.title)

    def keep_open(self):
        try:
            # Keep the program running indefinitely until manually closed
            print("Browser is open. Press Ctrl+C to exit.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nManual close initiated. Exiting program.")

# Example usage:
#news = NewsSearch()
#news.search_news("AI technology advancements")  # Replace with any news topic
#news.keep_open()  # Keeps the browser open until manually interrupted

