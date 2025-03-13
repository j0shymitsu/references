######################
### ERROR HANDLING ###
######################

# Basic example
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)


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

# In functions

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e 

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]


# Unhandled / raised exception

def purchase_item(price, gold_available):
    if price > gold_available:
        raise Exception ("not enough gold")
    else:
        return gold_available - price
    


