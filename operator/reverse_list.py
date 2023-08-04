# Reverse List Order:
# Description: Write a program that reverses the order of elements in a given list.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

li = []
no_length = 6
for i in range(no_length):
    items = int(input("Enter a no:"))
    li.append(items)
print(li)
li.reverse()
print(li)