t = ()
print(type(t)) # empty tuple
one_element_tuple = (42, )
three_elements_tuple = 1, 3, 5
a, b, c = 1, 2, 3 # tuple for multiples assignment
print(a, b, c)
print(3 in three_elements_tuple)   

a, b = 1, 2
c = a # we need three lines and a temporary var c
a = b
b = c
print(a, b) # a and b have been swapped
