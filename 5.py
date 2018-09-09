import math


side1 = float(input("Length of first side"))
side2 = float(input("Length of second side"))
side3 = float(input("Length of third side"))


s= ( side1 + side2 + side3)/2

sqr= s*(s-side1)*(s-side2)*(s-side3)

if sqr <= 0 :
    print("Given sides do not form a triangle")

else:
    area = math.sqrt(sqr)
    print(str(round(area,2)))



