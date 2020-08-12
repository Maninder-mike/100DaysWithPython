theset = {'apple', 'banana', 'mango', 'pineapple'}
fruits = {'apple', 'banana'}
vegies = {'tomato', 'lettuse', 'onion', 'potato'}

theset.add('cherry')    # Add item in set

copyset = theset.copy()  # Copy all items to new set

# diffenence between two sets values - 'cherry','mango','pineapple'
theset.difference(fruits)

# update current set after remove same values from other set
theset.difference_update(fruits)

# Remove the specified item, this in not raise error if item not in it
theset.discard('kivi')
# Remove the specified item but if item not in it this raise the error
theset.remove('mango')
theset.pop()  # Removes an element from the set Randomly
# theset.clear()   #Clear all values from set

theset.intersection(fruits)  # output is same value from both sets

fruits.intersection_update(theset)  # remove item that not in other set

x = theset.isdisjoint(vegies)  # Return True if no items in both sets
y = theset.issubset(fruits)  # Return False if not all items in set
# Returns whether this set contains another set or not
z = theset.issuperset(fruits)


# add both set together if item is double then remove one
addboth = theset.union(fruits, vegies)

# Update the set with the union of this set and others
setupdate = theset.update(vegies)


# Returns a set with the symmetric differences of two sets
fruits.symmetric_difference(theset)
# Inserts the symmetric differences from this set and another
fruits.symmetric_difference_update(theset)
