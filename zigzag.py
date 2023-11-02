import time, sys
indent =0 # how many space to indent
indentIncreasing = True # indentation is increasing or not

try:
    while True:
        print(' ' * indent, end="")
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                # change direction
                indentIncreasing = False
        
        else:
            indent -= 1
            if indent == 0:
                # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit() # 若輸入ctrl+c 就可終止程式