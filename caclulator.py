# (1)簡易的計算機
# 以下是一個簡易的計算機
# 透過輸入兩個數字跟運算符號跑出結果
# 除數於0要特別處理
num1 = float(input("請輸入第一個數字："))
operator = input("請輸入+ 或 - 或 * 或 /：")
num2 = float(input("請輸入第二個數字："))

if operator == "+":
    result = round(num1 + num2)
elif operator == "-":
    result = round(num1 - num2)
elif operator == "*":
    result = round(num1 * num2)
elif operator == "/":    #在除法條件下再設另一個if，除數不可為0
    if num2 == 0:
        result = "無意義"
    else:
        result = round(num1 / num2)
else:
    result = "無法運算"
print(result)


#(2)複利計算機
# 先來了解複利公式
# 總金額=本金*(1+(利率/100))**年限
# 先寫變數
amount=0
rate=0
time=0

while amount<=0:
    if amount<=0:
        print("本金不能小於0")
    amount=float(input("請輸入本金"))

while rate<=0:
    if rate<=0:
        print("利率不能小於0")
    rate=float(input("請輸入利率"))

while time<=0:
    if time<=0:
        print("時間不能小於0")
    time=float(input("請輸入時間"))

print("本金",amount)
print("利率",rate)
print("時間",time)
total=amount*(1+rate/100)**time
print("最後總共金額為",round(total))