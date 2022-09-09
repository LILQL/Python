from ast import Num
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index1.html')
def index1():
    return render_template("index1.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/detail.html')
def detail():
    datalist1=[]
    score=[]
    num=[]
    conn=sqlite3.connect('movie.db')
    sql="select * from movie250"
    sql1="SELECT score,count(score) FROM movie250 group by score "
    c1=conn.cursor()
    data1=c1.execute(sql)
    if(data1==c1.execute(sql)):
        for item in data1:
            datalist1.append(item)
    if(data1==c1.execute(sql1)):
        for item in data1:
            score.append(item[0])
            num.append(item[1])
    conn.commit()
    conn.close()

    return render_template("detail.html", movies=datalist1, score=score, num=num)


if __name__ == '__main__':
    app.run()
