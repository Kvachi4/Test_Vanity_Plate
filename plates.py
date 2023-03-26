def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s.split()
    if len(s) >= 2 and len(s) <= 6:
        return True
    if s[:2].isdigit():
        return False
   

if __name__ == "__main__":
    main()