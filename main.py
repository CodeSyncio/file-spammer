import os
from time import sleep as s
def c():
    os.system('cls' if os.name=='nt' else 'clear')
print('Made by me, use this wisely, and no, its not made for educational perposes :)')
print('starting in 5 seconds...')
s(5)
c()
print('File Name?')
fn=input()
c()
print('Text inside files?')
fin=input()
c()
print('Extension of spam files?')
ex=input()
c()
print('Amount of spam files?')
am=input()
c()
ln=0
while int(ln)<int(am):
    print('Creating files ('+(str(ln))+' / '+(str(am)))
    file=open (fn+'_________'+(str(ln))+'.'+ex ,"w")
    file.write(str(fin))
    ln=ln+1
print('DONE')
s(1)
c()
ca = 5
for number in range(5):
    print ('quitting in '+ str(ca)+  ' sec...')
    s(1)
    ca = ca -1