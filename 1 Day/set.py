theset = {'apple','banana','mango','pineapple'}
fruits = {'apple', 'banana'}
vegies = {'tomato','lettuse','onion','potato'}

theset.add('cherry')    # Add item in set

copyset = theset.copy()   #Copy all items to new set

theset.difference(fruits)  # diffenence between two sets values - 'cherry','mango','pineapple'

theset.difference_update(fruits) # update current set after remove same values from other set

theset.discard('kivi') # Remove the specified item, this in not raise error if item not in it
theset.remove('mango') # Remove the specified item but if item not in it this raise the error
theset.pop() # Removes an element from the set Randomly
# theset.clear()   #Clear all values from set

theset.intersection(fruits)  # output is same value from both sets

fruits.intersection_update(theset) # remove item that not in other set

x = theset.isdisjoint(vegies)  # Return True if no items in both sets
y = theset.issubset(fruits)  # Return False if not all items in set
z = theset.issuperset(fruits)  # Returns whether this set contains another set or not


addboth = theset.union(fruits, vegies) #add both set together if item is double then remove one

setupdate = theset.update(vegies) # Update the set with the union of this set and others


fruits.symmetric_difference(theset) # Returns a set with the symmetric differences of two sets
fruits.symmetric_difference_update(theset) # Inserts the symmetric differences from this set and another
