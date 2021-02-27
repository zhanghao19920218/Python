# Python 从入门到实践
## 2. 变量和简单数据类型
> 在本章，你将学习在Python中使用的各种数据，还将学习如何在程序中使用变量来表示这些数据

### 2.1 运行hello_world.py时发生的情况
```python
print("Hello Python world!")
```
* 末尾`.py`指出这是一个Python程序
* 编辑器将使用**Python解释器**来运行
* Python解释器读取整个程序，确定其中每个单词的含义，比如`print`

### 2.2 变量
```python
message = "Hello Python world!"
print(message)
```
这里添加了一个`message`的**变量**, 每个**变量**都指向一个**值**----与该变量相关联的信息
Python解释器的处理过程:
* 将变量`message`与文本`Hello Python World!`关联起来
* 将与变量`message`相关联的值打印到屏幕

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```
#### 2.2.1 变量的命名与使用
#### 2.2.2 使用变量时避免命名错误
(本节略)
#### 2.2.3 变量是标签

### 2.3 字符串
定义: **字符串** 就是一系列的字符。单引号或双引号都行
```python
"This is a string."
'This is also a string.'
```
这种灵活性让你能够在字符串中包含引号和撇号
```python
```

#### 2.3.1 使用方法修改字符串的大小写
* title() 首字母大写
* upper() 全部字母大写
* lower() 全部字母小写

#### 2.3.2 在字符串中使用变量
```python
firstName = "Taylor"
lastName = "Swift"
print(f"{firstName} {lastName}") # Taylor Swift
```
* f 代表的是format
* 使用{}来使用变量

#### 2.3.3 使用制表符或换行符来添加空白
**空白**泛指任何非打印字符，如空格、制表符和换行符。
* \n 换行符
* \t 制表符
* \n\t 换行+制表符
```shell
>>> print("Language:\n\tJavaScript\n\tPython\n\tC")
```

#### 2.3.4 删除空白
* 使用rstrip()删除右侧空白
* 使用lstrip()删除左侧空白
* 使用strip()删除整个字符串空白

### 2.4 数
#### 2.4.1 整数
* `+`:加
* `-`:减
* `*`:乘
* `/`:除
* `**`: 表示指数

#### 2.4.2 浮点数(Float)
Python将所有带小数点的数为**浮点数**

#### 2.4.3 整数和浮点数
* 任意两个整数相除 => 结果总是浮点数(Float)
* 任何运算，如果一个为Float，则结果肯定是Float

#### 2.4.4 数中的下划线
```python
universe_age = 14_000_000_000
```

#### 2.4.5 同时给多个变量赋值 
```python
x, y, z = 0, 0, 0
```

#### 2.4.6 常量
**常量**类似于变量，但其值在程序的整个生命周期内保持不变。Python没有内置的常量类型, 但Python程序员会使用全部大写来指出某个值为常娘
```python
MAX_CONNECTIONS = 5000
```

### 2.5 注释
#### 2.5.1 如何编写注释
```python
# 向大家问好
print("Hello Python people!")
```

## 3 列表简介
> 本章和下一章泥浆学习列表是什么及如何使用列表元素。列表让你能够在一个地方存储成组的信息，其中可以只包含几个元素，也可以包含数百万个元素，
### 3.1 列表是什么
**列表**由一系列按照特定顺序排列的元素组成。列表通常包含多个元素，因此给列表指定一个表示复数的名称（如`letters`、`digits`或`names`）是个不错的主意。

#### 3.1.1 访问列表元素
列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（**索引**）告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在括号内。
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```
#### 3.1.2 索引从0而不是1开始
* 使用-1返回最后一个元素

#### 3.1.3 使用列表中的各个值

### 3.2 修改、添加和删除元素
#### 3.2.1 修改列表元素
* 根据索引拿到值
* 指定索引元素的新值
```python
bicycles = ['trek', 'cannonable', 'truck', 'green']
bicycles[0] = 'bus'
print(bicycles)
```
#### 3.2.2 在列表中添加元素
* append()函数可以添加
* insert()可以从中间插入

#### 3.2.3 从列表中删除元素
* `del`语句删除元素
```python
del bicycles[1]
```
* `pop()`删除尾部元素
* `pop(index)`删除索引下的元素, pop()有返回值
* `remove()`删除key-value里面的值类型，而且仅删除最前面一次
> 注意: 方法`remove()`只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。这将在第7章中介绍。

### 3.3 组织列表

#### 3.3.1 使用方法`sort()`对列表永久排序
* sort()排序
* sort(reverse=True)反向排序

#### 3.3.2 使用函数`sorted()`对列表进行临时排序
* sorted(arr)

#### 3.3.3 倒着打印列表
* `reverse()`

#### 3.3.4 确定列表长度
* `len()`函数

## 4 操作列表
> 学习**遍历**
### 4.1 遍历整个列表
* `for`循环
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
#### 4.1.1 深入研究循环
循环这种概念很重要，
```python
for magician in magicians:
```
#### 4.1.2 在`for`循环中执行更多操作

### 4.2 避免缩进错误
### 4.3 创建数值列表
* 列表非常适合用户存储数字集合，而Python提供了很多工具
#### 4.3.1 使用函数`range()`
```python
for value in range(1, 5):
    print(value)
```
#### 4.3.2 使用`range()`创建数字列表
* 使用函数`list()`将`range()`的结果转为列表
```python
numbers = list(range(1, 5))
print(numbers)
```
* range(startIndex, endIndex, space) space跳了几个index

#### 4.3.3 对数字列表执行简单的统计计算
* min()
* max()
* sum()

#### 4.3.4 列表解析
**列表解析**将`for`循环和创建新元素的代码合成一行，并自动附加新元素。
```python
squares = [value**2 for value in range(1, 10)]
print(squares)
```

### 4.4 使用列表的一部分
Python处理列表的部分元素: 切片
#### 4.4.1 切片
* arr[startIndex: endIndex]
* 索引`startIndex`为负数则从尾部取值
```python
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])
```
#### 4.4.2 遍历切片
```python
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
# print(players[0:3])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
```
#### 4.4.3 复制列表
* 使用`[:]`函数操作直接全部复制
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # 深拷贝还是浅拷贝

print("My favorite foods are:")
my_foods[1] = 'apple'
print(my_foods)
print(friend_foods)
```