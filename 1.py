
x = input("Enter the expression\n")

stack = []  #initialize list named stack
balanced = True

for i in x:
    if i == "(":
        stack.append("(")  #push to stack if open parantheses

    else :
        if len(stack) == 0:

            balanced = False
        else :
            stack.pop()     #pop from stack if closed parantheses provided stack is not empty

if len(stack) == 0 and balanced:
    print("Balanced")

else:
    print("not balanced")

