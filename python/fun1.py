sum1=lambda x,y: x + y
print("sum=",sum1(3,5))

def small(a,b):
    if(a<b):
        return a
    else:
        return b
sum=lambda x,y:x+y
diff=lambda x,y:x-y
print("smaller of two number",small(sum(-3,-2),diff(-1,2)))