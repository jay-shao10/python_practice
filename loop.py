#複習(1)for迴圈 (2)巢狀迴圈 (3)if-elif-else (4)while 

# (1)for迴圈
# 就是重複做一件事情
for x in range(1,10):#這是1到10之間，10不包含!!!!
    print(x,end=" ")
    # end=" " 可以讓所有的輸出在同一行，並用空格分隔。
    #輸出1 2 3 4 5 6 7 8 9

for x in reversed(range(1,10)):
    print(x,end=" ")
    #輸出9 8 7 6 5 4 3 2 1 

student="B114020027_邵威捷"
for x in student:
    print(x)


# (2)巢狀迴圈 
# 定義一個 3x3 的矩陣
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 外層迴圈處理行
for row in matrix:
    # 內層迴圈處理列
    for element in row:
        print(element, end=" ")
    print()  # 打印換行符，用於分隔行




#(3) if-elif-else
# 根據條件來控制程式。當條件成立時代碼會執行，否則會跳過該代碼塊。
# 舉個例子大家就懂了
activity = input("請問邵威捷同學在做什麼？輸入讀金融或寫程式或偷懶或其他事情: ")
if activity == "讀金融":
    print("你正在學習金融知識，準備變成下一個股神！")
elif activity == "寫程式":
    print("你正在練習 Python 程式設計，請保持這樣的動力！")
elif activity == "偷懶":
    print("你正在偷懶睡覺，該起來做點有意義的事情了！")
else:
    print("不管在做甚麼事情都請加油歐")



# (4) while
# 也可以使用 while 迴圈來加入並修改if-elif-else 。
# while True: 會使迴圈一直執行，直到遇到 break(會終止迴圈)。
# 如果輸入無效，顯示提示消息，讓使用者重新輸入。
while True:
    activity = input("請問邵威捷同學在做什麼？輸入讀金融或寫程式或偷懶或其他事情: ")
    
    if activity == "讀金融":
        print("你正在學習金融知識，準備變成下一個股神！")
        break
    elif activity == "寫程式":
        print("你正在練習 Python 程式設計，保持這樣的動力！")
        break
    elif activity == "偷懶":
        print("你正在偷懶睡覺，該起來做點有意義的事情了！")
        break
    elif activity == "其他":
        print("不管在做甚麼事情都請加油歐'。")
        break
    else:
        print("輸入無效，請重新輸入。")
