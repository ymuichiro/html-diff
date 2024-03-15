# HTML-DIFF

このツールは HTML を定期的に取得し、変更があれば差分を diff 形式で表示します。
以下は Azure OpenAI API の deprecated を検出した際の出力例です。

```text
更新を検出しました
  
  Azure OpenAI API プレビューのライフサイクル
  
  
  [アーティクル]
  
  03/08/2024
  
  
  3 人の共同作成者
  
  
  フィードバック
  
  この記事の内容
  
  この記事は、Azure OpenAI API プレビューのサポート ライフサイクルを理解するのに役立ちます。 新しいプレビュー API は、毎月のリリース周期を対象としています。 2024 年 4 月 2 日以降、最新の 3 つのプレビュー API は引き続きサポートされますが、前の API はサポートされなくなります。
+ 
+ Note
+ DALL-E 2 はこの API バージョンでのみ使用できるので、現時点で 2023-06-01-preview API は引き続きサポートされます。 DALL-E 3 は、最新の API リリースでサポートされています。
  
  最新のプレビュー API リリース
  Azure OpenAI API バージョン 2024-03-01-preview が、現時点で最新のプレビュー リリースです。
  このバージョンには、以下のような Azure OpenAI のすべての最新機能のサポートが含まれています。
  
  [埋め込み encoding_format と dimensions パラメーター] [2024-03-01-preview で追加]
  Assistants API。 [2024-02-15-preview で追加]
  DALL-E 3。 [2023-12-01-preview で追加]
  テキスト読み上げ。 [2024-02-15-preview で追加]
  gpt-35-turbo、babbage-002、davinci-002 モデルの微調整。[2023-10-01-preview で追加]
  Whisper。 [2023-09-01-preview で追加]
  関数呼び出し [2023-07-01-preview で追加]
  "独自のデータに基づく" 機能を使用した取得拡張生成。  [2023-06-01-preview で追加]
  
  間もなく廃止
  2024 年 4 月 2 日に、次の API プレビュー リリースは廃止され、API 要求の受け付けは停止されます。
  
  2023-03-15-preview
  2023-07-01-preview
  2023-08-01-preview
  2023-09-01-preview
  2023-10-01-preview
  2023-12-01-preview
  
  サービスが中断しないよう、廃止日より前に最新のプレビュー バージョンを使うように更新する必要があります。
  API バージョンの更新
  環境全体でグローバルに変更を行う前にまず、新しい API バージョンへのアップグレードをテストして、API を更新してもアプリケーションに影響がないのを確認することをお勧めします。
  OpenAI Python クライアント ライブラリまたは REST API を使っている場合は、コードを最新のプレビュー API バージョンに直接更新する必要があります。
  C#、Go、Java、または JavaScript いずれかの Azure OpenAI SDK を使っている場合は、代わりに最新バージョンの SDK に更新する必要があります。 各 SDK リリースは、Azure OpenAI API の特定のバージョンで動作するようにハードコーディングされています。
  次のステップ
  
  Azure OpenAI の詳細についてご覧ください
  Azure OpenAI モデルの操作について理解する
```

## 実行手順

```shell
pip install -r requirements.txt
python -m app.py
```