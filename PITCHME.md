
## Dash hands on
#### はんなりPython #11

---

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

### はい。でも次は結構すごいです。      

---

### app4.py
- スライダーを使って年を選んだり    
- legendをクリックしただけでデータが選択できたりします。    
    
+++?code=app4.py     
    
