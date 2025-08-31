# 書き込み
with open("intro.txt", "w", encoding="utf-8") as f:
    f.write("こんにちは、私はPythonを学習中です！\n")
    f.write("1日1時間ずつ頑張っています。")

# 読み込み
with open("intro.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("ファイルの内容：")
    print(content)