x = "maninder"
y = "mike"
z = "this is a string line /n and it is a small line"


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

print(z.lstrip('is'))