import requests
import os

api_key = os.getenv('API_KEY')
query = os.getenv('QUERY')
location = 'Tokyo, Japan'
hl = 'ja'
gl = 'jp'
total_pages = 29 #何ページ取得するか
results_per_page = 10 #1ページの中でいくつURLを取得するか

all_results = []

for page in range(total_pages):
    start = page * results_per_page
    params = {
        'api_key': api_key,
        'engine': 'google',
        'q': query,
        'location': location,
        'hl': hl,
        'gl': gl,
        'start': start
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        all_results.extend(search_results.get('organic_results', []))
    else:
        print(f"Failed to fetch page {page + 1}: {response.status_code}")

# all_results にすべての検索結果が格納されます。
print(f"Total results fetched: {len(all_results)}")

# 結果をファイルに保存する場合:
import json
with open('search_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)

