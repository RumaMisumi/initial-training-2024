a=1.2 + 3.8
print(f"aの値は{a}です。型は{type(a)}です")
b=10 // 100
print(f"bの値は{b}です。型は{type(b)}です")
c=1 >= 0
print(f"cの値は{c}です。型は{type(c)}です")
d='Hello World' == 'Hello World'
print(f"dの値は{d}です。型は{type(d)}です")
not 'Chainer' != 'Tutorial'
e=all([True, True, False])
print(f"eの値は{e}です。型は{type(e)}です")
f=any([True, True, False])
print(f"fの値は{f}です。型は{type(f)}です")
g=abs(-3)
print(f"gの値は{g}です。型は{type(g)}です")
#h=2//0
print(f"hの値は0で割れないのでエラーがでる")