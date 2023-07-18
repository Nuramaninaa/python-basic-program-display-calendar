#python program to display calendar

#import calendar module
import calendar

#take input from user for year and month
year = int(input("Enter the number of year : "))
month = int(input("Enter the number of month : "))

#output of calendar
print(calendar.month(year,month)) 
