"""N = int(input("Enter the value of N:"))
num = 1
while num <= N:
    print(num)
    num += 1"""


"""n=int(input("Enter the number zaki : "))
sum=0
for i in range(1,n+1,1):
    sum+=i
print(sum)"""

"""n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
    	factorial=factorial *i
print("Factorial of the given number is: ", factorial)"""

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

X = 2
Y = 8
print(power(X, Y))

