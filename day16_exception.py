filename = "data.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"{filename} が存在しません。新しく作成します。")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("これは新しく作成されたファイルです。")