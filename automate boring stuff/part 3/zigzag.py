# Write your code here :-)
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True


try:
    while True:
        print(' ' * indent, end='')
        print('*'*8)
        time.sleep(0.1) # Pause for .1 seconds

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyBoardInterrupt:
    sys.exit()
