from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeInfo:
    def __init__(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.youtube.com")

    def search_video(self, query):
        # Wait for the page to load
        time.sleep(2)

        # Locate the search bar, enter the query, and execute the search
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(3)

        # Optionally, print the title of the first video in the search results
        first_video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        print("First video title:", first_video.get_attribute("title"))

    def keep_open(self):
        try:
            # Keep the program running indefinitely until manually closed
            print("Browser is open. Press Ctrl+C to exit.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nManual close initiated. Exiting program.")

# Example usage:
#yt = YouTubeInfo()
#yt.search_video("Python programming tutorial")
#yt.keep_open()  # Keeps the browser open until manually interrupted
