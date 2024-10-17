"""
Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
"""
input_values = input()
values_list = set(map(int, input_values.split()))
print("Maximum:", max(values_list))
print("Minimum:", min(values_list))
