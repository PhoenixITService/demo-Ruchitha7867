words = input("Enter a list of words separated by spaces: ")
length= [len(word) for word in words if 'e' not in word]
print(length)
