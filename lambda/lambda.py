lambda5 = lambda x: x+5
lambda7 = lambda x: x+7

def addNum(val,func):
    return func(val)
print(addNum(3,lambda7))
print(addNum(12,lambda5))
