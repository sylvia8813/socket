from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

from config import Config

app = Flask(__name__) #建立application物件

app.config.from_object(Config)

db = SQLAlchemy(app)

#建立網站首頁回應方式
@app.route("/")
def hello(): #回應網站首頁連線的的方式
    title = 'HomePage'
    return render_template('Main_page.html', title=title) #回傳網站首頁的內容

with app.app_context(): #沒加這段害我浪費一小時 gan==
    db.create_all()

#啟動網站伺服器
if __name__ == '__main__':
    app.run(debug=True)
    