my_list = [5, 2, 12, 7, 3, 8]
low = []
for element in my_list:
    if element < 5:
        low.append(element)
print(low) # Prints the final list only after the loop completes (Correctly prints [2, 3])
