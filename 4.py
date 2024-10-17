"""
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.
"""
set_input = input("Enter numbers for the set separated by spaces: ")
my_set = set(map(int, set_input.split()))

element_to_delete = int(input("Enter the element to delete: "))

if element_to_delete in my_set:
    my_set.remove(element_to_delete)
    print(" ".join(map(str, sorted(my_set))) + " ")
else:
    print("Given value is not present in the set list.")
