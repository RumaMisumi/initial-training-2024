a = [str(i) for i in range(100)] #str(i)にrange(100)が代入されている
s = " ".join(a)#リストの要素をjoinで結合
print(f"5-(1):{s}")

s = "{0:.9f}".format(1.0 / 7.0)#formatは、小数点以下を表示できる。
print(f"5-(2):{s}")