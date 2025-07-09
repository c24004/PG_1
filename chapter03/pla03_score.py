import sys
def test(num):
    if num < 0:
        print("あなたは補習です")
        sys.exit()
    elif num > 100:
        print("ズルはいけません")
        sys.exit()
math = int(input("数学の点数："))
test(math)
english = int(input("英語の点数："))
test(english)
score = ""
if math >= 90 and english >= 90:
    score = "S"
elif math >= 70 or english >= 70:
    score = "A"
elif math >= 50 or english >= 50:
    score = "B"
else:
    score = "C"
print(f"あなたの成績は{score}です")
