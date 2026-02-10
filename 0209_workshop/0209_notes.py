# 간단한 스택
top = -1
stack = [0]*10

# push 1
top += 1
stack[top] = 1
# push 2
top += 1
stack[top] = 2
# push 3
top += 1
stack[top] = 3

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])


st = []
st.append(1) # push 1
st.append(2) # push 2
st.append(3) # push 3
print(st.pop())
print(st.pop())
print(st.pop())