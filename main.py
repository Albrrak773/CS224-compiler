'''
    Phase 1: A compiler that translates from infix input to postfix output
    Phase 2: clear whitespace and newlines from the input

    Grammar:
        expr  -> term rest
        rest  -> + term rest | - term rest | ε
        term  -> digit
'''

# ── Global State ──────────────────────────────────────────────
input_text = "4  +    3      3\n-5+1"
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
def error(reason: str | None = None):
    print(f"\n\033[31msyntax error\033[0m\n{reason}")
    exit(1)

def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()

# ── Grammar Rules ─────────────────────────────────────────────

# term -> digit   (prints the digit, then consumes it)
def term():
    if lookahead.isdigit():
        print(lookahead, end='')
        match(lookahead)
    else:
        error(f"Expected '{lookahead}' to be digit")

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
    elif lookahead == "EOF":
        match(lookahead)
        print("\032[31mEOF\033[0m")
    else:
        error(f"Expected '{lookahead}' to be one of: +, - or EOF")

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
