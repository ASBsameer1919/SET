"""
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
"""
values = []
unique_values = set()

n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for _ in range(n):
    value = int(input())
    values.append(value)
    unique_values.add(value)

duplicates = len(values) - len(unique_values)

print(f"Duplicate Values: {duplicates}")
print(" ".join(map(str, unique_values)))
