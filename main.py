count = int(input("How many numbers? "))

numbers = []

for i in range(count):
    number = float(input())
    numbers.append(number)

average = sum(numbers) / len(numbers)
MA = max(numbers)
MI = min(numbers)

print("average number: ", average)
print("maximum number: ", MA)
print("minimum number: ", MI)