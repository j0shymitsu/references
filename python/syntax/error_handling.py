######################
### ERROR HANDLING ###
######################



# Division example
try:
    x = float(input("Enter the dividend: "))
    y = float(input("Enter the divisor: "))

    quotient = x/y

    print(quotient)

except:
    print("There was a problem with your code")
else:
    print("Your code is good")
finally:
    print("End\n\n")

# Conversion
bad_input = True

while bad_input:
    try:
        age=int(input("Enter age: "))
        bad_input = False
    except ValueError as diag:
        print(f"An exception has been raised: {diag}\nEnd\n\n")

    # Fraction example
    try:
        n = input("\n\nEnter the numerator: ")
        d = input("Enter the denominator: ")

        f = int(n)/int(d)

        print(f"{n}/{d} is a valid fraction.")
    
    except ValueError:
        print("Value error.")
    
    except ZeroDivisionError:
        print("Value cannot be zero.")

    except TypeError:
        print("Type error.")
    
    except Exception as e:
        print(f"General exception: {e}")

    finally:
        if bad_input == True:
            print("Please try again.")
