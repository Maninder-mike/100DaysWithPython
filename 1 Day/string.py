x = "maninder"
y = "mike"
z = "this is a string line \n and it is a small line"


print(x.capitalize())
print(x.casefold())

print(x.center(20))
print(x.center(20, "-"))

print(z.count("is"))

# print(x.encode())

print(x.endswith("r"))
print(z.endswith("line"))

# print(z.expandtabs(2))
print(z.find("is"))

print("{}{}".format(x, y))

# print(x.format_map())

print(z.index("is"))

print(z.isalnum())
print("123456".isalnum())

print(x.isalpha())
print("123456".isalpha())

print(x.isascii())
print("123456".isascii())

h = 3

# print(x.isdecimal())
# print(h.isdecimal())
# print(h.isdigit())

# print(x.isidentifier())

print(z.islower())
# print(h.isnumeric())
print(z.isprintable())

# print(x.isspace())

# print(z.istitle())

print(z.capitalize())

print("".join(z))

print(x.ljust(20, '-'))
print(z.lower())

print(z.lstrip('this'))
# print(z.l)

# print(z.maketrans())

print(z.partition('this'))

print(z.replace('this', 'Not'))

print(z.rfind('is'))

print(z.rindex('is'))

print(x.rjust(20, '-'))

print(z.rpartition('\n'))

print(z.rsplit('is'))


space = "      spaceBetween        "

# print(space.rstrip())

print(z.split())

print(z.splitlines())

print(z.startswith("this"))

print(space.strip())

print(z.title())

# print(z.translate())

print(z.upper())
print(x.zfill(20))