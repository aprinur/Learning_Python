import requests
from bs4 import BeautifulSoup
import csv

key = 'ssd'
url = 'https://shopee.co.id/search?keyword={}&page='.format(key)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 Edg/113.0.1774.42'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('div', 'VTjd7p whIxGK')
for it in items:
    nama = it.find('div', 'ie3A+n bM+7UW Cve6sh')
    print(nama)

 ###  https://youtu.be/YIiYeyfo7MM?t=757

