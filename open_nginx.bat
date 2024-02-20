rem 啟動 nginx 前 需先檢查 避免重複開啟
@echo off

rem 切換工作路徑
cd /d C:\Users\user\nginx-1.23.0

rem 啟動 nginx 來 反向代理 https 開啟後關閉cmd
start nginx

rem 等待
timeout /t 1 /nobreak

rem 結束離開cmd
exit
