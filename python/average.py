
def average(*numbers):
    if not numbers:
        return "No numbers provided."
    return sum(numbers) / len(numbers)


print(average(10, 20, 30))      
print(average(5, 15))            
print(average(33,55))                 
