prime=[2,3,5,7,11,13,17,19]
print(max(prime))

# function

def find_max(li):
    if len(li) == 0:   # list value na thakle none print hobe
        return None
    max_item = li[0]
    for item in li:
        if item > max_item:
            max_item = item
    return max_item
prime = [2,3,5,7,11,13,17,19]
print(find_max(prime))       


prime = [2,3,5,7,11,13,17,19]
print(17 in prime)
print(18 in prime)

# true or false print korbe
def find_item (li,x):
    for item in li:
       if x == item:
          return True
    print("could not find: ", x)
    return False

prime = [2,3,5,7,11,13,17,19]
print(find_item(prime,11)) 

def find_item (li,x):
    for item in li:
       if x == item:
          return True
    print("could not find: ", x)
    return False

prime = [2,3,5,7,11,13,17,19]
print(find_item(prime,10))  

def find_item (li,y):  #local variable
    y = 19
    for item in li:
       if x == item:
          return True
    print("could not find: ", y)
    return False

prime = [2,3,5,7,11,13,17,19]
x = 20
print(find_item(prime,x)) 
print("x =",x)