#TYPECASTING MEANS CHANGING ONE DATA TYPE TO ANOTHER

#STRING------->INTEGER
a="10"
b=int(a)
print(b,type(b))

#INTEGER------->FLOAT
a=5
b=float(a)
print(b,type(b))

#TUPLE--------->LIST
t=(4,5,6)
lst=list(t)
print(lst)

#WE CAN NOT ADD THE STRING AND INTEGER
a=1
b="2"
sum=a+b
print(sum)                         #o/p------>ERROR
