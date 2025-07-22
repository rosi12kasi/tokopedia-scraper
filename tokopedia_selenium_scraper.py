from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import pandas as pd

# Setup Chrome
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service("D:\\project\\chromedriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

data = []
keywords = ["iphone"]

# Loop halaman
for halaman in range(1, 6):
    url = f"https://www.tokopedia.com/search?page={halaman}&q=iphone"
    driver.get(url)
    time.sleep(5)

    # Scroll otomatis untuk muat semua produk
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(5):  # scroll 5x per halaman
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)

    produk_elements = driver.find_elements(By.XPATH, '//a[@href and @data-theme="default"]')

    for produk in produk_elements:
        try:
            nama = produk.find_element(By.XPATH, ".//div[contains(@class, 'SzILjt4fxHUFNVT48ZPhHA')]").text
        except:
            nama = "(nama tidak ditemukan)"

        try:
            harga = produk.find_element(By.XPATH, ".//div[contains(@class, 'urMOIDHH7I0Iy1Dv2oFaNw')]").text
        except:
            harga = "(harga tidak ditemukan)"

        try:
            link = produk.get_attribute("href")
        except:
            link = "(link tidak ditemukan)"

        if any(keyword in nama.lower() for keyword in keywords):
            print("Nama:", nama)
            print("Harga:", harga)
            print("Link:", link)
            print("-" * 50)
            data.append([nama, harga, link])

produk_dicts = [{"nama": row[0], "harga": row[1], "link": row[2]} for row in data]
with open("produk_tokopedia.json", "w", encoding="utf-8") as f:
    json.dump(produk_dicts, f, ensure_ascii=False, indent=4)
    
# Simpan ke Excel
if data:
    df = pd.DataFrame(data, columns=["Nama Produk", "Harga", "Link"])
    df.to_excel("hasil_scraping_tokopedia.xlsx", index=False)
    print("✅ Data berhasil disimpan ke hasil_scraping_tokopedia.xlsx")
else:
    print("❌ Tidak ada data yang berhasil diambil.")

driver.quit()
