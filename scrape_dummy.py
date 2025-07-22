import pandas as pd

produk_iphone = [
    {
        "Nama Produk": "iPhone 13 128GB",
        "Harga": "Rp12.499.000",
        "Toko": "iBox Official Store",
        "Link": "https://www.tokopedia.com/ibox/iphone-13"
    },
    {
        "Nama Produk": "iPhone 11 64GB",
        "Harga": "Rp8.299.000",
        "Toko": "Digimap Official",
        "Link": "https://www.tokopedia.com/digimap/iphone-11"
    },
    {
        "Nama Produk": "iPhone 14 Pro Max 256GB",
        "Harga": "Rp20.999.000",
        "Toko": "Apple Premium Reseller",
        "Link": "https://www.tokopedia.com/apple-premium/iphone-14-pro-max"
    },
    {
        "Nama Produk": "iPhone SE 2022 64GB",
        "Harga": "Rp6.799.000",
        "Toko": "iBox Official Store",
        "Link": "https://www.tokopedia.com/ibox/iphone-se-2022"
    }
]

df = pd.DataFrame(produk_iphone)
df.to_excel("hasil_scraper_iphone_dummy.xlsx", index=False)
print("Berhasil membuat file excel: hasil_scraper_iphone_dummy.xlsx")