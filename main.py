'''
    Phase 1: A compiler that translates from infix input to postfix output
'''
def main():
    global lookahead
    lookahead = lexan()
    expr()

def print_input():
    global lookahead
    while lookahead != 'EOF':
        lookahead = lexan()
        print(lookahead, end='')

input_text = "4+3-5+1"
input_index = 0
lookahead = ''

def lexan():
    global input_index, input_text
    if input_index < len(input_text):
        t = input_text[input_index]
        input_index += 1
        return t
    else:
        return 'EOF'

def error():
    print("syntax error")

def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()
    else:
        error()

def term():
    if lookahead.isdigit():
        print(lookahead, end='')
        match(lookahead)

def reset():
    if lookahead == "+":
        match(lookahead)
        term()
        print('+', end='')
        reset()
    elif lookahead == "-":
        match(lookahead)
        term()
        print('-', end='')
        reset()
    # else:
    #     error()


def expr():
    term()
    reset()

if __name__ == "__main__":
    main()
