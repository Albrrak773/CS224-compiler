'''
    Phase 1: A compiler that translates from infix input to postfix output

    Grammar:
        expr  -> term rest
        rest  -> + term rest | - term rest | ε
        term  -> digit
'''

# ── Global State ──────────────────────────────────────────────
input_text = "4  +          3\n-5+1"
input_index = 0
lookahead = ''

# ── Lexer ─────────────────────────────────────────────────────
def lexan():
    global input_index, input_text
    # input_text = input_text.replace(" ", "").replace("\t", "").replace("\n", "")
    if input_index < len(input_text):
        while True:
            t = input_text[input_index]
            input_index += 1
            if t == ' ' or t == '\t' or t == '\n':
                continue
            return t
    else:
        return 'EOF'

# ── Utilities ─────────────────────────────────────────────────
def error():
    print("syntax error")

def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()
    else:
        error()

# ── Grammar Rules ─────────────────────────────────────────────

# term -> digit   (prints the digit, then consumes it)
def term():
    if lookahead.isdigit():
        print(lookahead, end='')
        match(lookahead)

# rest -> + term rest | - term rest | ε
def rest():
    if lookahead == "+":
        match(lookahead)
        term()
        print('+', end='')
        rest()
    elif lookahead == "-":
        match(lookahead)
        term()
        print('-', end='')
        rest()

# expr -> term rest
def expr():
    term()
    rest()

# ── Entry Point ───────────────────────────────────────────────
def main():
    frontend()
    backend()

def frontend():
    parser()

def parser():
    global lookahead
    lookahead = lexan()
    expr()

def backend():
    pass
if __name__ == "__main__":
    main()
