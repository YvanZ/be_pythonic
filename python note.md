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
f = "result(0)"

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





# 类





# 异常





# 实战

To be continued



# 爬虫

To be continued



# Flask入门





# Flask进阶





# 自动化运维

To be continued