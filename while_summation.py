#while summation code following directions from Readme
num = int(input("Enter a number: "))
total = 0
count = 1
while count <= num:
    total += count
    count += 1
print("The sum from 1 to", num, "is:", total)
