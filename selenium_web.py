from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Infow:
    def __init__(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.google.com")
    
    def get_info(self, query):
        # Format and execute the search query
        search_url = "https://www.google.com/search?q=" + query.replace(' ', '+')
        self.driver.get(search_url)
        time.sleep(2)  # Add a wait to let the page load fully
        
        # Print page title or other information
        print(self.driver.title)
    
    def close_driver(self):
        # Close the driver when done
        self.driver.quit()

# Example usage


# Keep the program running so the browser stays open
#try:
#   while True:
#      # Wait here indefinitely until manually closed
#     time.sleep(1)
#except KeyboardInterrupt: #   # Close the browser if the program is interrupted
#  assist.close_driver()
