people = [("Alice", 30), ("Bob", 20), ("Charlie", 35), ("David", 40), ("Eve", 22)]
names = [name for name, age in people if age > 25 and 'e' not in name.lower()]
print("the name is:",names)
