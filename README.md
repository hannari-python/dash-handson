# スライド

[はんなりPython #11](https://gitpitch.com/hannari-python/dash-handson/master?grs=github&t=simple)

# ハンズオンの準備

このリポジトリをcloneしておいてください。cloneするにはgitコマンドが使える状態である必要があります。
[gitのインストールページ](https://git-scm.com/book/ja/v1/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB) を参照してインストールしてください。  
  
```
$ git clone https://github.com/hannari-python/dash-handson.git
```

で準備完了です。


## 方法その1 各種ライブラリをインストールします。

今回のハンズオンで使う以下の3つのライブラリを`pip`コマンドを使ってインストールします。

- dash
- pandas
- scikit-learn

```
$ pip install dash==0.28.5
$ pip install dash-html-components==0.13.2
$ pip install dash-core-components==0.35.1
$ pip install pandas
$ pip install -U scikit-learn
```

必要なライブラリがそろったら `app.py` を実行します。

```
$ python app1.py
```

ブラウザでアクセスするとDashのページが表示されます。
[http://localhost:8050/](http://localhost:8050/)



## 方法その2 Dockerを使う方法

[Docker](https://www.docker.com/get-started)ページからインストーラーを使ってインストールしてください。  
他にもインストール方法があるので各自の環境に合わせてインストールしてください。  
`docker` コマンドが使える状態にしてください。

このリポジトリをクローンして `dash-handson/` に移動します。

```
$ cd dash-handson
```

Dockerイメージを作成します。

```
$ docker build -t dash-handson .
```

Dockerコンテナを起動します。

```
$ docker run --rm -it -v $(pwd):/work -P -p 8050:8050 dash-handson python app1.py
```

ブラウザでアクセスするとDashのページが表示されます。
[http://localhost:8050/](http://localhost:8050/)


