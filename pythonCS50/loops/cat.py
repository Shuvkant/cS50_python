def main():
    number=getnumber()
    meow(number)

def getnumber():
    while True:
        n=int(input("Enter number "))
        if n>0:
            break
    return n
    
    
def meow(n):
    for _  in range(n):
        print('Meow')
        
main()