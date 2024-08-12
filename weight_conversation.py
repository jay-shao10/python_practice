# 以下是體重轉換器，請輸入你的體重和單位就可以同時顯示你kg或是lb的體重
# 轉大寫.upper() 與小寫.lower():
# round()四捨五入，避免小數點太多位

weight = float(input("請輸入你的體重"))
unit = input("單位是KG還是LB ").upper()
weight_LB = 0.0
if unit == 'KG':
    weight_LB = weight*2.2
elif unit == 'LB':
    weight_LB = weight
    weight = weight/2.2
else :
    print("單位錯誤")
    exit()
print(f"你的體重是 {round(weight,2)}KG，{round(weight_LB, 2)}LB")



# 溫度轉換器。
temp = float(input("請輸入溫度："))
unit = input("單位是 (C/F)：").upper()
new_unit = ""
if unit == 'C':
    temp = round(temp * 9 / 5 + 32)
    new_unit = "F"
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9)
    new_unit = "C"
else:
    print("非單位")
    exit()

print(f"轉換後的溫度是 {temp} {new_unit}")


# 轉大寫upper() 與小寫lower():
# original_string = "Hello, World!"
# original_string.upper() 轉大寫
# original_string.lower() 轉小寫
