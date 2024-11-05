import numpy as np
#必須の引数は、第一引数の配列の形状(shape)を指定するshapeだけです。他の2つの引数については、dtypeは要素のデータ型を、orderはデータの保存の仕方を指定します
#すべての要素が0
masuo0=np.zeros((3, 3)) #np.zeroは全部の要素を0とする配列を生成
print("3-3(1)",masuo0)

#すべての要素が1
masuo1= np.ones((3, 3))
print("3-3(2)",masuo1)

#-1から1の間のランダムな要素
masuo11=np.random.random((3,3))*2-1#(0,1)に対して*2で(0,2).-1をして(-1,1)
print("3-3(3)",masuo11)

#対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0
real_masuo= np.eye(3) * 2#np.eye(3)は、3*3で対角で要素1になる。二倍すれば、2になる。
print("3-3(4)",real_masuo)
