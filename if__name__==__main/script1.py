# if__name__==__main__: (This script can be imported OR run stand alone)
# Functions and classes in this module can be reused without the main block of code executing 
# Good practice (code is modular, helps readability, leaves no global variables, avoid unintended execution)

# Ex. library = import library for functionality when running library directly, display a help page


def favourite_food(food):
    print(f"Your favourite food is {food}")


def main():
    print("This is script1")
    favourite_food("Ofe Onugbu")
    print("Goodbye")
    

if __name__ == '__main__':
    main()