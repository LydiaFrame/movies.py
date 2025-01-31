#!/usr/bin/env python3

"""Write a program to calculate the price of a movie ticket"""

__author__="Lydia Frame"
__date__="01/31/2025"

#prompt for time of day
time_of_day = input("morning, noon, or night? ") 
print()
#prompt for weekend (y or n)
weekend = input("weekend (y/n)? ")
print()
#prompt for age
age = int(input("age? "))
print()

#calculate day price
if time_of_day.lower() == "morning":
    price = 10
elif time_of_day.lower() == "noon":
    price = 12
elif time_of_day.lower() == "night":
    price = 14
else:
    print("Invalid input for time of day")
    exit()

#calculate surcharge 
if weekend.lower() == "y":
    surcharge = 2.5
else:
    surcharge = 0

#calculate discount 
if age <= 12 or age >= 65:
    discount = (price + surcharge)*0.1 
    ticket_cost = (price + surcharge) - discount
    print("Your ticket costs $" + str(ticket_cost))
else:
    ticket_cost = (price + surcharge)
    print("Your ticket costs $" + str(ticket_cost))
