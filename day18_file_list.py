import os

path = "." # カレントディレクトリ
files = os.listdir(path)

print("フォルダ内のファイル一覧：")
for file in files:
    print("-", file)