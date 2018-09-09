x = input("Enter the expression\n")

stack = []  #initialize list named stack
balanced = True
index = 0   #index counter for list

def matchedpair( x1, x2):   #Returns Boolean Values if the arguments are matched pairs of parantheses
    if x1 == "(" and x2 == ")":
        return True
    if x1 == "{" and x2 == "}":
        return True
    if x1 == "[" and x2 == "]":
        return True

for i in x:
    if i == "(" or i == "{" or i == "[" :  #push to stack if open parantheses
        stack.append(i)
        index =+ 1
    else :
        if len(stack) == 0:
            balanced = False
        if matchedpair(stack[index-1],i):  #pop from stack if closed parantheses matches the one on stack
            stack.pop()
            index =- 1

if len(stack) == 0 and balanced:
    print("Balanced")

else:
    print("not balanced")

