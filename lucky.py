#!/usr/bin/python
import random

from time import sleep
loading = 'Lucky.py : '
for i in range(10):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.2)

print("")
print("")

lotterynumbers = []
supplementary1 = []

x = 0
y = 1 
z = 2

# Six randomly drawn numbers
while x < 7:
    lotterynumbers.append(random.randint(1, 35))
    x += 1
 
lotterynumbers.sort()

# supplementary number one
while y < 2: 
    supplementary1.append(random.randint(1, 20))
    y += 2
    
supplementary1.sort()

#print('Powerball Ticket Generated'.center(2, '*'))
print('Powerball Ticket Generated')
#Printing
print("Your lucky numbers are: ")
print (lotterynumbers)
print ("Supplementary are: ")
print (supplementary1)
print("")

lotterynumbers = []
supplementary1 = []

x = 0
y = 1 
z = 2

# Six randomly drawn numbers
while x < 6:
    lotterynumbers.append(random.randint(1, 45))
    x += 1
 
lotterynumbers.sort()

#print('Lotto Ticket Generated'.center(2, '*'))
print('Lotto Ticket Generated')
#Printing
print("Your lucky numbers are: ")
print (lotterynumbers)
print("")

from time import sleep
loading = 'Goodluck! '
for i in range(10):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)

