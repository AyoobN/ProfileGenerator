from datetime import datetime
from numpy import true_divide
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from random import random, randrange
import random


#input quantity of names
while True:
    try:
        num = int(input('Enter a number \n>>> '))
        break
    except ValueError:
        print('Input integer only')
        continue
print("num:", num)


#input gender choice
while True:
    answer = input('\nMale = M \nFemale = F \nBoth = B \n >>> ')
    if answer.lower().strip() == 'm':
        gender = 2
        break
    elif answer.lower().strip() == 'f':
        gender = 3
        break
    elif answer.lower().strip() == 'b':
        gender = 1
        break
    else:
        print('Please enter gender again...')
        continue
print('gender: ', gender )

#input name style
while True: 
    answer = int(input('\nPlease enter name style.... \n 1 - Common \n 2 - Average \n 3 - Rare\n>>> '))
    if answer == 1:
        style = 1
        break
    elif answer == 2:
        style = 2
        break
    elif answer ==3:
        style = 3 
        break
    else: 
        print('\nPlease enter style number again....')
        continue
print('style: ', style)

#gender column
while True: 
    if gender == 2:
        li = ['Male'] * num  
        break
    elif gender == 3:
        li =['Female'] * num
        break
    else:
        continue


#request HTML of url --> locate '<ol>' tag within HTML code --> convert HTML to text
#n=(number of names), g=(1= M & F, 2 = M, 3 = F), st=(1=common, 2=avergae, 3=rare)

page = requests.get(f'http://random-name-generator.info/index.php?n={num}&g={gender}&st={style}')
soup = BeautifulSoup(page.content, 'html.parser')
output = str(soup.find_all('ol')[0].get_text())
# output = str([item.text for item in soup.select('ol')])

output = (output.strip("\n\t")).split()

lastName = output[0::2]
firstName = output[1::2]


#Random Birthday Generator
def genDateOfBirth(number=1):
    CurrentTime = datetime.now()
    Year = random.randrange(1970,2000)
    for item in range(number):
        yield random.randrange(1960,2002), random.randrange(1, 12), random.randrange(1, 31)

dateTimeThatIwant = genDateOfBirth(num)

DOB = []
for year, month, date in dateTimeThatIwant:
    DOB.append("%s-%s-%s" % (year, month, date))

