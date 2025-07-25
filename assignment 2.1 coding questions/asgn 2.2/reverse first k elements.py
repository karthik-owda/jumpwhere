#Reverse first K elements of Queue using stack
def reverse_first_k_elements(k,q):
    stack=[]
    for i in range(k):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    for i in range(len(q)-k):
        q.append(q.popleft())
    return q
