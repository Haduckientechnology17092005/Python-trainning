Strings = ['a','b','c','d']
print(Strings[2])
Strings.append('e')
print(Strings)
Strings.pop()
print(Strings)
Strings.remove('b')
print(Strings)
Strings.insert(2,'f')
print(Strings)
#Array native python methods :-
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
# Strings.clear()
# print(Strings)
#copy()	Returns a copy of the list
import copy
original_list = [1, 2, [3, 4]]
# Tạo shallow copy
shallow_copy = copy.copy(original_list)
print("Shallow Copy:", shallow_copy)
# Tạo deep copy
deep_copy = copy.deepcopy(original_list)
print("Deep Copy:", deep_copy)
# Thay đổi trong đối tượng con của bản gốc
original_list[2][0] = 99
print("\nAfter modifying original_list:")
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
#count()	Returns the number of elements with the specified value
print("Count:")
count = Strings.count(2)
print(count)
#extend()	Add the elements of a list (or any iterable), to the end of the current list
list1 = ['a', 'b', 'c']
string = "def"
list1.extend(string)
print(list1)
#index()	Returns the index of the first element with the specified value
my_list = [10, 20, 30, 40, 50]
try:
    index = my_list.index(60)
    print(index)
except ValueError:
    print("Phần tử không tồn tại trong danh sách")
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
Strings.reverse()
print(Strings)
#sort()	Sorts the list
Strings.sort()
print(Strings)
#List objects are implemented as arrays. 
#They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) 
#operations which change both the size and position of the underlying data representation.
#For in depth information on arrays 
#https://docs.python.org/3/tutorial/datastructures.html
#to implement arrays as a stack 
#https://docs.python.org/3/library/collections.html#collections.deque