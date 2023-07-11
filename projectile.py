import math
print(math.pi)
print(math.tan)
#accelertion
g = 9.81 ** 2
#velocity
vo = 44
#elevation
O = 80
#distance traveled
x = 0.5
#height
yo = 1
#theta
#theta = 80*(math.pi/180)
deg = 80






yo = 1.0  # initial yo value
x = 0.5  # x value
theta = deg*(math.pi/180)  # convert degrees to radians

sum1 = yo + x * math.tan(theta)
print("sum1:",sum1 )


sum2 = g ** 2 + x ** 2

print ("sum2",sum2)





sum3 = 2 * vo * math.cos(theta)  # 2(vo cos θ)
sum3 = sum3 ** 2  # squared expression

print("Sum3:", sum3)

y = sum1 - (sum2 / sum3)
print("y" ,y)
#print(g)
