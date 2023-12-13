import random
import matplotlib.pyplot as plt

# 空のリストを作成して、xの値を保存する
x_values = []
y = {}

def count():
    global x_values, y  # グローバルなリストとディクショナリを使うことを示す

    value = random.randint(1, 10)
    x_values.append(value)  # xの値をリストに追加
    print(value)
    
    # ディクショナリに出現回数を記録
    if value in y:
        y[value] += 1
    else:
        y[value] = 1

# count()を1000回呼び出す
for _ in range(1000):
    count()

# グラフのプロット
plt.hist(x_values, bins=range(1, 12), align='left', edgecolor='black')
plt.xlabel('値')
plt.ylabel('出現回数')
plt.title('値の出現回数のヒストグラム')
plt.xticks(range(1, 11))
plt.show()

# 各数値の出現回数を表にする
print("数値 | 出現回数")
for num, count in y.items():
    print(f"{num} | {count}")
