apd = open('demo.txt', 'a')   # add values end of the lines.
apd.write('last line')
print(apd.mode) # check what file mode.
apd.close()

# ----------------------------------------
with open('readwrite.txt', 'a+') as a:
    for x in range(5):
        a.write(f"append {x}\n")

