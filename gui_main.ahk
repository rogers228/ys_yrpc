; 開啟 或 重啟 web server 網路服務器

#SingleInstance force
Menu, Tray, Icon, camera.ico
Menu, Tray, Add, 重啟server, open_or_reload
open_or_reload() ;直接啟動


runbat(){
    ; RunWait, svelte_update_to_flask.bat
    RunWait, open_server.bat
}

open_or_reload(){
	if WinExist("server_for_yrpc"){
		; Msgbox, 已開啟
		WinKill   ; 關閉
		Sleep 500 ; Waits 1 second
		runbat()  ; 啟動bat
	}
	else{
		; Msgbox, 尚未開啟
		runbat()  ; 啟動bat
	}
}