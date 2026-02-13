import requests
import base64

# --- لیست منابع سنگین (Super Mix) ---
urls = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity",
    "https://raw.githubusercontent.com/AlienLimited/V2rayFree/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/ts-cf/V2ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/lofc-s/V2ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",
    "https://raw.githubusercontent.com/peasoft/Pea2ray/main/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/free-v2ray-config/main/all.txt"
]

output_file = "sub.txt"

def get_configs():
    all_configs = set()
    
    print("Starting Super Collection...")
    for url in urls:
        try:
            print(f"Fetching from: {url}")
            resp = requests.get(url, timeout=15)
            content = resp.text
            
            # اگر محتوا Base64 بود دیکود کن
            if "vmess://" not in content and "vless://" not in content:
                try:
                    content = base64.b64decode(content).decode('utf-8', errors='ignore')
                except: pass

            # استخراج خط به خط
            count = 0
            for line in content.splitlines():
                line = line.strip()
                if line.startswith(("vmess://", "vless://", "trojan://", "ss://", "ssr://")):
                    all_configs.add(line)
                    count += 1
            print(f"  > Found {count} configs.")
                    
        except Exception as e:
            print(f"  > Error: {e}")

    # ذخیره فایل
    final_list = sorted(all_configs)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(final_list))
    
    print(f"\nSUCCESS: Total {len(final_list)} unique configs saved!")

if __name__ == "__main__":
    get_configs()
