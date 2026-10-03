# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator

# *args example
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.","Jkagency","Agbawo","Bekke")
print()


# **kwargs example
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="11 Fake street", 
              city= "London",
              state="Freetown",
              zip= "1914" )
print()

# *args and **kwargs example together

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
              
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")
    

shipping_label("Mr.","Jkagency","Agbawo","Bekke",
               street="11 Fake street", 
               pobox= "POBOX #1001",
               city= "London",
               state="Freetown",
               zip= "1914")
print()