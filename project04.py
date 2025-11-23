'''a trafiic system records the average speed of vehicles every hour for 12 hours.
Write a program that:Reads 12 speed values (floats).
Calculate the average speed.
displays whether traffic flow was "slow" (avg < 40) , "normal" (40 - 80) or "fast" (avg>80)
CONCEPT : list input , loop , conditional check , average calculation'''

speeds = []

for i in range (0,12):
    speed = float(input(f"enter average speed in hour {i+1}: "))
speeds.append(speed)

avg_speed = sum(speeds)/12
print(f"Average speed of vehicles : {avg_speed}")
if avg_speed<40:
    print("Traffic flow was SLOW")

elif avg_speed>=40 or avg_speed<=80:
    print("Traffic flow was NORMAL")

else:
    print("Traffic flow was FAST")