@echo off

rem 修改標題
title server_for_yrpc

rem 切換工作路徑
cd /d C:\Users\user\Documents\Rogers\ys_yrpc\flask

rem 生產環境 使用 waitress wsgi server
python waitress_main.py