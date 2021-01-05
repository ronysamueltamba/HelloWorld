# l = [1, 2, 3, 3, 4, 4, 4, 5, 'abc', "abc"]
# no_duplicate_set = set(l)
# print(no_duplicate_set)

# s = {'Blueberry, Rasberry'}
# s.add('Strawberry')
# print(s)

# VEN DIAGRAMS

library_1 = {'Harry Potter', 'Hunger Games', 'Lord od the Rings'}
library_2 = {'Harry Potter', 'Romeo and Juliet'}

all_books = library_1.union(library_2)
at_booth_libraries = library_1.intersection(library_2)
go_to_library = library_1.difference(library_2)

print(go_to_library)