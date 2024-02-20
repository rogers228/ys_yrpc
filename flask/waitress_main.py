# 生產環境 使用 waitress wsgi server

import os, sys, time
from waitress import serve

_p = os.path.dirname # 上層
sys.path.append(_p(_p(os.path.abspath(__file__))))
from yrpc_setting import *

sys.path.append(PATH_FLASK)   # 加入 falsk app路徑
import flask_main               # 匯入 flask 主程序


def main():
    # print('run_server')
    app_server_name = 'server_yrpc'
    port = 8245 # 預設80
    threads = 10 # 請求駐列數量

    print(f'\n=========  {app_server_name} is running.  ===========')
    print(f'\nhttp://220.168.100.186:{port}/')
    print(f'\nfrom: {time.strftime("%Y-%m-%d %H:%M", time.localtime())}')
    print('\nCtrl + c to exit')
    print(f'\n=========         請勿關閉         ===========')

    serve(flask_main.app, host='0.0.0.0', port=port, threads=threads) # 以serve開啟 flask app

    # cmd 執行 waitress
    # cd /d C:\Users\user\Documents\Rogers\ys_yrpc\flask
    # python waitress_main.py

def test1():
    print('test1')

if __name__ == '__main__':
    main()