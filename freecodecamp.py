"""#it is a problem to check whether the candiate is eligible to watch the movie in the scheduled timing of minor and major.soo here we need 
#give the prices of tickets and also adding the discounts and i implemented this using conditional statements
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    
else:
    print('Ticket booking failed due to restrictions')


#problem is regarding employees wroking out there and here we needd to add there names and detailed info shud be stored using variables
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
"""

"""Build a Travel Weather Planner
For this lab, you will use conditional statements to determine whether commuting is possible based on the weather, the distance to travel, and the availability of a vehicle.
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
You should create the following variables:
distance_mi (a number representing the distance to travel in miles)
is_raining (a boolean representing if the user is currently experiencing rainy weather)
has_bike (a boolean representing if the user has a bicycle)
has_car (a boolean representing if the user has a car)
has_ride_share_app (a boolean representing if the user has an app that allows them to request a ride)
You should use conditional statements to determine whether commuting is possible based on the values of these variables.
You should use if, elif, and else statements to evaluate the distance categories in ascending order.
If distance_mi is a falsy value:
You should print False.
If the distance is less than or equal to 1 mile:
You should print True only if it is not raining.
Otherwise, you should print False.
If the distance is greater than 1 mile and less than or equal to 6 miles:
You should print True only if the person has a bike and it is not raining.
Otherwise, you should print False.
If the distance is greater than 6 miles:
You should print True if the person has a car or has a ride-share app.
Otherwise, you should print False."""

distance_mi = 5
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
