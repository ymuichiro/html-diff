
from difflib import ndiff


def get_diff(html1:str, html2:str) -> tuple[str, bool]:
  """
  2つのHTMLの差分を取得する関数
  """

  result = list(ndiff(html1.splitlines(), html2.splitlines()))
  result_text = "\n".join(result)

  is_update = False
  for r in result:
    if r[0:1] in ['+', '-']:
        is_update = True

  # print(result_text)

  return result_text, is_update