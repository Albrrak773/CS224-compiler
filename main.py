def main():
    print("Hello from cs224-compiler-project!")
    print_input()

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
    if input_index != len(input_text):
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
    pass
def reset():
    if lookahead == "+":
        pass
    if lookahead == "-":
        pass

def expr():
    term()
    reset()

if __name__ == "__main__":
    main()
