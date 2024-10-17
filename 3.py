'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
set1_input = input("Enter numbers for the first set separated by spaces: ")
set1 = set(map(int, set1_input.split()))

set2_input = input("Enter numbers for the second set separated by spaces: ")
set2 = set(map(int, set2_input.split()))

difference = set1.difference(set2)

print(" ".join(map(str, sorted(difference))) + " ")
