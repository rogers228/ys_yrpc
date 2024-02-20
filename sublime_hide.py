# 此腳本由 SublimeOnSaveBuild (sublime套件) 設定為儲存後自動執行
# 用來控制資料夾，檔案的隱藏狀態

import os, re, json5, json

is_hide = True  # True | False
custom_hide_files = [ # 檔案設定顯示隱藏 使用註解將被隱藏
    # -- 通用
    # '.gitattributes',
    '.gitignore',
    'readme.md',
    'yrpc_setting.py',
    # 'camera.ico',
    # 'gui_main.ahk',
    # 'open_server.bat',

    # -- flask
    # 'cert.pem',
    # 'key.pem',
    ]

custom_hide_folders = [

    # --git
    # '.git',
    # --node
    # 'node_modules',

    # --python
    # '__pycache__',
]

# 以下平常不需要修改
if True:
    dic_sublime_settings = {
        'VM-TESTER': r'C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User\Preferences.sublime-settings',
    }
    computer = os.environ['COMPUTERNAME']
    if computer not in list(dic_sublime_settings.keys()):
        raise TypeError('computer is not found!') # 不同電腦將引發錯誤
    sublime_setting = dic_sublime_settings.get(computer)
    ps = sublime_setting

def read_option():
    # 讀取 hide 設定檔
    with open(ps, encoding='utf-8') as data:
        dic = json5.loads(data.read())
    json_str = json5.dumps(dic, indent = 4)
    print(json_str)

def set_option(lis_files=[], lis_folders=[]):
    # lis_file     隱藏檔案
    # lis_folders  隱藏資料夾
    with open(ps, encoding='utf-8') as data:
        dic = json5.loads(data.read())
    dic['file_exclude_patterns'] = lis_files
    dic['folder_exclude_patterns'] = lis_folders
    json_str = json.dumps(dic, indent = 4) #格式化
    with open(ps, 'w') as outfile:
        outfile.write(json_str)
    # print('write hide is finished')

def get_hide_files():
    with open(__file__, encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'custom_hide_files\s*=\s*\[([^]]*)\]', re.DOTALL)
    match = pattern.search(content)
    lis = []
    if match:
        match_content = match.group(1) # 欲隱藏者 使用註解掉 符合使用者習慣
        lis = re.findall(r'#\s*\'([^\']*)\'', match_content)

    lis = list(filter(lambda e: e != os.path.basename(__file__), lis)) # 排除自身
    return lis

def get_hide_folders():
    with open(__file__, encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'custom_hide_folders\s*=\s*\[([^]]*)\]', re.DOTALL)
    match = pattern.search(content)
    if match:
        match_content = match.group(1) # 欲隱藏者 使用註解掉 符合使用者習慣
        lis = re.findall(r'#\s*\'([^\']*)\'', match_content)
        return lis

def main():
    if is_hide:
        lis_files=get_hide_files()
        lis_folders=get_hide_folders()
        print('hide files:')
        for e in lis_files:
            print(f'    {e}')
        print('\nhide folders:')
        for e in lis_folders:
            print(f'    {e}')
        print()
        set_option(lis_files, lis_folders)
    else:
        set_option()

if __name__ == '__main__':
    main()