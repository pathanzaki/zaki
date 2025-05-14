
def print_data(**kwargs):
    if not kwargs:
        print("No data provided.")
        return
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_data(name="zaki", age=21, city="New York")
print_data(language="Python", version=3.10)
print_data()  
