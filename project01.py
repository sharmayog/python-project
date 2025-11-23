travel_distance = int(input("How far do you want to travel (in miles)? "))

if travel_distance < 3:
    print("You should ride a bicycle.")
elif travel_distance < 300:
    print("You should ride a motorcycle.")
else:
    print("You should drive a supercar.")
