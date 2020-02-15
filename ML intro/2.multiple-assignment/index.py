## Python functions can return multiple result

def split_parameter(a):
    return a+1, a-1


b,c = split_parameter(50)
print(b,c)


e, f = 100/5,100/20

print(e,f)