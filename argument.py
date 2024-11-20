# positional argument

def my_func(a,b,c):
    result= a*3+b*2+c
    return result
a,b,c = 10,20,30
s = my_func(a,b,c)
print(s)  


def my_func(a,b,c):
    result= a*3+b*2+c
    return result
a,b,c = 10,20,30
s = my_func(b,a,c)
print(s) 


def my_func(a,b,c):
    result= a*3+b*2+c
    return result

s = my_func(10,20,30) #position
print(s)   

#keyword argument

def my_func(a,b,c):
    result= a*3+b*2+c
    return result

s = my_func(a=15,b=20,c=30) #key
print(s) 


# defolt

def my_func(a,b,c=0):
    result= a*3+b*2+c
    return result

s = my_func(a=15,b=20) #key
print(s) 

def my_func(a=0,b,c=0):
    result= a*3+b*2+c
    return result

s = my_func(b=20) #key
print(s) 