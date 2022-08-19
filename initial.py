from datetime import datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from random import random
import random
import pandas as pd
import os
import sys
from time import sleep


#Type Writer Function
def typewriter(text):
    for i in text:
        print(i, end = "")
        sys.stdout.flush()
        sleep(0.001)
    print("\n")

#Clear Console Function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("""


               .__                               
__  _  __ ____ |  |   ____  ____   _____   ____  
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >
             \/          \/            \/     \/ 
                                       
                                                 
                                                 
""")
sleep(1)

cls()
#input quantity of names
while True:
    try:
        typewriter('\nHow many profiles would you like to generate?')
        num = int(input('>>> '))
        break
    except ValueError:
        cls()
        typewriter('Input integer only')
        continue
cls()
print("Quantity:", num)


#input gender choice
while True:
    typewriter('Choose gender:')
    answer = input('\nMale = M \nFemale = F \n >>> ')
    if answer.lower().strip() == 'm':
        gender = 2
        break
    elif answer.lower().strip() == 'f':
        gender = 3
        break
    # elif answer.lower().strip() == 'b':
    #     gender = 1
    #     break
    else:
        cls()
        typewriter('Please enter gender again...')
        continue
cls()
print("Quantity:", num)    
print('gender: ', gender )

#input name style
while True:
    typewriter('What name style would you like?') 
    answer = int(input('1 - Common \n 2 - Average \n 3 - Rare\n>>> '))
    if answer == 1:
        style = 1
        style_name = 'Common'
        break
    elif answer == 2:
        style = 2
        style_name = 'Average'
        break
    elif answer ==3:
        style = 3 
        style_name = 'Rare'
        break
    else: 
        cls()
        typewriter('\nPlease enter style number again....')
        continue
cls()


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

fullName = output
firstName = output[0::2]
lastName = output[1::2]


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

numberList = random.sample(range(1,99), num)

while True:
    try:
        recoveryCatchall = [f'{numberList}@fairmontmail.com'] * num
        break
    except ValueError:
        continue


while True:
    try:
        forwardingCatchall = ['@fairmontmail.com'] * num
        break
    except ValueError:
        continue


#Attempt 1
# recoveryMail = [list(e) for e in zip(firstName,lastName,recoveryCatchall,)]
# print(recoveryCatchall)

#Attemp 2
# recoveryMail = []
# for firstName,lastName,recoveryCatchall in zip(firstName,lastName,recoveryCatchall):
#     recoveryMail['{}{}{}'.format(firstName,lastName,recoveryCatchall)]
#     # print(recoveryMail)
#     # recoveryMail.append("%s %s %s" % firstName,lastName,recoveryCatchall)
#     print(recoveryMail)


#Attempt 3

recoveryMail = []
fName = firstName
lName = lastName

for fName, lName, recoveryCatchall in zip(fName,lName,recoveryCatchall):
    recoveryMail.append('{}{}{}'.format(fName,lName,recoveryCatchall))
    
   
forwardingMail = []
fname = firstName
lname = lastName

for fname, lname, forwardingCatchall in zip(fname,lname,forwardingCatchall):
    forwardingMail.append('{}{}{}'.format(fname,lname,forwardingCatchall))
    
df = pd.DataFrame({'First Name':firstName, 'Last Name':lastName, 'Gender':li, 'DOB':DOB, 'Recovery Mail':recoveryMail, 'Forwarding Mail':forwardingMail})

cls()
print("Quantity:", num)
print('Gender: ', gender )
print('Style: ', style_name)

typewriter('\n\nProcess complete \nOpen export.csv..........')

df.to_csv('export.csv', encoding='utf-8', index=False)
