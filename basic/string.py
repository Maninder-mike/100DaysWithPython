x = "maninder"
y = "mike"
z = "this is a string line and it is a small line"


print("first word capitalize: ", x.capitalize())
print("lowercase: ", x.casefold())

print("center", x.center(20))
print("center with value: ", x.center(20, "-"))

print("count value in str: ", z.count("is"))

# print(x.encode())

print("value ends with: ", x.endswith("r"))
print(z.endswith("line"))

txt = "this is \t tab"

print("expande tabs: ", txt.expandtabs())
print(z.find("is"))


print("format values: ", "{} {}".format(x, y))

# print(x.format_map())

print(z.index("is"))

print(z.isalnum())
print("123456".isalnum())

print(x.isalpha())
print("123456".isalpha())

print(x.isascii())
print("123456".isascii())

deci = '\u0030'  # 0
num = '005'
print("decimal: ", deci.isdecimal())
print("digit: ", num.isdigit())

print("string or not: ", x.isidentifier())

print("is value lower case", z.islower())

print("value only countains numbers: ", num.isnumeric())

print("value not use \\n \\t: ", z.isprintable())

spc = "   "
print("all white space: ", spc.isspace())

print("if line start with uppercase: ", z.istitle())

print("join values in one line: ", "".join(z))

print("add str after value: ", x.ljust(20, '-'))
print("lowercase all sts: ", z.lower())

print("strip from giving value: ", z.lstrip('this'))

maktr = "Hello, Sam"
mktable = maktr.maketrans('S', 'P')
print("maketrans: ", maktr.translate(mktable))

print("partition with specified location: ", z.partition('this'))

print("replace value: ", z.replace('this', 'Not'))

print(z.rfind('is'))

print(z.rindex('is'))

print(x.rjust(20, '-'))

print("partition: ", z.rpartition('is'))

print(z.rsplit('is'))


space = "      spaceBetween        "

print("rstrip: ", space.rstrip())

print(z.split())

print(z.splitlines())

print(z.startswith("this"))

print('strip: ', space.strip())

print("first word uppercase: ", z.title())

mydict = {12: 123}
dtext = "Hello mike"
print("translate: ", dtext.translate(mydict))

print("uppercase: ", z.upper())
print("fill zero in front: ", x.zfill(20))
