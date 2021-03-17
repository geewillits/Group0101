largest = None
smallest = None
while True:
    nums = input("Enter a number: ")
    if nums == "done":
        break
    try:
        num = int(nums)
    except:
        print("Invalid input")
    if largest is None:
        largest = num
        smallest = num
    elif num < int(smallest):
        smallest = num
    elif num > int(largest):
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)