#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     12/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime

print("welcome to Age Calculator")

birth_year=int(input("Enter Your Birth Year:\n"))
birth_month=int(input("Enter Your Birth Month:\n"))
birth_day=int(input("Enter Your Birth Day:\n"))

current_year=datetime.date.today().year
current_month=datetime.date.today().month
current_day=datetime.date.today().day

age_year=current_year - birth_year
age_month = current_month - birth_month
age_day = current_day - birth_day

if age_day < 0:
    age_month -= 1
    previous_month = (current_month - 1) if current_month > 1 else 12
    days_in_previous_month = (datetime.date(current_year, previous_month, 1) - datetime.timedelta(days=1)).day
    age_day += days_in_previous_month

# Adjust for negative months
if age_month < 0:
    age_year -= 1
    age_month += 12

print(f"Your age is : {age_year}-Years , {age_month}-Months ,{age_day}-Days ")