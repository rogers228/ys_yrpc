import os, subprocess

is_hide = True  # True | False
custom_hide_files = [ # 檔案設定顯示隱藏 使用註解將被隱藏
    # -- file
    # '.gitattributes',
    # '.gitignore',
    'readme.md',

    # --gui
    # 'gui_main.ahk',
    # 'camera.ico',

    # -- flask

    # -- ssl
    # 'cert.pem',
    # 'key.pem',
    ]

custom_hide_folders = [
    # --git
    # '.git',

    # --python
    # '__pycache__',
]

def main():
    dic_base = {
        'VM-TESTER': r'C:\Users\user\Documents\Rogers', # 依照電腦 設定專案資料夾的 path (專案資料夾的上層)
    }
    computer = os.environ['COMPUTERNAME']
    if computer not in list(dic_base.keys()):
        raise TypeError('computer is not found!') # 不同電腦將引發錯誤
    path_ffds = os.path.join(dic_base[computer], 'sublime_text_ffds')
    pj_name = os.path.basename(os.path.dirname(__file__))
    command = f'python sublime_setting.py -project {pj_name} -mode 1'
    subprocess.run(command, cwd=path_ffds, shell=True, capture_output=True, text=True)

if __name__ == '__main__':
    main()