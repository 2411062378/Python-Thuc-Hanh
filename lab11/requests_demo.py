import requests

print("=== 5.1: GỌI GITHUB API ===")
url_github = "https://api.github.com/repos/python/cpython"
res_gh = requests.get(url_github)

if res_gh.status_code == 200:
    data_gh = res_gh.json()
    print("Tên repository:", data_gh["full_name"])
    print("Số lượt gắn sao (stars):", data_gh["stargazers_count"])
    print("Ngôn ngữ chính:", data_gh["language"])
else:
    print("Gọi API thất bại, mã lỗi:", res_gh.status_code)

print("\n=== 5.2: TỶ GIÁ NGOẠI TỆ (USD -> VND) ===")
url_rate = "https://open.er-api.com/v6/latest/USD"
res_rate = requests.get(url_rate)

if res_rate.status_code == 200:
    data_rate = res_rate.json()
    ty_gia = data_rate["rates"]["VND"]
    print(f"1 USD = {ty_gia:,.0f} VND")
else:
    print("Không lấy được tỷ giá, mã lỗi:", res_rate.status_code)