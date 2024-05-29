from datetime import datetime

age = int(input("Tell me your age :"));
dt = datetime.now()
Day = dt.isoweekday()

price = 12 if age>=18 else 8
# here short hand we will cosider if true price 12 if false so price 8
if Day == 3:
    price = price -2
    print("Today is wednesDay so DisCount 2$",price);
    exit()
    # if condition true we will exit from here

print(price,"Ticket Done!");