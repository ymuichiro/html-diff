import requests
from bs4 import BeautifulSoup

def get_html(url):
  """
  URLからHTMLを取得する関数
  """
  response = requests.get(url)
  response.encoding = response.apparent_encoding # Encoding 判定
  response.raise_for_status()

  soup = BeautifulSoup(response.text, 'html.parser')
  content = soup.find('div', class_='content')

  if content is None:
    raise Exception('Content not found')

  return content.get_text()
