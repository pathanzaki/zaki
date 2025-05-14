def handle_exceptions():
    try:
        
        print("Choose an option to simulate an exception:")
        print("1. NameError")
        print("2. ValueError")
        print("3. IndexError")
        print("4. ZeroDivisionError")
        print("5. TypeError")
        print("6. FileNotFoundError")
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            print(undefined_variable)  
        elif choice == 2:
            int("invalid")  
        elif choice == 3:
            my_list = [1, 2, 3]
            print(my_list[5])  
        elif choice == 4:
            result = 10 / 0  
        elif choice == 5:
            print("string" + 5)  
        elif choice == 6:
            with open("nonexistent_file.txt", "r") as f:  
                content = f.read()
        else:
            print("Invalid choice.")
    except NameError:
        print("Caught a NameError: Variable is not defined.")
    except ValueError:
        print("Caught a ValueError: Invalid value provided.")
    except IndexError:
        print("Caught an IndexError: List index out of range.")
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError: Division by zero.")
    except TypeError:
        print("Caught a TypeError: Operation on incompatible types.")
    except FileNotFoundError:
        print("Caught a FileNotFoundError: File does not exist.")
    except Exception as e:
        print(f"Caught an unexpected exception: {e}")

handle_exceptions()
