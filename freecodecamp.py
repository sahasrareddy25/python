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
    print('Ticket booking failed due to restrictions')"""


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
