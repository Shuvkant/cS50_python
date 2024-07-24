import sys
from sayings import hello
from sayings import bye

if len(sys.argv) ==2:
    hello(sys.argv[1])
    bye(sys.argv[1])
