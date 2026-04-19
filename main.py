'''
    Phase 1: A compiler that translates from infix input to postfix output

    Grammar:
        expr  -> term rest
        rest  -> + term rest | - term rest | ε
        term  -> digit
'''

# ── Global State ──────────────────────────────────────────────
input_text = "4+3-5+1"
input_index = 0
lookahead = ''

# ── Lexer ─────────────────────────────────────────────────────
def lexan():
    global input_index, input_text
    if input_index < len(input_text):
        t = input_text[input_index]
        input_index += 1
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
# (called "reset" here — it handles everything after the first term)
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

# expr -> term rest
def expr():
    term()
    reset()

# ── Entry Point ───────────────────────────────────────────────
def main():
    global lookahead
    lookahead = lexan()
    expr()

if __name__ == "__main__":
    main()
