# 以下多種操作字串的方式，幫助更有效率寫程式。
# 還有很多其他的string_method方法，這裡最常用的

#注意字串第一個數字是從index 0開始算的
id_number="B114020027_資管系邵威捷"
first_char=id_number[0]
print("first_char:", first_char)#輸出 "B"

second_char=id_number[1]
print("second_char:", second_char)# 輸出 "1"

first_four_char=id_number[0:4]
print("first_four_char:", first_four_char) # 輸出 "B114"

last_one_char=id_number[-1]
print("last_one_char:", last_one_char)     # 輸出"捷"


# 1.len()函數用於返回字串的長度，也就是字符的數量。
text = "hello nsysu student"
print(len(text))  # 輸出20


# 2. str.find(substring)
# find() 方法用於查找子字串的首次出現位置。如果未找到子字串，返回 -1。
text = "hello nsysu student"
print(text.find("nsysu"))  # 輸出6 
print(text.find("Python")) # 輸出-1

# 3. str.capitalize()
# capitalize() 方法將字串的第一個字母轉換為大寫字母，其餘字母轉換為小寫字母。
text = "hello nsysu student"
print(text.capitalize())  #輸出 "Hello nsysu student"


# 4. str.upper()
# upper() 方法將字串中的所有字母轉換為大寫字母。
text = "hello nsysu student"
print(text.upper())  # 輸出 "HELLO NSYSU STUDENT"


# 5. str.lower()
# lower() 方法將字串中的所有字母轉換為小寫字母。
text = "HELLO NSYSU STUDENT"
print(text.lower())  # 輸出 "hello nsysu student"


# 6. str.count(substring)
# count() 方法用於計算子字串 substring 在字串中出現的次數。
text = "hello nsysu student"
print(text.count("student"))  # 輸出 1


# 7. str.replace(old, new)
# replace()方法用於將舊的字串換成新的字串
text = "hello nsysu student"
print(text.replace("nsysu", "university"))  # 輸出 "hello university student"