table = int(input("Enter the table : "))
start = int(input("Enter the starting number : "))
limit = int(input("Enter the limit : "))
while start <= limit:
    print(f"{start} * {table} = {start * table}")
    start += 1


num = int(input("Enter number to multiply "))
table = int(input(f"Enter how many times to multiply {num} by "))
for i in range(1, table + 1):
    print(f"{num} x {i} = {num * i}")