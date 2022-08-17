from bdb import Breakpoint
from datetime import datetime, timedelta
from random import random, randrange
import random

#enter birthdate
# while True:
#     date = input('Enter a Birth Date (DD-MM-YYY) \n>>> ')
#     today = datetime.today() 
#     try:
#         input_date = datetime.strptime(date, "%d-%m-%Y")
#         age = today.year - input_date.year - ((today.month, today.day) < (input_date.month, input_date.day))
#         if age > 18:
#             print(f'{age} Years Old')
#             break
#         else:
#             print('Not above 18 years old.')
#             continue
#     except ValueError:
#         print('Enter a Valid date in the format YYYY.....')
#         continue


#birthdate generator
# num = 5 
# def random_date(start,end):
#     delta = end - start
#     int_data = (delta.days * 24 * 60 * 60) + delta.seconds
#     random_second = randrange(int_data)
#     return start + timedelta(seconds=random_second)

# d1 = datetime.strptime('1/1/1965 1:30 PM', '%d/%m/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2002 4:50 AM', '%d/%m/%Y %I:%M %p')

# def birth_date(d1,d2):
#     random_date(d1, d2).date()

# birth_date()

# for random_date in range(num): 
#     print(random_date)

# while x > num:
#     print(x) 


# BirthDate Generator V2: 
# num = 5
# def genDateOfBirth(number=1):
#     CurrentTime = datetime.now()
#     Year = random.randrange(1970,2000)
#     for item in range(number):
#         yield random.randrange(1960,2002), random.randrange(1, 12), random.randrange(1, 31)

# dateTimeThatIwant = genDateOfBirth(num)

# DOB = []
# for year, month, date in dateTimeThatIwant:
#     DOB.append("%s-%s-%s" % (year, month, date))

# print(DOB)

# with open('names.csv', "w", encoding='utf-8') as file:
#     file.write(str(header))
#     file.write(str(list, ranDate))

# print('\n \nOpen names.csv file...')

num = 5 
gender = 3

while True: 
    if gender == 2:
        li = ['Male'] * num  
        print(li)
        break
    elif gender == 3:
        li =['Female'] * num
        print(li)
        break
    else:
        continue