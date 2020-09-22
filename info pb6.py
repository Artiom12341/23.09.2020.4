
n=9875
#ultima cifra
print(n%10)
#penultima cifra
print(n%100//10)
#restul si catul impartirei la 9
print(n/9)
print(n%9)
#suma cifrelor acestui numar
a=((n-(n%1000))//1000)
b=((n%1000)//100)
c=(n%100//10)
d=(n%10)
a=a+b+c+d
print(a)
#rasturnatul acestui numar
print((n%10),(n%100//10),((n%1000)//100),((n-(n%1000))//1000),sep='')
