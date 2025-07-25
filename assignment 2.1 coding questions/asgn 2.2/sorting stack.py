#Sorting a Stack
def sortstack(stack):
    tmpstack=[]
    while stack:
        num=stack.pop()
        while (tmpstack and tmpstack[-1]<num):
            stack.append(tmpstack.pop())
        tmpstack.append(num)
    return tmpstack
