int_value = 1
float_value = 3.1415
string_value = '1'  # or "1" both same
complex_value = 3j+2
list_value = [1, 'two', '3', {5: 'five'}, (9, 8, 7)]
tuple_value = (1, 2, 3, 'four', (9, 8, 7))
range_value = range(5)
dict_value = {'name': 'maninder', 'age': 25}
# dict_value1 = dict(name='maninder', age=25)

set_value = {1, 2, 'three', 6}
frozenset_value = frozenset({'apple', 'banana', 'cherry'})
bool_value = True | False
bytes_value = b'hello'
bytearray_value = bytearray(5)
memoryview_value = memoryview(bytes(5))

print('integer value', type(int_value))
print('float value', type(float_value))
print('String value', type(string_value))
print('3j+2', type(complex_value))
print('List value', type(list_value))
print('Tuple value', type(tuple_value))
print('Range value', type(range_value))
print('dictonary value', type(dict_value))
print('set value', type(set_value))
print('frozenset value', type(frozenset_value))
print('boolean', type(bool_value))
print('bytes', type(bytes_value))
print('bytearray', type(bytearray_value))
print('memoryview', type(memoryview_value))
