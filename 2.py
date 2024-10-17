"""
 Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
Note: There is no trailing space at the end of output.
"""
user_input = input("Enter numbers separated by spaces: ")
sorted_set = sorted(set(map(int, user_input.split())))
print(" ".join(map(str, sorted_set)))
