import os, sys
from flask import (Flask, send_file)
from flask_cors import CORS

_p = os.path.dirname # 上層
sys.path.append(_p(_p(os.path.abspath(__file__))))
from yrpc_setting import *

app = Flask(__name__)

@app.route("/")
def index():
    return send_file(FILE_INDEX)

def test1():
    print('test1')

if __name__ == '__main__':
    test1()

# 開發環境使用 flask內建的 Werkzeug 作為server啟動  進行調試
# cmd
# cd /d C:\Users\user\Documents\Rogers\ys_yrpc\flask
# set FLASK_APP=flask_main
# set FLASK_ENV=development
# flask run --port=8245          啟動app server
# 瀏覽器上運行 http://127.0.0.1:8245/
