from app.lib.get_diff import get_diff
from app.lib.get_html import get_html
from app.lib.pretty_html import pretty_html
from app.lib.config import TARGET_URL
import os

# __init__.py を起点としてプロジェクトルートの1つ上の階層の絶対パスを取得する
prev_html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","prev.html")


def main():

  # 前回のHTMLを取得
  try:
    with open(prev_html_path, "r") as f:
      prev_html = f.read()
  except FileNotFoundError:
    prev_html = ""

  # 現在のHTMLを取得
  html = get_html(TARGET_URL)
  html = pretty_html(html)

  # 差分を取得
  diff, is_updated = get_diff(prev_html, html)

  if is_updated:
    print("更新を検出しました")
    print(diff)
  else:
    print("更新はありません")

  # 現在のHTMLを保存
  with open(prev_html_path, "w") as f:
    f.write(html)

if __name__ == "__main__":
  main()