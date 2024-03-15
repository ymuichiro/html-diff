from app.lib.get_html import get_html
from app.lib.pretty_html import pretty_html
from app.lib.config import TARGET_URL
import os

# __init__.py を起点としてプロジェクトルートの1つ上の階層の絶対パスを取得する
prev_html = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","prev.html")

def init():

  # prev.html が存在するか確認する
  if os.path.exists(prev_html):
    return
  
  # 現在のHTMLを取得
  html = get_html(TARGET_URL)
  html = pretty_html(html)

  # 現在のHTMLを保存
  with open(prev_html, "w") as f:
    f.write(html)

if __name__ == "app":
  init()