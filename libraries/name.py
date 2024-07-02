import sys

if len(sys.argv)<2:
    sys.exit('Too few arguments')


for arg in sys.argv[1:]:
    print("Hello, my name is ", arg)


# Another type of printing method
'''
elif len(sys.argv)>2:
    sys.exit('Too many arguments')


print('Hello, my name is ', sys.argv[1].strip().title())
'''
