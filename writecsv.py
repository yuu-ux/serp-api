import csv
import json

# JSONファイルから検索結果を読み込む
with open('search_results.json', 'r') as f:
    search_results = json.load(f)

# URLを抽出
urls = [result.get('link') for result in search_results if 'link' in result]

# CSVファイルにURLを保存
with open('search_results_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL'])
    for url in urls:
        writer.writerow([url])

print(f"Total URLs saved: {len(urls)}")

