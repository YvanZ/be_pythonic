# 第一周

To be continued



# 内置数据类型

## Python全景

Python程序可以分解为模块，语句，表达式及对象

- 程序由模块构成

- 模块包含语句

- 语句包含表达式

- 表达式建立并处理对象

字符串，列表和元组都是序列，序列支持索引和分片。所以从访问角度来说，它们都是一样的。

切割列表时，即便start或end索引越界，也不会出现问题。但是，访问单个元素，下标不能越界，否则导致异常`IndexError: list index out of range`

可以将列表的某个范围替换成新值，即便长度不同依然可以替换

```python
a = [ 1, 2, 3, 4, 5 ]
a[1:3] = [ -2, -3, -4 ]
print a # Prints [ 1, -2, -3, -4, 4, 5 ]
```



## 字符串

代码中对于字符串，推荐优先用双印号，其次再用单引号。多行使用三引号。

连接字符串，优先使用`join`而不是`+`符号，因对内存的使用不同。

```python
",".join(["abc", "def"])
"".join(["abc", "def"])
```

字符串格式化，推荐使用`format`函数，少用`%`。若一个格式多次出现，可先定义一个格式，之后调用`format`方法达到复用的目的

```python
f = "result{0}"

f.format(1)
f.format("one")
```

当然，有些情况下例如在写python操作shell的命令，若shell命令中包含{}，则该使用`%`方式。

更多`format`资料可见：

[pyFormat](https://pyformat.info/)

[Python String Format Cookbook](https://mkaz.tech/python-string-format.html)



## 列表



## 元组

不可变的列表



## 字典

创建字典

`D = dict(name='Bob', age='42', job='dev')`

还可以使用如下的方式添加字典键值

`d['a'] = 1`

字典的key并不一定总是字符串，其具有不可变，以及可哈希等属性。

`D.get(k[,d])`字典的get方法，提供获取键k值的功能，若字典中没有k，则返回d的值，其中d的默认值为None。



## 动态类型

函数是传值还是传引用的思考

```python
# 传递不可变对象
def f1(aa):
    aa = 1

a = 0
f1(a)
print a # Prints 0
```

```python
# 传递可变对象
def f2(bb):
    bb[0] = 1
    
b = [0]
f2(b)
print b # Prints [1]
```

结论：对于python函数参数，既不是传值也不是传引用。正确的说法应该是传递参数的引用，函数在参数传递过程中，将整个对象传入，对不可变对象，由于不能修改，所以修改往往是通过生成一个新对象来实现。对于可变对象，修改对外部内部都可见。



## 引用计数器

python在每个对象上保存了一个计数器，记录当前指向该对象引用的数目。当计数器为0，python自动将对象回收

```python
import sys
a = [1, 2, 3]
sys.getrefcount(a)
```

当前值会为2，因为在新建对象之时，python自身会对该对象也引用一次。



## 列表解析

`[expr for iter_item in iterable if cond_expr]`

对于一个可迭代对象，将其迭代并对每一项进行操作，同时可以使用`if`语句过滤一些项。

例：

```python
# 一行代码罗列当前目录下所有.py结尾的文件之一
[ item for item in os.listdir(".") if item.endswith('.py') ]
```

```python
# 创建内含5个0的列表
[ 0 for i in range(5) ]
```



## 文件

尽量使用with语句，可自动关闭资源

```python
with open("/etc/passwd", "rt") as myfile:
    for line in myfile:
        # process line

# with也可以打开多个文件，这里的source和target为演示用，实际上需要先赋值。
with open(source) as s, open(target, 'w') as t:
    t.write(s.read())
        
def get_conn(**kwargs):
    return pymysql.connect(host=kwargs.get('host', '127.0.0.1'),
                          user=kwargs.get('user'),
                          passwd=kwargs.get('password'),
                          port=kwargs.get('port', 3306))
conn = get_conn(user='', password='')
with conn as cur:
    sql = ''
    cur.execute(sql)
    rows = cur.fetchall()
    print rows
```

写一个不存在的文件，使用x模式。文件不存在顺利写入，文件存在则抛出异常`FileExistError`

```python
with open("somefile", "xt") as f:
    f.write("Hello World\n")
```



## 数据类型高级话题

从内部实现的角度，python中的list和tuple都是数组。与链表相比，数组在内存中是挨着的，在获取元素的时候，只需要知道起点以及偏移量，就可以获取元素值，其时间复杂度只有O(1)。而链表中各元素依靠指针连接，获取元素时，链表需要从第一个元素开始顺着链路依次查找，时间复杂度为O(n)。



## 补充一些操作系统的标准库

使用subprocess库执行shell命令

```python
def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout
```

fnmatch和glob使用举例

```python
# 一行代码罗列当前目录下所有.py结尾的文件之二
[ item for item in os.listdir(".") if fnmatch.fnmatch(item, "*.py") ]

glob.glob("*.py")
```



## 练手

1. 获取当前用户home目录下所有的文件列表
```python
import os

```
2. 获取当前用户home目录下所有的目录列表
```python
import os

```
3. 获取当前用户home目录下所有目录的目录名到绝对路径之间的字典
```python
import os

```
4. 获取当前用户home目录下所有文件到文件大小之间的字典
```python
import os

```
5. 读取`/etc/passwd`文件，获取用户名，用户的home目录和shell。保存到userinfo.txt文件中，并以逗号分隔。程序可以反复执行，如果userinfo.txt文件已经存在，则覆盖之。
```python
import os
```


# 高级数据结构

## deque

python的双向链表，使用标准库`collections`实现。

因`deque`在头部添加或删除的时间复杂度为O(1)，所以其提供`deque.appendleft`，`deque.popleft`等方法。

```python
from collections import deque

# 新建一个双链表
q = deque()
# 新建一个带长度限制的双链表，可实现只保存最近若干输入项
q = deque(maxlen=3)
```



## heapq

堆作为一种数据结构，很适合用来实现优先级队列。其典型应用场景为，从1亿个数里面找出最大或最小的100个数

```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
```

关于堆概念的更详细资料可见：

[Heap Data Structures](https://www.tutorialspoint.com/data_structures_algorithms/heap_data_structure.htm)



## defaultdict

默认字典可以对一个不存在的key设一个默认值，当之后访问该key，返回设置的默认值。

```python
# 普通字典
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
    
# 默认字典
from collections import defaultdict

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
```



## OrderDict

字典是一个hash表，其内部的数据是无序的。而有序字典可以保留字典键值的插入顺序。

有序字典的实现方式为，在key-value形态之外，还维护了一张链表。每个值之间通过指针，链接而成。也因此，其更占内存。

```python
# print 'Regular dict:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k, v in d.items():
    print k, v
"""
a A
c C
b B
e E
d D
"""

# print 'OrderedDict:'
from collections import OrderedDict
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k, v in d.items():
    print k, v
"""
a A
b B
c C
d D
e E
"""
```



## Counter

counter保存了元素的次数：将元素保存为字典的键，将次数保存为字典的值

`from collections import Counter`



## Namedtuple

元组为不可变列表，可以通过下标或切片的方式访问。而命名元组还可以通过属性的方式访问

```python
from collections import namedtuple
Person = namedtuple('Person', 'name age gender')
bob = Person(name='Bob', age=30, gender='male')
bob.age # 30
bob[0] # Bob
```

```python
# 实战代码，获取磁盘健康信息

DiskDevice = collections.namedtuple('DiskDevice', 'major_number\ minor_number device_name \
read_count read_merged_count \
read_sections time_spent_reading \
write_count write_merged_count \
write_sections time_spent_write \
io_requests time_spent_doing_io \
weighted_time_spent_doing_io')

with open("/proc/diskstats") as f:
    for line in f:
        if line.split()[2] == self.disk:
            # *号是对列表解引用，将self.disk指定的磁盘各值赋给DiskDevice
            return DiskDevice(*(line.split()))
```



## bisect

二分查找：bisect模块提供了高效的二分折半搜索算法，能够在一系列排好序的元素中搜寻某个值。需要注意的是，列表内容有序，是很重要的一个前提

```python
import bisect
import random
l = []
for i in range(5):
    item = random.randint(1, 100)
    bisect.insort(l, item)
print l # [9, 12, 16, 18, 60]
```



# 语句和语法

## Python基本语法

python中大量使用缩进规范代码块。所有复合语句，都是首行以冒号结尾，下一行嵌套的代码缩进。遗漏冒号是新手常犯的错误。

python里通常一行的结束就终止该语句。如果代码需要跨多行，推荐使用()，而不是\

```python
if (A==1 and
   B==2):
    pass
```



## 赋值、表达式和打印

赋值语句建立对象引用

变量名在首次赋值时自动创建

变量名在引用前必须先赋值

序列赋值模式时，需要`=`两边序列的元素数目相同

```python
a = 'ABC'
print a # ABC

a, b, c = 'ABC'
print a, b, c # A B C
```

序列赋值在for循环中也有效

```python
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
    
"""
(1, 2, 3)
(4, 5, 6)
"""
```

python3中还有扩展序列包，可以不需要`=`两边序列元素数目相同

```python
# Python 2
seq = [1, 2, 3, 4]
a, b, c, d = seq
a, b, c = seq # python2里面这样赋值则报错

#Python 3
seq = [1, 2, 3, 4]
a, *b, c = seq
#(1, [2, 3], 4) 赋值时先给没有*号的变量赋值，剩下多余的值全部给带*号的变量。不过此方法，变量b就成了数组。
```

多目标赋值时共享引用

增强型赋值

```python
X += Y
X = X + Y

L += [9, 10] # Mapped to L.extend([9, 10])
```

以单一下划线开头的变量名（\_X）不会被from module import * 语句导入

前后有下划线的变量名（\_X_），对解释器有特殊含义

以两个下划线开头，但结尾没有两个下划线的变量名是private

在交互模式下，单下划线（\_）保存了上次执行的结果

python的`print`默认输出到`sys.stdout`，python2可使用`print>>file, spam`的方式输出到指定文件。并且python2的`print`是一个关键字。若要像python3那样使用`print`函数，可在python2程序所有import前使用`from __future__ import print_function`



## if语句、while循环和for循环

三元表达式

```python
# 常规写法
if X:
    A = Y
else:
    A = Z

# 三元表达式写法
A = Y if X else Z
```

for循环更容易编写，效率更高，应该是我们首选的工具。

有很多工具帮助编写for循环：

- 内置的`range`函数返回一系列连续增加的整数，可作为for中的索引

- 内置的`zip`函数返回并行元素的元组列表，可于for循环遍历数个序列

  ```python
  L1 = [1, 2, 3, 4]
  L2 = [5, 6, 7, 8]
  zip(L1, L2) # [(1, 5), (2, 6), (3, 7), (4, 8)]

  for (x, y) in zip(L1, L2):
      print x, y, '--', x+y
      
  """
  1 5 -- 6
  2 6 -- 8
  3 7 -- 10
  4 8 -- 12
  """

  # zip还可用于字典的初始化
  keys = ['spam', 'eggs', 'toast']
  vals = [1, 3, 5]
  D = dict(zip(keys, vals))
  print D # {'toast': 5, 'eggs':3, 'spam': 1}
  ```

- 内置的`enumerate`可以产生偏移和元素，可用于for循环产生偏移

  ```python
  L = ['a', 'b', 'c', 'd']
  for index, item in enumerate(L, 1):
      print index, item
      
  """
  1 a
  2 b
  3 c
  4 d
  """
  ```



## 迭代器

迭代器即为实现了`__next__`方法的对象，迭代器只能迭代一次。在没有数据可返回时，返回`StopIteration`异常终止迭代。在使用`for`循环遍历可迭代对象时，其自动捕获异常，将其作为终止迭代的信号，不抛出给用户。

“可迭代对象”就是实现了迭代器协议的对象。

Python的内置工具（for循环，sum，min，max等）使用迭代器协议访问对象。

文件对象提供迭代器协议，而for循环使用迭代器协议访问文件，所以可以逐行访问文件。

```python
L = [1, 2, 3]

for x in L:
    print(x, end = ' ') # 1 2 3
    
I = iter(L)
while True:
    try:
        print(next(I), end = ' ')
    except StopIteration:
        Break
# 1 2 3
```

可以处理迭代器的内置函数：

```python
sum([1, 2, 3, 4, 5])
any(['spam', '', 'nice'])
all(['spam', '', 'nice'])
max([1, 2, 3, 4, 5])
min([1, 2, 3, 4, 5])
```

内置的`itertools`模块中，包含大量的函数，可以用来组合并操控迭代器。



## 文档

注释是给修改代码的人看的文档。

`dir`函数可以获取对象内所有属性、方法的列表。

`help`函数可以获取帮助文档，该函数调用`PyDoc`工具。

文档字符串`__doc__`出现在文件开端以及其中的函数和类的开头，文件和函数多行注释，一般用三重引号的字符串。



# 函数

## 函数基础

`global`：在函数内部修改全局变量

`yield`：生成器相关函数，将函数变成生成器。向调用者返回一个结果对象，但记住离开的地方。

```python
def squares(x):
    for i in range(x): yield i**2
```

`lambda`：一种迷你函数。其创建了一个对象，但将其作为结果返回。

```python
funcs = [ lambda x:x**2, lambda x:x**3]
```

函数基本格式：

```python
def <name> (arg1, arg2,..., argN):
    <statements>
    return <value> # 如果没有return，则返回None
```

函数定义是实时发生的，所以对于函数名来说，并没有什么特别之处，关键在于函数名所引用的那个函数对象

```python
def f():
    return 2 + 3

othername = f
print othername()
# 因为函数名f只是对函数对象的引用，所以我们可以对f赋值给其他变量名，再通过其它名字调用这个函数
```

所有在函数内部进行赋值的变量名，都默认为本地变量（局部变量）。



## 变量作用域

当我们在程序中使用变量名时，Python创建、改变或查找变量名都是在所谓的命名空间（一个保存变量名的地方）中进行的。

函数除了打包代码之外，还定义了一个全新的命名空间，一个函数的所有变量，都与函数的命名空间相关联。所以：

1. def内定义的变量名能够被def内的代码使用，不能在函数外部引用这样的变量名。
2. def之中的变量名与def之外的变量名，并不冲突。

函数定义了本地作用域，而模块定义了全局作用域。

Python预定义的模块可以使用`dir(__builtin__)`查看。

变量名引用分为三个作用域进行查找，首先是本地，之后是函数内，之后是全局，最后是内置。这里的三个作用域，指的是自定义的前三个作用域。

当在函数中使用未认证的变量名时，Python搜索四个作用域：

1. `L` 本地作用域
2. `E` 上一层结构中的本地作用域
3. `G` 全局作用域
4. `B` 内置作用域
5. 如果变量名在这次搜索中没有找到，Python就会报错

全局变量是位于模块顶层的变量名

全局变量如果在函数内部改变的话，必须先声明

全局变量在函数内部不经过声明，也可以引用

全局变量使得程序难以理解和使用，应尽量避免使用

插播`sys`标准库

```python
import sys
sys.argv # 获取python程序执行参数

sys.stderr.write('error message')
sys.exit(1)
# 上下两种方式作用一样。提示输入错误并退出程序
raise SystemExit('error message')
```

另外还有诸如将程序当作模块导入再访问达到修改全局变量的途径，或者通过`module = sys.modules['模块名']`间接引用模块再修改全局变量。

Python3的`nonlocal`类似于`global`，只不过修改的是嵌套作用域上层的变量。

内置函数`locals`可以看到函数内所有的变量

```python
x = 1
def f(a, b=1, c=2):
    global x
    y = 0
    print(locals())
    
f(0) # {'y': 0, 'a': 0, 'c': 2, 'b': 1}
```

内置函数`globals`可以看到全局命名空间的变量名。



## 函数的参数

函数的参数，是传递对象的引用。若对象可修改，修改对外部内部都可见。

位置参数，从左到右传入

关键字参数：通过参数名匹配

默认参数：为没有传入值的参数定义参数值

可变参数

Python3的keyword-only参数：参数必须按照名称传递

参数解包（\*，\*\*）

```python
def func(*name) # 匹配任意多的位置参数，python将其解析成元组
def func(**name) # 匹配任意多的关键字参数，python将其解析成字典
# 调用时使用如下方式，使用时需将*arg放在**kwargs之前
func(*args, **kwargs) #解引用
```

参数匹配算法：

1. 非关键字参数用位置匹配

2. 有关键字的通过名字匹配

3. 其它非关键字的参数都传给*name元组

4. 其他关键字参数传给**name字典

5. 没有赋值的参数用函数预设的默认值

   ```python
   # 位置和关键字传参
   def f(a, b, c):print a, b, c
   f(1,c=3,b=2) # 1 2 3

   # 参数默认值赋值
   def f(a, b=2, c=3):print a, b, c
   f(1) # 1 2 3
   f(1, c=6) # 1 2 6

   # 传递任意位置参数
   def f(*args):print args
   f(1) # (1,)
   f(1,2,3,4) # (1,2,3,4)
   L = [1, 2, 3, 4]
   f(L) # ([1, 2, 3, 4],)
   f(*L) # (1, 2, 3, 4)

   #传递任意关键字参数
   def f(**kwargs):print args
   f() # {}
   f(a=1, b=2) # {'a': 1, 'b': 2}
   d = dict(a=1, b=2, c=3)
   f(**d) # {'a': 1, 'c': 3, 'b':2}

   # 传递参数方式汇总
   def f(a, *args, **kwargs):
       print a, args, kwargs
   f(1,2,3,4,x=1,y=2,z=3) # 1 (2, 3, 4) {'y': 2, 'x': 1, 'z': 3}
   ```


函数的名字因为仅仅是一个名字，其背后代表的是对函数对象的引用。所以函数的名字可以用作函数的参数传入另一个函数，而被传递的参数，通常称之为“回调”，即callback。

```python
def minmax(callback, *args):
    res = args[0]
    for arg in args[1:]:
        if callback(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def greaterthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(greaterthan, 4, 2, 1, 5, 6, 3))
```




## 函数的高级话题

函数的设计概念：

1. 对于输入使用参数，对于输出使用return
2. 只有在真正必要的情况下使用全局变量
3. 不要改变可变类型的参数
4. 每个函数应该只有单一的、统一的目标（只做一件事）
5. 每个函数都应该相对较小
6. 避免直接改变另一个模块的变量

递归就是函数调用自己。

递归需要注意两点：递归深度和结束递归。

`lambda`的一般形式是关键字lambda，之后是一个或多个参数，紧跟的是一个冒号，之后是表达式：

`lambda argument1, argument2, … argument:expression using arguments`

`lambda`能够出现在Python语法不允许`def`出现的地方——例如，在一个列表常量中或者函数调用的参数中

`lambda`的主体是一个单个的表达式，而不是一个代码块

函数陷阱1：本地变量是静态检测的

```python
X = 99
def selector():
    print(X)
    X = 88
    
selector()
# 此时报错UnboundLocalError: local variable 'X' referenced before assignment。因为先编译后执行，编译认为X是局部变量，但是打印之前，局部变量X并没有被定义
```

函数陷阱2：默认值是可变对象

函数陷阱3：没有return的函数，只会得到None



## 生成器

Python对延迟提供了更多的支持——它提供了工具在需要的时候才产生结果，而不是立即产生结果。有如下方式制造生成器：

- 生成器函数：常规的def语句，但是使用`yield`语句一次返回一个结果。在每个结果之间，挂起并继续它们的状态

  ```python
  def gensquares(N):
      for i in range(N):
          yield i ** 2
          
  a = gensquares(5) 
  a # <generator object gensquares
  # 生成器产生了一个迭代器对象，一次产生一个结果。最后用for循环迭代出来。对于大的数据时，可以减少内存的使用
  a.next() # 0
  a.next() # 1
  a.next() # 4

  for item in gensquares(5):
      print item, # 0 1 4 9 16
  ```

- 生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

  ```python
  # 把实现列表推导的写法，放在一对圆括号中，就构成了生成器表达式
  [x ** 2 for x in range(4)] # [0, 1, 4, 9]
  (x ** 2 for x in range(4)) # <generator object <genexpr>
  list(x ** 2 for x in range(4)) # [0, 1, 4, 9]
  ```

生成器和常规函数是一样的，并且，实际上也是用常规的def语句编写，差别在于，创建生成器的时候，会自动实现迭代器协议，以便应用到迭代背景中（如for循环）

状态挂起：生成器函数和常规函数之间的主要代码不同之处在于，生成器yield一个值，而不是返回一个值。yield语句挂起该函数并再向调用者返回一个值，但是，**保留足够的状态以便之后从它离开的地方继续**

举例：用生成器改写直接返回列表的函数

```python
# 使用列表的方式
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            result.append(index)
    return result

print index_words('How old are you') # [0, 4, 8, 12]

# 使用生成器
def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            yield index
            
print list(index_words('How old are you')) # [0, 4, 8, 12]
```

- 使用生成器把收集到的结果放入列表返回给调用者更加清晰
- 由生成器函数所返回的那个迭代器，可以把生成器函数体中，传给`yield`表达式的那些值，逐次产生出来
- 无论输入量多大，生成器都能产生一系列输出，因为这些输入量和输出量，都不会影响它在执行时所消耗的内存




## 装饰器

Python2.4开始提供了装饰器（decorator），装饰器作为**修改函数**的一种便捷方式，为程序员编写程序提供了便利性和灵活性。

**装饰器本质上就是一个函数，这个函数接收其他函数作为参数，并将其以一个新的修改后的函数进行替换。**

```python
# 函数嵌套
def outer(x, y):
    def inner():
        return x ** y
    return inner
x = outer(2, 4)
x() # 16

# 装饰器
def sandwich(food="--ham--"):
    print food

def bread(other_func):
    def wrapper():
        print "</''''''\>"
        func()
        print "</______\>"
    return wrapper
    
sandwich_copy = bread(sandwich)
sandwich_copy()
"""
</''''''\>
--ham--
</______\>
"""

# 语法糖写法
def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "</______\>"
    return wrapper

@bread # 此语法糖的效果等同于第二个例子中最后两行代码
def sandwich(food="--ham--"):
    print food

sandwich()
"""
</''''''\>
--ham--
</______\>
"""
```

综上的例子可见，装饰器涉及到了如下的知识点：

- 函数嵌套
- 函数就是对象（函数对象），可以随意传递
- 语法糖：语言自身提供，用更加简便的方式表示某种行为

装饰器具体实例：检查参数，将检查功能与业务逻辑拆分

```python
# 一般写法
class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.get(food)
    
    def put_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.put(food)
    
# DRY写法
def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to get food")
        
class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)
    
    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)
    
# 装饰器语法糖写法
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)
    
    @check_is_admin
    def put_food(self, username, food):
        return self.storage.put(food)
```

装饰器的使用场景：

- 注入参数（提供默认参数，生成参数）
- 记录函数行为（日志、缓存、计时之类）
- 预处理/后处理（配置为上下文之类）
- 修改调用时的上下文（线程异步或者并行，类方法）

  ```python
  # Python官方示例
  # benchmark
  import time
  def benchmark(func):
      def wrapper(*args, **kwargs):
          t = time.clock()
          res = func(*args, **kwargs)
          print func.__name__,
          time.clock() -t
          return res
      return wrapper

  # logging
  def logging(func):
      def wrapper(*args, **kwargs):
          res = func(*args, **kwargs)
          print func.__name__, args, kwargs
          return res
      return wrapper

  # counter
  def counter(func):
      def wrapper(*args, **kwargs):
          wrapper.count = wrapper.count + 1
          res = func(*args, **kwargs)
          print "{0} has been used:{1}x".format(func.__name__, wrapper.count)
          return res
      wrapper.count = 0
      return wrapper

  @counter
  @benchmark
  @logging
  def reverse_string(string):
      return str(reversed(string))
  ```

装饰器的注意事项：

- 函数属性变化
  ```python
  def is_admin(f):
      def wrapper(*args, **kwargs):
          if kwargs.get("username") != 'admin':
              raise Exception("This user is not allowed to get food")
          return f(*args, **kwargs)
      return wrapper

  def foobar(username='someone'):
      """Do crazy stuff"""
      pass

  @is_admin
  def barfoo(username='someone'):
      """Do crazy stuff"""
      pass

  print foobar.__doc__ # Do crazy stuff
  print foobar.__name__ # foobar
  print barfoo.__doc__ # None
  print barfoo.__name__ # wrapper
  # 因为被装饰器修改，所以barfoo的函数属性有了变化。如果需要在使用装饰起i时，仍要获取原函数的相关属性，可以使用标准库import functools，并在def wrapper前@functools.wraps(func)
  ```

- 使用inspect获取函数参数
  ```python
  # 前面check_is_admin例子中装饰器使用kwargs.get获取username的参数。但实际上，对username传参即可以以位置方式传参，也可以以字典的方式传参。所以前面的例子有报错的可能。恰好python提供了标准库inspect，可以将装饰器所有获取到的参数转化为字典形式，再获取参数
  import functools
  import inspect
  def check_is_admin(f):
      @functools.wraps(f)
      def wrapper(*args, **kwargs):
          func_args = inspect.getcallargs(f, *args, **kwargs)
          if func_args.get('username') != 'admin':
              raise Exception("This user is not allowed to get food")
          return f(*args, **kwargs)
      return wrapper

  @check_is_admin
  def get_food(username, food="chocolate"):
      return "{0} get food: {1}".format(username, food)
  print get_food('admin') # admin get food: chocolate
  print get_food(username='admin') # admin get food: chocolate
  ```

- 多个装饰器的调用顺序

  ```python
  def makebold(fn):
      def wrapper():
          return "<b>" + fn() + "</b>"
      return wrapper
  def makeitalic(fn):
      def wrapper():
          return "<i>" + fn() + "</i>"
      return wrapper

  @makebold
  @makeitalic
  def hello():
      return "hello world"
  print hello() # <b><i>hello world</i></b>
  # 即相当于hello-copy = makebold(makeitalic(hello))。越靠近函数的地方越优先执行
  ```

- 给装饰器传递参数

  ```python
  """
  内层函数的参数是被装饰的函数的参数
  外层函数的参数是被装饰的函数
  如果需要给装饰器传递参数，则再加一层嵌套
  """
  import functools

  def timeout(seconds, error_message = 'Function call timed out'):
      def decorated(func):
          def _handle_timeout(signum, frame):
              raise TimeoutError(error_message)
          
          def wrapper(*args,  **kwargs):
              signal.signal(signal.SIGALRM, _handle_timeout)
              signal.alarm(seconds)
              try:
                  result = func(*args, **kwargs)
              finally:
                  signal.alarm(0)
              return result
          return functools.wraps(func)(wrapper)
      return decorated

  import time
  @timeout(1, 'Function slow: aborted')
  def slow_function():
      time.sleep(5)
  ```


装饰器的缺点：

- 装饰器新增于2.4版本，无法兼容之前的版本
- 装饰器经过封装，可能降低程序执行效率，但不明显
- cannot un-decorate a function
- 可能带来调试难度

更多Python装饰器资料可见：

[PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)



## 函数最佳实践

用生成器改写数据量较大的列表推导

```python
value = [len(x) for x in open('/tmp/my_file.txt')]
print value

it = (len(x) for x in open('/tmp/my_file.txt'))
# <generator object <genexpr>
print next(it)
print next(it)

# 1. 当输入的数据量较大时，列表推导可能会因为占用太多内存而出现问题
# 2. 由生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免了内存用量问题
```

需要清楚生成器的副作用——生成器只能迭代一次。若代码某一处对生成器对象进行了迭代访问，之后该对象将为空，不再可用。

用异常表示特殊情况，不要返回`None`

用数量可变的位置参数减少视觉杂讯。不过如果以后要增加新的位置参数，那就必须修改所有调用该函数的代码，扩展性不好。所以，数量可变的位置参数也要慎用

```python
# 使用元组
def log(message, values):
    pass
log('My number are', [1, 2])
log('Hi, there', [])

# 使用数量可变的位置参数
def log(message, *values):
    pass
log('My number are', 1, 2)
log('Hi, there')
favorites = [7, 33, 99]
log('Favorite colors', *favorites)

# 令函数接受可选的位置参数，能够使代码更加清晰。对于这里的第一个例子，即便没有需要打印的值，只是打印一条消息，也必须传入一个空的列表，这种写法既麻烦又显得杂乱，最好能让调用者在不必要时把第二个参数完全省略掉
```

用关键字参数来表达可选的行为

1. 以关键字参数来调用函数，能使读到这行代码的人更容易理解其含义

2. 可以在函数定义中提供默认值

3. 便于扩展

   ```python
   def remainder(number, divisor):
       return number % divisor

   print remainder(20, 7)
   print remainder(number=20, divisor=7)
   print remainder(number=20, 7) # ❌ 位置参数必须出现在关键字参数之前
   print remainder(20, number=7) # ❌ 每个参数只能指定一次
   ```

用None赋值给动态默认值

1. 参数的默认值，只会在程序加载模块并读到本函数的定义时评估一次，对于{}或[]等动态的值，这可能会导致奇怪的现象

2. 对于以动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为None，并提供文档

   ```python
   def grow(A, B=[]):
       B.append(A)
       return B
   grow(1) # [1]
   grow(1) # [1, 1]
   grow(1) # [1, 1, 1]
   ```




## 练手

1. 熟悉`ConfigParser` 模块和`argparse`模块，通过配置文件和命令行参数，指定连接数据库的参数

2. Scrabble challenge

3. 练习老师课堂上的案例，自动配置config文件

4. 实现一个拼写检查器spelling corrector




# 模块

## 模块的宏伟蓝图

为什么使用模块——代码重用、系统命名空间的划分、实现共享服务和数据

Python程序架构

- 启动的那个Python文件称之为顶层文件
- 模块文件就是工具的库，我们导入模块，获取它的属性并使用它的工具

`import`如何工作

- 导入是运行时的运算，程序第一次导入，会执行一下三步：
  1. 找到模块文件
  2. 编译成字节码（pyc文件）
  3. 执行模块的代码来创建其所定义的对象
- Python把载入的模块存储到一个名为`sys.modules`的表中，并在一次导入操作的开始检查该表，如果模块不存在，将会启动一个三个的过程来载入模块。
  1. 搜索
  2. 编译
  3. 运行

模块搜索路径

1. 程序的主目录
2. `PYTHONPATH`目录（环境变量）
3. 标准链接库目录
4. 任何`.pth`文件的内容



## 模块代码编写基础

模块的创建

- 定义一个Python文件，编写代码，就是一个Python模块
- 模块在Python中会变成变量（一个变量对象），因此，需要遵循普通变量名命名规则

模块的使用

- `import`语句

- `from`语句

- `from *`语句
  ```python
  import module1 # get module
  from module1 import printer # get an export
  from module1 import * # get all exports
  ```

- 导入只发生一次

- `import`和`from`是赋值语句

  - `import`将整个模块对象赋值给一个变量
  - `from`将一个或多个变量名赋值给另一个模块中的同名对象（函数参数传递），修改不可变对象不起作用，修改可变对象可能有副作用

- 文件间的变量名改变
  ```python
  import small
  small.x = 42 # 这里small中x的值会被修改成42

  from small import x, y
  x = 42 # 这里只是赋值给另一个同名对象，所以不会修改small中的x
  ```


`from`语句陷阱

- 多个模块具有同名函数或变量
- 导入模块和当前模块有同名函数或变量

模块命名空间

- 模块就是命名空间，而存在于模块之内的变量名，就是模块对象的属性
  - 模块语句会在首次导入时执行
  - 顶层的赋值语句（不存在与`def`或`class`语句内）会创建模块属性，赋值的变量名会存在模块的命名空间内
  - 模块的命名空间能通过`__dict__`或`dir`查看属性
  - 模块是一个独立的作用域（本地变量就是全局变量）
- 作用域：模块程序代码绝对无法看见其他模块内的变量名，除非明确地进行导入
- 命名空间嵌套：命名空间不会向上嵌套，但是可以发生向下嵌套



## 模块包

除了模块名以外，导入也可以指定目录路径。Python代码的目录就称为包，因此，这类导入就称为包导入

包导入是把计算机上的目录变成另外一个Python命名空间，而属性就是子目录或目录下的模块文件

```python
# 如果我们要在dir0目录下进行包导入，则
import dir1.dir2.mod
"""
dir0必须包含在sys.path
dir1和dir2文件夹中，都必须包含__init__.py文件
dir0不需要__init__.py文件
"""
```

为什么需要包导入：包让导入更具有信息性

包相对导入

- 相对导入只适用于包内导入

- 相对导入只适用于`from`语句

  ```python
  from system.section.mypkg import string
  from . import string
  ```

- 相对导入中的“.”用来表示包含文件的包目录

- 相对导入中的“..”用来表示当前包的父目录

  ```python
  # 例：位于模块A.B.C中的代码要进行导入
  from . import D # imports A.B.D(. means A.B):导入整个D
  from .. import E # import A.E(.. means A):导入整个E

  from .D import X # imports A.B.D.X(. means A.B):导入D中的X
  from ..E import X # imports A.E.X(.. means A.E):导入E中的X
  ```




## 高级模块话题 

在模块中隐藏数据，最小化`from *`的破坏
1. 把下划线放在变量名前面，例如`_X`，可以防止客户端使用`from  *`语句导入模块名时，把其中的那些变量名复制出去
2. 模块顶层把变量名的字符串列表赋值给变量`__all__`，可以达到`_X`命名管理的隐藏效果。具体可参考`/usr/lib64/python2.7/os.py`

启用以后的特性，可能破坏现有代码语言方面的变动会不断引入。一开始，是以扩展的方式出现，默认是关闭的，可以启用这类扩展：例如`from __future__ import “featurename”`

`__name__`和`__main__`

- 每一个模块都有一个名为`__name__`的属性，Python会自动设置该属性
  - 如果文件是以顶层程序文件执行，在启动时，`__name__`就会自动设置为字符串`__main__`
  - 如果文件被导入，`__name__`就会设置为模块名
- 模块可以自己检测`__name__`，以确定自己是在被执行还是被导入。这样可以在写模块时，定义`__main__`完成自测模块功能。

修改模块搜索路径

- 模块搜索路径是一个目录列表，可以通过环境变量`PYTHONPATH`进行定制

- Python本身也可以通过修改`sys.path`增加搜索目录

  ```python
  import sys
  import os
  print sys.path # ['', '/usr/bin', '/usr/lib/python2.7...
  os.path.realpath('.')
  sys.path.append(os.path.realpath('.'))
  ```

`as`扩展：`import`语句和`from`语句都可以扩展，让模块可以在脚本中给予不同的变量名

```python
from modulename import name
import modulename as name

try:
    import MySQLdb as db
except ImportError:
    import pymysql as db
```

模块是对象，可以通过`__dict__`暴露自己的属性。也可以写程序，来管理这些属性，一般称这样的程序为metaprogram（元编程）。因为我们写的程序，能够在其他程序之上工作，所以，也叫作内省（introspection）

```python
# 假设模块内有名为name的属性
M.name
M.__dict__['name']
sys.modules['M'].name
getattr(M, 'name')
```

模块设计理念：

- 总是在Python的模块内编写代码
- 模块耦合要降低到最低：全局变量
- 最大化模块的粘和性：统一目标
- 模块不应该去修改其他模块的变量

模块陷阱：顶层代码的语句次序很重要

- 当模块首次导入时，Python会从头到尾执行语句：
  - 在导入时，模块文件顶层的程序文件（不在函数内），一旦Python运行至此，就会立刻执行。因此，该语句无法引用该位置后面的变量和函数
  - 位于函数主体内的代码直到函数被调用后才会运行，因为函数内的变量名在函数实际执行前都不会解析，通常可以引用文件内任意地方的变量

`from`复制变量名，而不是连接

```python
# nested1.py
X = 99
def printer():
    print X
    
# nested2.py
from nested1 import X, printer
X = 88
printer() # 99

# nested3.py
import nested1
nested1.X = 88
nseted1.printer() # 88 但是并不推荐这样的方式，因为这种情况修改了模块nested1的变量
```

`from *`会让变量语意模糊

- `from *`可能会意外的覆盖了作用域内已使用的变量名
- 如果有多个`from *`，且有同名的对象（变量、函数、类），你在使用的时候，很难确定对象来自哪里
- 要避免这个问题的方法，即不要这么做

递归形式的`from`导入无法工作

```python
# recur1.py
X = 1
import recur2
Y = 2

# recur2.py
from recur1 import X
from recur1 import Y
# 变量名Y是在导入recur1以后才赋值的，这时候import Y，Y还不存在
```



## 补充一些开源库

系统管理库`psutil`

- `cpu_percent`返回当前cpu利用率百分比
- `cpu_count`获取逻辑或物理cpu的个数
- `virtual_memory`内存占用情况
- `disk_partitions`硬盘分区信息
- `disk_usage`分区或目录的使用情况
- `pids`当前运行的进行列表
- `pid_exists`检查进程是否存在
- `Process(memory_info cmdline kill)`管理进程

邮件发送库`yagmail` [Github地址](https://github.com/kootenpv/yagmail)

```python
import yagmail
yag = yagmail.SMTP()
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('to@someone.com', 'subject', contents)
```



## 练手

获取系统信息，发邮件

写一个装饰器，能够记录函数开始运行和结束运行，再修改该装饰器，传递一个参数给装饰器，表明是谁调用了这个函数



# 类

## 类的概念

OOP(Object Oriented Programming)即面向对象编程，可以分解代码，把代码的冗余度降至最低。并且，可以通过定制现有的代码来编写新的程序，而不是原处修改

类就是一些函数的包，这些函数大量使用并处理内置对象

在Python中，OOP完全是可选的，并且在初期学习阶段，不需要使用类

合理使用类，能够大量减少开发时间

Python中的类，包含三部分知识：

1. 类的概念
2. 类的语句
3. 运算符重载







## 类代码编写基础





## 实例





## 深入细节







## 运算符重载





## 高级主题









# 异常





# 实战

To be continued



# 爬虫

To be continued



# Flask入门

## Flask基本介绍

我们先来看一下`Flask`官方提供的Demo

```python
from flask import Flask
app = Flask(__name__)   # 导入Flask类，这个类的实例将会是我们的WSGI应用程序
						# 接下来，我们创建一个该类的实例，第一个参数是应用						  模块或者包的名称
@app.route('/')			# 我们使用route()装饰器告诉Flask，什么样的URL触						发我们的函数，这个函数的名字也在生成URL时被特定的						  函数采用，这个函数返回我们想要显示在用户浏览器中的						   信息
def hello_world():
    return 'Hello World!'

if __name__ == '__main__': # 最后使用run()函数让应用运行在本地服务器
    app.run()
```

基于上面的代码，可以试图追溯，Flask是如何工作的。而在这之前，我们需要知道以下几个概念：

- `WSGI`是什么
  - Python Web服务器网关接口，为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口
  - 在`WSGI`出现之前，Web应用框架的选择将限制可用的Web服务器的选择，反之亦然：`WSGI`统一了Web服务器和Web框架之间的约定
  - 也就是说，在Python的世界里，通过`WSGI`约定了Web服务器怎么调用Web应用程序的代码，Web应用程序需要符合什么样的规范，只要Web应用程序和Web服务器都遵守`WSGI`协议。那么，Web应用程序和Web服务器就可以随意的组合，这就是`WSGI`存在的理由。
  - `WSGI`为Web服务器与Web应用程序或应用框架之间的一种低级别借口，直接使用低级别的接口，会使编程难度陡增，也不易于维护。遂出现了众多Web框架。
  - 注：`WSGI`是一种协议，另有`uwsgi`也是一种协议。而`uWSGI`则是实现了`uwsgi`和`WSGI`两种协议的Web服务器
- `Jinja2`是什么
  - `Jinja2`是一个功能齐全的模板引擎，可以将业务逻辑和表现逻辑分离
- `Werkzeug`是什么
  - `Werkzeug`是一个`WSGI`工具包，它可以作为Web框架的底层库。
  - 如果我们自己写Python框架，也可以单独使用`Werkzeug`
- `Flask`是什么
  - `Flask`是一个依赖`Jinja2`模板和`Werkzeug`的`WSGI`服务的Web框架
  - `Werkzeug`只是工具包，其用于接受`http`请求并对请求进行预处理，然后出发`Flask`框架
  - 开发人员基于`Flask`框架提供的功能对请求进行相应的处理，并返回给用户
  - 如果要返回给用户的内容比较复杂，需要借助`Jinja2`模板来实现对模板的处理。将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器




路由和视图:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

客户端（例如Web浏览器）把请求发送给Web服务器，Web服务器再把请求发送给Flask程序实例。程序实例需要知道对每个URL请求运行哪些代码，所以保存了一个URL到Python函数的映射关系。处理URL和函数之间关系的程序称为**路由**。

在Flask程序中定义路由最简便的方式，是使用程序实例提供的`app.route`装饰器，把修饰的函数注册为路由。

像`hello_world()`这样的函数称为视图函数（view function）。视图函数返回的响应可以是包含HTML的简单字符串，也可以是复杂的表或`JSON`串。



调试模式:

`Flask`开发过程中，可以打开调试模式。即在`app.run`函数里增加参数`debug=True`。如此可以在修改代码时，自动reload代码。



配置文件管理:

- 复杂的项目需要配置各种环境，如果配置项比较少，可以直接在代码中硬编码

  ```python
  from flask import Flask
  app = Flask(__name__)
  app.confg['DEBUG'] = True
  ```

- `app.config`是`flask.config.Config`类的实例，继承自Python内置数据结构`dict`。所以，可以像字典一样使用

  ```python
  app.config.update(DEBUG=True, SECRET_KEY='...')
  ```

- 如果配置项很多，应该使用配置文件

- 常用有如下三种方式加载配置文件

  - 通过模块加载

    ```python
    import settings
    app.config.from_object(settings)
    ```

  - 通过文件名字加载

    ```python
    app.config.from_pyfile('settings.py', slient=True)
    ```

  - 通过环境变量加载

    ```shell
    > export YOURAPPLICATION_SETTINGS='settings.py'
    ```

    ```python
    app.config.from_server('SETTINGS')
    ```




动态URL:

要给URL添加变量部分，妳可以把这些特殊的字段标记为\<variable_name>，这个部分将会作为命名参数传递到你的函数。还可以用\<converter:variable_name>指定一个可选的转换器

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id
```



唯一URL:

`Flask`的URL规则基于`Werkzeug`的路由模块。这个模块背后的思想时基于`Apache`以及更早的`HTTP`服务器主张的先例，保证优雅且唯一的URL

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

虽然它们看起来着实相似，但它们结尾斜线的使用在URL定义中不同。第一种情况下，指向projects的规范URL尾端有一个斜线。这种感觉很像在文件系统中的文件夹。访问一个结尾不带斜线的URL会被`Flask`重定向到带斜线的规范URL去

第二种情况的URL结尾不带斜线，类似`UNIX-like`系统下的文件的路径名。访问结尾带斜线的URL会产生一个`404 Not Found`错误

这个行为使得在遗忘尾斜线时，允许关联的URL接任工作，与`Apache`和其他的服务器行为并无二异。此外，也保证了URL的唯一，有助于避免搜索引擎索引同一个页面两次



生成URL:

你可以用`url_for()`来给指定的函数构造URL。它接受函数名作为第一个参数，也接受对应URL规则的变量部分的命名参数。未知变量部分会添加到URL末尾作为查询参数

反向构建通常比硬编码的描述性更好。更重要的是，它允许你一次性修改URL，而不是到处边找边改

URL构建会转义特殊字符和`Unicode`数据，免去你很多麻烦

如果你的应用不位于URL的根路径（比如，在/myapplication下，而不是/），`url_for()`会妥善处理这个问题

```python
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(): pass

with app.test_request_context():
	print url_for('index')	# /
    print url_for('login')	# /login
	print url_for('login', next='/')	# /login?next=%2F
	print url_for('profile', username="John Doe")	# /user/John%20Doe
```



HTTP方法:

默认情况下，路由只回应`GET`请求，但是通过`route()`装饰器传递`methods`参数可以改变这个行为

如果存在`GET`，那么也会替你自动地添加`HEAD`，无需干预

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```



静态文件:

动态Web应用也会需要静态文件，通常是`CSS`和`JavaScript`文件。理想状况下，你已经配置好Web服务器来提供静态文件，但是在开发中，Flask也可以做到。只要在你的包中或是模块的所在目录创建一个名为`static`的文件夹，在应用中使用`/static`即可访问

给静态文件生成URL，使用特殊的`'static'`端点名

```python
url_for('static', filename='style.css')
```



模版渲染:

`Flask`继承了`Jinja2`来渲染HTML

```python
from flask import render_template  # Flask使用render_template集成Jinja2

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```



访问请求数据:

对于Web应用，与“客户端发送给服务器的数据”交互至关重要。在Flask中由全局的`request`对象来提供这些信息

你可以通过args属性来访问URL中提交的参数(?key=value)

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    searchword = request.args.get('key', '')
```



Flask的上下文:

为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。有了上下文，就可以写出厦门的视图函数

```python
from flask import request
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
```

注意，在这个视图函数中我们如何把`request`当作全局变量使用。事实上，`request`不可能是全局变量。试想，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，每个线程看到的`request`对象必然不同。`Flask`使用上下文让特定的变量在一个线程中全局可访问，与此同时却不会干扰其他线程。

- `current_app`：
  - 程序上下文——当前激活程序的程序实例
- `g`：
  - 程序上下文——处理请求时用作临时存储的对象，每次请求都会重设这个变量
- `request`：
  - 请求上下文——请求对象，封装了客户端发出的HTTP请求中的内容
- `session`：
  - 请求上下文——用户会话，用于存储请求之间需要“记住”的值的词典



Cookies:

你可以通过`cookies`属性来访问Cookies，用响应对象的`set_cookie`方法来设置Cookies。请求对象的`cookies`属性是一个内容为客户端提交的所有Cookies的字典

```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # 用cookies.get(key)的方式替代cookies[key]获取cookie，可以避免在cookie没有值的时候发生KeyError
    
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```



重定向和错误:

你可以用`redirect()`函数把用户重定向到其他地方。放弃请求并返回错误代码，用`abort()`函数

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_excuted()
```



错误处理:

默认情况下，错误代码会显示一个黑白的错误页面。如果你要定制错误页面，可以使用`errorhandler()`装饰器

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```



响应对象:

视图函数的返回值会被自动转换为一个响应对象。如果返回值是一个字符串，它被转换为该字符串为主体的、状态码为`200 OK`的、MIME类型是`text/html`的响应对象

`Flask`处理响应对象的方法是

- 如果返回的是一个合法的响应对象，它会从视图直接返回
- 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建
- 如果返回的是一个元组，则元组中的元素可以提供额外的信息

```python
# 返回元组
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

# 返回响应对象
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```



Sessions:

`session`对象允许你在不同请求间存储特定用户的信息。它是在Cookies的基础上实现的，并且对Cookies进行密钥签名。这意味着用户可以查看你的Cookies内容，但却不能修改它，除非用户知道签名的密钥。

要使用会话，你需要设置一个密钥

```python
# 使用session
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

# session管理
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return """xxx"""

@app.route('logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
app.secret_key = 'miyue'
```



消息闪现:

```python
from flask import Flask, flash...
```



日志记录:

从Flask 0.3开始，Flask就已经预置了日志系统

```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```



命令行工具:

直接执行`flask --help`查看输出

Flask从0.11开始提供了命令行工具，不再需要`Flask-script`扩展

```python
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')
```



# 深入浅出Jinja2

## 模版渲染

为什么需要模版：

- 把业务逻辑和页面逻辑混在一起会导致代码难以理解和维护
- 假设要为一个大型表格构建HTML代码，表格中的数据由数据库中读取的数据以及必要的HTML字符串连接在一起。在代码中拼接HTML简直是噩梦，并且，给维护代码的人极大的心理负担
- 把页面逻辑移到模版中能够提升程序的可维护性
- 模版是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。**使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染**



在Flask中使用Jinja2:

- 可以使用Flask提供的`render_template`函数来渲染模版
- 我们要做的就是将模版名和想作为关键字的参数传入模版的变量
- `render_template`函数的第一个参数是模版的文件名，随后的参数都是键值对，表示模版中变量对应的真实值

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

- Flask会自动在`templates`文件夹里寻找模版
- 需要做的一切就是将模版名和你想作为关键字的参数传入模版的变量

```shell
/application.py
/templates
	/hello.html
```

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```



Flask使用Jinja2总结:

- Flask集成了Jinja2模版引擎
- Flask默认使用Jinja2模版引擎（也可以很方便的使用其他引擎，如Mako）
- Flask集成Jinja2的方式
  - 提供了`render_template`函数
  - 默认在templates文件夹下寻找模版



Jinja2入门:

- 模版仅仅是文本文件，它并没有特定的扩展名，`.html`或`.xml`都是可以的
- 模版包含HTML标签、控制结构、变量和表达式
- 对于Python的Web开发来说，Jinja2就是简单的Python + HTML



Jinja2的语句:

```jinja2
{% %}  # 控制结构
{{ }}  # 变量取值
{# #}  # 注释

{# note: disabled template because we no longer use this
	{% for user in users %}
		...
	{% endfor %}
#}
```



Jinja2中的变量:

模版中使用的{{ }}结构表示一个变量，它是一种特殊的占位符，告诉模版引擎这个位置的值从渲染模版时使用的数据中获取

Jinja2能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象

```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a vraible index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```



Jinja2中的过滤器:

变量可以通过“过滤器”修改，过滤器与变量用管道(|)分割

多个过滤器可以链式调用，前一个过滤器的输出会被作为后一个过滤器的输入

过滤器可以理解为Jinja2里面的内置函数和字符串处理函数

| 过滤器名       | 说明                    |
| ---------- | --------------------- |
| safe       | 渲染值时不转义               |
| capitalize | 把值的首字母转换成大写，其他字母转换成小写 |
| lower      | 把值转换成小写形式             |
| upper      | 把值转换成大写形式             |
| title      | 把值中每个单词的首字母都转换成大写     |
| trim       | 把值的首尾空格去掉             |
| striptags  | 渲染之前把值中所有的HTML标签都删掉   |



Jinja2的if 控制结构:

Jinja2中if 语句可类比Python中的if语句。在最简单的形式中，你可以测试一个变量是否未定义，为空或false

像在Python中一样，用`elif`和`else`来构建多个分支

```jinja2
{% if users %}
<ul>
{% for user in users %}
<li>{{ user.username|e }}</li>
{% endfor %}
</ul>
{% endif %}

{% if kenny.sick %}
	Kenny is sick.
{% elif kenny.dead %}
	You killed Kenny.You bastard
{% else %}
	Kenny looks ok --- so far
{% endif %}
```



Jinja2的for控制结构:

```jinja2
# 遍历序列中的每项
<h1>Members</h1>
<ul>
{% for user in users %}
  <li>{{ user.username |e }}</li>
{% endfor %}
</ul>

# 迭代dict
<dl>
{% for key, value in d.iteritems() %}
	<dt>{{ key|e }}</dt>
	<dd>{{ value|e }}</dd>
{% endfor %}
</dl>
```

Jinja2还提供了一些特殊变量，方便使用

| 变量             | 描述                 |
| -------------- | ------------------ |
| loop.index     | 当前循环迭代的次数（从1开始）    |
| loop.index0    | 当前循环迭代的次数（从0开始）    |
| loop.revindex  | 到循环结束需要迭代的次数（从1开始） |
| loop.revindex0 | 到循环结束需要迭代的次数（从0开始） |
| loop.firse     | 如果是第一次迭代，为True     |
| loop.last      | 如果是最后一次迭代，为True    |
| loop.length    | 序列中的项目数            |
| loop.cycle     | 在一串序列              |

```jinja2
{% for todo in todo_list %}
   <tr class="info">
      <td>{{ loop.index }}</td>
      <td>{{ todo['title'] }}</td>
      <td>{{ todo['status'] }}</td>
      <td>{{ todo['create_time'] }}</td>
   </tr>
{% endfor %}
```



Jinja2的宏控制结构:

```jinja2
# 定义
<!-- 定义宏，类似于函数 -->
{% macro hello(name) %}
    Hello {{ name }}
{% endmacro %}

# 使用
<!-- 使用宏 -->
{% import 'macro.html as macro %}
<p>{{ macro.hello('world') }}</p>
```





# Flask进阶





# 自动化运维

To be continued