import requests
import re
import base64

# --- لیست منابع جدید و قوی ---
urls = [
    "https://raw.githubusercontent.com/AlienLimited/V2rayFree/main/All_Configs_Sub.txt", # جایگزین شد
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity",
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt"
]

output_file = "sub.txt"

def get_configs():
    all_configs = set() # حذف تکراری‌ها
    
    for url in urls:
        try:
            print(f"Downloading: {url}")
            resp = requests.get(url, timeout=10)
            content = resp.text
            
            # اگر محتوا کد شده بود (Base64)، بازش کن
            if "vmess://" not in content and "vless://" not in content:
                try:
                    content = base64.b64decode(content).decode('utf-8', errors='ignore')
                except: pass

            # پیدا کردن خط به خط کانفیگ‌ها
            for line in content.splitlines():
                if line.startswith(("vmess://", "vless://", "trojan://", "ss://", "ssr://")):
                    all_configs.add(line.strip())
                    
        except Exception as e:
            print(f"Error: {e}")

    # ذخیره در فایل
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(all_configs)))
    print(f"Saved {len(all_configs)} configs.")

if __name__ == "__main__":
    get_configs()
