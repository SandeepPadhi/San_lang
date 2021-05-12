from Basic.basic import *

while True:
    txt = input('sanlang 1.0:\n')
    print(txt)
    tokens,Error = Lexer(txt,'<stdin>').tokenize()
    if Error:
            print(Error)
    else:
        print(tokens)
