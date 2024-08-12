#(1)list(2)set(3)tuple(4)dictionary的資料型別還有sort方法

# dictionary
# 語法: dictionary = {key1: value1, key2: value2, ...}
# 每個鍵必須是唯一的，值可以重複。
# 鍵是不可變的（如字串、數字、元組），但值可以是任意類型。
# 使用鍵來訪問對應的值。
my_dict = {"邵威捷": "資管", "王小明": "企管", "陳小光": "財管"}

# 遍歷字典中的鍵值對
for key, value in my_dict.items():
    print("key:", key)    # 輸出key
    print("value:", value)  # 輸出value

# 使用 get() 方法取得指定鍵的值
print(my_dict.get("邵威捷"))  # 輸出: 資管

# 使用 update() 方法更新字典，添加新的鍵值對
my_dict.update({"李美珠": "國際商務"})
print(my_dict)  # 輸出: {'邵威捷': '資管', '王小明': '企管', '陳小光': '財管', '李美珠': '國際商務'}

# 使用 pop() 方法刪除指定鍵的鍵值對
my_dict.pop("王小明")
print(my_dict)  # 輸出: {'邵威捷': '資管', '陳小光': '財管', '李美珠': '國際商務'}

# 使用 values() 方法獲得字典中所有的值
print(my_dict.values())  # 輸出: dict_values(['資管', '財管', '國際商務'])

# 使用 items() 方法獲得字典中所有的鍵值對
print(my_dict.items())  # 輸出: dict_items([('邵威捷', '資管'), ('陳小光', '財管'), ('李美珠', '國際商務')])





# list 
# 語法: list = [元素1, 元素2, ...]
# 是有序且可變的集合，可以出現重複的值
# 適用於需要保持順序且需要修改的數據。

# 定義一個包含三種水果的列表
fruits = ["apple", "banana", "guava"]

# 在列表末尾添加 "pear"
fruits.append("pear")
# 此時列表變為 ["apple", "banana", "guava", "pear"]

# 移除列表中的 "banana"
fruits.remove("banana")
# 此時列表變為 ["apple", "guava", "pear"]

# 將列表中的元素反轉
fruits.reverse()
# 此時列表變為 ["pear", "guava", "apple"]

# 輸出最終的列表
print(fruits)  # 輸出: ["pear", "guava", "apple"]






# set 
# 語法: set = {元素1, 元素2, ...}
# 是沒有順序且元素部會重複的集合
# 適用於需要去重或進行集合運算的數據

# 定義一個集合，包含三個水果
fruits_set = {'apple', 'banana', 'guava'}

# 由於集合不允許重複元素，因此apple已經存在於集合中，這個操作不會改變集合
fruits_set.add('apple')

# 添加 'watermelon' 到集合中
fruits_set.add('watermelon')

# 輸出集合的內容
print(fruits_set)  # 可能的輸出: {'banana', 'watermelon', 'guava', 'apple'}






# tuple 
# 語法: tuple = (元素1, 元素2, ...)
# 是一個不可變的、按順序排列的集合，可以包含任意類型的元素。
# 元素不可修改（不可變）。
# 可以包含重複的元素。


fruits_tuple = ("apple", "banana", "guava")
# 嘗試將 "apple" 添加到元組中
# 這會引發錯誤，因為元組是不可變的，不能進行添加操作
fruits_tuple.add("apple")


# python中sort方法
# list的排列
# 定義一個包含數字的列表
num_list = [1, 3, 5, 2, 4]

# 將數字由小到大進行排序
num_list.sort()
print(num_list)  # 輸出: [1, 2, 3, 4, 5]

# 將數字由大到小進行排序
num_list.sort(reverse=True)
print(num_list)  # 輸出: [5, 4, 3, 2, 1]


