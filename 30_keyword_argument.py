# Keyword arguments = An argument preceded by an identifier helps with the readability order of an arguments doesn't matter

def hello(greetings,title,first,last):
    print(f"{greetings} {title}{first} {last}")

hello("Hello",title="Mr.",last="Jkagency",first="Agbawo")


# To create a phone number using keyword argument

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+234", area=9037, first=860, last=443)
print(phone_num)