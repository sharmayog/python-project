'''an app for mobile hosting provider charges $0.51 per hour
how much does it cost to operate per day per week per month?
how many days can i operate with $918'''
per_hour=0.51
per_day=0.51*24
per_week=0.51*24*7
per_month=0.51*24*30
budget=918
db=918/(0.51*24)

print("cost per hour = ",per_hour)
print("cost per day = ", per_day)
print("cost per week = ",per_week)
print("cost per month =",per_month)
print("days in budget=",db)