#Older version
'''
names=[]

for _ in range(3):
    names.append(input("What's your name "))

for  name in sorted(names):
    print(f"Hello, {name}")
    
'''
import sys
import os
import time
import tty
import termios

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#print(f'You pressed: {char}')

def insert():
      name=input("What's your name ").strip().title() 
                                                      
      with open("names.csv","a") as file:             
          file.write(f"{name}\n")                     
      print(f"{name} added")


def read():
     names=[]                            
     with open("names.csv") as file:     
         for line in file:               
             names.append(line.rstrip()) 
                                         
                                         
     for name in sorted(names):          
         print(f"Hello, {name}")         
def main():                                      
        while True:                                  
         os.system("clear")                         
         print("Select a option")                 
         print("1.Insert\n2.Read\n3.Exit")        
         response=input()
         responseInt=int(response)
         if responseInt==1:                          
             insert()                             
             print("Press any key to continue: ") 
             char=get_char()                      
         elif responseInt==2:                        
             read()                               
             print("Press any key to continue: ") 
             char=get_char()                      
         else:                                    
             sys.exit()                           
                                                  
                                                  
if __name__=="__main__":
    main()
