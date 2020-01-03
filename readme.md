# 研修用プログラム

## Webスクレイピングして、ページ毎のデータを取得

scraping.py 

### 概要

* `BASE_URL` のURLにpetid を指定してそのページのデータを取得する
* main でpetid を指定して、ループでデータを取得する流れ
* `OUT_CSV` に取得したテキストデータが保持される
* `IMG_PATH` の下にpetidと同名のディレクトリが作られ、その下に画像が保持される（テキストデータの作成と同じタイミングで作成される

### 動作方法

* Python 3.7 or 3.8 では動作確認済み
* 取得する対象によって、 BASE_URL や mainメソッドでpetid の範囲を指定する
* 以下の操作で環境を作成し、実行

```
# pip installでは不要な物もありますが・・・
# venv は必要に応じて作成

> pip install -r requirements.txt
> python scraping.py

```

