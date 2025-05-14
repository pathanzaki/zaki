def power(x, y=2):
    result = 1
    for _ in range(abs(y)):  
        result *= x
    if y < 0: 
        result = 1 / result
    return result   

print(power(2, 3))  
print(power(5))     
print(power(2, -3)) 