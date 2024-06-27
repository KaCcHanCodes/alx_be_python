#Prompt for a value
pattern = int(input("Enter the size of the pattern: "))

#make the value of pattern immutable 
n = pattern

#loop through the value provided
while pattern > 0:
    for i in range(1, n + 1):
        print('*', end='')
    print()
    pattern -= 1