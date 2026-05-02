# Q: Add number and calculate average
print("\nAverage Calculator")
x= int(input("please enter how much number:::"))
total= 0
for i in range(x):
    y = float(input("Enter your numbers:::"))
    total= total+y

if x !=0:
    avg= total/x
    print(f"Average is {avg}")
else:
    print("Can't Calculate Average")


 



