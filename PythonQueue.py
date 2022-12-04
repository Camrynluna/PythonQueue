#PythonQueue
names = []

for i in range(0, 10):
    acceptedName = input('Enter Name:')
    names.append(acceptedName)

print(names)

for name in range(len(names)):
    print(names.pop(0))

print (names)


    

