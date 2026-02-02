import calendar

def cal(year, month):
    print(calendar.month(year, month))

def main():
    
    year = 2025
    month = 1
    
    while True:
        cal(year, month)
        nav = input("\nType '>' for next, '<' for previous, or 'x' to close:\n").strip()

        if nav == ">":
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        elif nav == "<":
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
        elif nav == "x":
            break
        else:
            print("Invalid command. Press '>' for next, '<' for previous, or 'x' to close\n")

if __name__ == "__main__":
    main()