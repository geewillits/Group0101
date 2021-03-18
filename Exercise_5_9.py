#My attempt to write a program to answer 5.9 in Python for Everyone text book
n=0
t=0
while True:
    nums = input("Enter a number: ")
    if nums == "done":
        break
    try:
        num = int(nums)
    except:
        print("Invalid input")
        continue
    if n == 0:
        n += 1
        t += num
    elif num is not None:
        n += 1
        t += num

print("Total is", t)
print("Count is", n)
print("Average is", (t/n))




        
