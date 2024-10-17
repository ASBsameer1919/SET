"""
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output

"""
input1 = input()
input2 = input()

set1 = set(map(int, input1.split()))
set2 = set(map(int, input2.split()))

common_elements = set1.intersection(set2)
print(" ".join(map(str, sorted(common_elements))) + " ")
