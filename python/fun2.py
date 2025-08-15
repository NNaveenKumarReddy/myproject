def convert_into_minutes(hrs,minute):
    minute=(hrs*60)+minute
    return minute

h=int(input("Enter the Hours:"))
m=int(input("Enter the minutes:"))
m=convert_into_minutes(h,m)
print("minutes=",m)