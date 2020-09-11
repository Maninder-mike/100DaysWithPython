write_file = open('write_new.txt', 'w')  # over write file if exists.

# write_file.write('this is a first line.')
write_file.write('this is a raplaced line.')

write_file.close()

# --------------------------------------------------------------------
with open('readwrite.txt', 'w+') as f:  # 'w+' for read and write both
    for x in range(1, 11):
        f.write(f"this in number: {x}\n")

print(f.read())
