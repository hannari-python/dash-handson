
## Dash hands on
#### はんなりPython #11

---

### 自己紹介
- 小川　英幸([@mazarimono](https://twitter.com/mazarimono))     
- はんなりPythonの会、Blockchain Kyoto主催    
- 合同会社長目（ちょうもく）って会社やってます。    
- そろそろ頑張って働かないとなー。     

### 今日の予定
1 Dashの使い方の概要    
2 データの前処理    
3 各自好きなデータで実際に作ってみる    
4 出来たものを見せる！   

---

### Dash
- 可視化ツール     
- Flask, Plotly.js, React.jsで作られている。     
- ブラウザでみられる     
- 色々工夫ができる    
- [Dash User Guide](https://dash.plot.ly/)     
- [Dash App Gallary](https://dash.plot.ly/gallery)
     
---

### 基本的な書き方

+++?code=app1.py    
- CUIで [ $python app1.py ] とすると・・・    

+++?image=app1.PNG&size=auto 70%    
    

---    

- app = dash.Dash() / アプリの箱作り    
- app.layout = ~~~ / アプリの中身作り     
- [dash_core_components](https://dash.plot.ly/dash-core-components) / インタラクティブなインターフェースを作る。スライダーとかボタン、グラフもこれを使う。     
- [dash_html_components](https://dash.plot.ly/dash-html-components) / アプリケーションのHTMLの部分に使う。    
- [dash_table](https://dash.plot.ly/datatable) / 11月2日にリリースされた。データを見るのに良い塩梅にしてくれる。     

---    

### なんか大したことないよね
<br>
### はい。でも以降は結構すごいです。      

---

### 色々見てみましょう
- コードを実行してどんな動きをするか見ましょう    
- コードの中身も見ましょう    
- $ python app4.py    
    
---?image=app4.PNG&size=auto 70%     

+++?code=app4.py     
- sliderから年をインプット ==> その年で関数実行 ==> 関数内のgo.scatterで作図　==> dcc.Graphにそれを渡す(app4.py)       

+++?code=app5.py
- 3つのコールバックにより、複雑な動きを実現している。(app5.py)     
- 右の二つのチャートはdef create_time_series()で作られている。     
     

+++?code=app6.py
- すごいー    
- 解説はなしの方向で・・・(app6.py)    
      
+++?code=app7.py
- グラフを下にどんどん足している。(app7.py)    


---

### データの形
- 今まではコードは見ましたが、データを見ていませんでした。    
- 何をやるにもデータの扱いやすい形ってのがあります。   
- ライブラリに同封されているものは扱いやすいが・・・。     
- ML/DLなんかも実際にどうデータを作るかって意外に難しい。     
- 一先ず、データがどんな形か見てみましょう！     

---     

### データを整える
- sklearnのデータを使って、Dashで使いやすいようにデータを作ってみます。    
- 先ほど見たような形に作ってみましょう。    
- <これを使ってなんか作るかどうするか？     
     
---

### 作ってみましょう！    
- では、何かデータを使ってDashでアプリを作ってみましょう！    
- 目的はデータを見やすくすることであるので、シンプルで見やすくすることを心掛けた方が良いかもしれません。     
- やってみたいデータがある人はそれを、ない人はsklearnのdatasetsを使ってください。   

---

### 披露しましょう！
- 作ったものを全員で見せ合いましょう！