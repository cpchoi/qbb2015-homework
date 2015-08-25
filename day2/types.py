#!/usr/bin/env python

# String
s = "A String"

# Integer (can be unlimited!)
i = 10000

# Floating point / real number
f = 0.333

# Coerce a integer into a float, vice versa  float into integer (will round)

i_as_f = float(i)
f_as_i = int(f)

# Boolean
truthy = True
falsy = False

# Dictionary (very improtant - because a lot of hte funcitons are built on dictionaries)
d1 = { "key1":"value1", "key2":"value2" }
d2 = dict( key1="value1", key2="value2" )
# putting a list in dictionary value
#d3 = dict{"key1": ["hi", "bye"], "key1": "value2"}
# dictionary containing a list of tuples
d3 = dict( [ ("key1" , "value1"), ("key2", "value2") ] )

#Lists -- are mutable, conventions contains only one type
l = [1,2,3,4,5]
l.append(7)

#Tuple -- can have different elements integers, strings, or floats, but are not immutable, they are a bit more efficient
t = (1, "foo", 5.0)

# comma after print, it will print each one with a space
for value in (i, f, s, truthy, l, t, d1, d2, d3):
    print value, type( value )




