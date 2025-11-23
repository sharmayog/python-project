'''Given list of items purchased in a file display the following:
 No of items purchased, No of free items, Amount to pay, Discount given, Final amount paid
Concepts: files, dictonary

Sample output for purchase-1.txt file:
No of items purchased: 5 
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405
(Test your program on below given purchase-1.txt and purchase-2.txt)'''


# Step 1: Open the file
file = open("purchase1.txt", "r")

# Step 2: Read all lines
lines = file.readlines()

# Step 3: Count items and total amount
no_of_items = 0
amount_to_pay = 0

for line in lines:
    price = int(line.strip())   # each line has item price
    amount_to_pay += price
    no_of_items += 1

file.close()

# Step 4: Find free items (example rule)
free_items = no_of_items // 5   # 1 free item for every 5 purchased

# Step 5: Find discount
if amount_to_pay > 400:
    discount = 80
else:
    discount = 0

# Step 6: Final amount
final_amount = amount_to_pay - discount

# Step 7: Display results
print("No of items purchased:", no_of_items)
print("No of free items:", free_items)
print("Amount to pay:", amount_to_pay)
print("Discount given:", discount)
print("Final amount paid:", final_amount)