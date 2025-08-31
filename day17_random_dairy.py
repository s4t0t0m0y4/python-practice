import datetime
import random

datestr = datetime.date.today().strftime("%Y-%m-%d")
moods = ["楽しかった", "眠い", "元気いっぱい", "だるい", "やる気がある"]

with open("dairy.txt", "a", encoding="utf-8") as f:
    line = f"{datestr} の気分： {random.choice(moods)}\n"
    f.write(line)

print("日記を追加しました！")