# w.a.p to print list
numbers=[10,20,30,40,50,60,70,80]
print(numbers)
print(type(numbers))

# access list items 
print("first items :",numbers[0])
print("last items :",numbers[-1])
print("second items :",numbers[1])
print("third items :",numbers[2])
print("fourth items :",numbers[3])

# calculate the list length
print("length of list :", len(numbers))

# remove an items from list
print(numbers.remove(30))
print(numbers)

# update a list 
numbers[2]=450
print(numbers)

# sort any list 
numbers.sort()
print("ascending orders of list :",numbers)

# find max numbers in list 
largest=numbers[0]

for num in numbers:
    if num > largest:
        largest=num
print("largest of numbers in list :", largest)

# find min numbers in list 
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest=num
print("smallest of numbers in list :", smallest)




