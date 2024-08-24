#Leap year program

year=int(input("Enter the year :\n"))
if(year%4==0 and year%100 or year%400==0):
    print("it is leap year")
else:
    print("it is not leap year")
