import sys

""" Çoklu satır yorumları
1. cümle
2. cümle
3. cümle
"""
# tek cümlelik yorum satırı
print("--------------------------------------------------------------")
##  Degiskenler
# Integer
x = 5
print("Sayı:",x,type(x))

# Float
x = 5.5
print("Ondalıklı Sayı:",x,type(x))

# String
x = "Hello World"
x = 'Hello World'
print("String:",x,type(x))

# Boolean 0 - 1 
x = True
x = False

print("Boolean:",x,type(x))

print("--------------------------------------------------------------")
# Değişken isimlendirmelerine.

# Değişken isimleri rakam ile başlayamaz.
degisken_ismi = 5

# Camel Case
degiskenIsmi = 5
# Snake Case
degisken_ismi = 5
# Pascal Case 
DegiskenIsmi = 5
print("--------------------------------------------------------------")
#Değişkenlerde tür dönüşümü
banka_bakiye = 1000
print(type(banka_bakiye))

banka_bakiye = str(banka_bakiye)
print(type(banka_bakiye))

onsekizYasindaMi = True
print(type(onsekizYasindaMi))

onsekizYasindaMi = int(onsekizYasindaMi)
print(type(onsekizYasindaMi))
print("--------------------------------------------------------------")
#Değişkenlerin boyutları
banka_bakiye = 1000 ** 5
print("Banka bakiyesi:", sys.getsizeof(banka_bakiye), "bytes")

banka_bakiye = 1000.0 ** 5
print("Banka bakiyesi:", sys.getsizeof(banka_bakiye), "bytes")

onsekizYasindaMi = False
print("Onsekiz yasinda mi:", sys.getsizeof(onsekizYasindaMi), "bytes")

# Python büyük/küçük harf duyarlıdır.
print("--------------------------------------------------------------")
degisken_ismi = 5
Degisken_ismi = 10
print(degisken_ismi)
print(Degisken_ismi)
