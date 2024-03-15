import re

def pretty_html(html:str) -> str:
  """
  テキストから2つ以上連続する改行とスペースを削除する関数

  Args:
    text: 処理対象のテキスト

  Returns:
    改行とスペースを削除したテキスト
  """
  html = re.sub(r'   +', '  ', html)
  html = re.sub(r'\n\n+', '\n\n', html)
  html = re.sub(r'\t+', '', html)

  return html