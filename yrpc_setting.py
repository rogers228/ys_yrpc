import os

dic_base = {
    'VM-TESTER': r'C:\Users\user\Documents\Rogers',
}

dic_sublime_settings = {
    'VM-TESTER': r'C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User\Preferences.sublime-settings',
}

computer = os.environ['COMPUTERNAME']
if computer not in list(dic_base.keys()):
    raise TypeError('computer is not found!') # 不同電腦將引發錯誤

pj_base = dic_base.get(computer) # 依電腦名稱尋找 project_base
# print('pj_base:', pj_base)

# sublime text
SUBLIME_SETTING = dic_sublime_settings.get(computer)
# project
PATH_YRPC = os.path.join(pj_base, 'ys_yrpc') # 依實際情況修改
PATH_FLASK = os.path.join(PATH_YRPC, 'flask')
FILE_INDEX = os.path.join(PATH_FLASK, 'index.html')
FILE_CERTIFICATE = os.path.join(PATH_FLASK, 'certificate.pem')
FILE_KEY = os.path.join(PATH_FLASK, 'key.pem')

def test1():
    print(PATH_YRPC)
    print(PATH_FLASK)
    print(FILE_INDEX)
    print(FILE_CERTIFICATE)
    print(FILE_KEY)

if __name__ == '__main__':
    test1()
