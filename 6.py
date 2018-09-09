#Take inputs
lower = int(input("Enter lower limit : "))
upper= int(input("Enter upper limit : "))

#Traverse through range of nos.
for n in range(lower, upper + 1):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10

    if n == sum:
        print(n)

    elif n == upper:
        print("No Armstrong Nos. in range")