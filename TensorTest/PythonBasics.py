#Basic Python Varibales & Operators
from math import sqrt as squareroot
from numpy import multiply as mult
print(5+2 ,' Float div :   ', 7/3 ,' Round off quotient ' , 7//3 )
wordarray=['t','h','i','s',' ','i','s',' ','t','e','s','t']
word='this is test'
print ('slice  : --> ' + word[:4] , ' give start -->' ,word[2:],'Start end -->' , word[2:5],'Last 4 -> ', word[-4:])
print (' length : ', len(word))
print(wordarray[:5])
print(squareroot(5))
print (mult(2,3))
print('---- Fibinacci ----')
#print fibonacci
limit =10
start =1
start, b = 0, 1
while start < limit:
    print(start)
    start,b = b ,start+ b

