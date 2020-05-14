import sys
import time

indent = 0
indentUp = True

try:
    while True:
        print(' ' * indent, end='')
        if indentUp:
            print("(>'')>")
            time.sleep(0.1)
            indent += 1
            if indent == 20:
                indentUp = False
        else:
            print("<(''<)")
            time.sleep(0.1)
            indent -= 1
            if indent == 0:
                indentUp = True

except KeyboardInterrupt:
    sys.exit()
