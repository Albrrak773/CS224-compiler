'''
    Phase 1: A compiler that translates from infix input to postfix output

    Infix:  4+3-5+1
    Postfix: 43+5-1+

    Algorithm:
        1. Read the first digit and print it
        2. Loop: read operator, read next digit, print digit, print operator
        3. Repeat until end of input
'''

# ── Global State ──────────────────────────────────────────────
input_text = "4+3-5+1"
input_index = 0

# ── Lexer ─────────────────────────────────────────────────────
def lexan():
    global input_index
    if input_index < len(input_text):
        t = input_text[input_index]
        input_index += 1
        return t
    else:
        return 'EOF'

# ── Entry Point ───────────────────────────────────────────────
def main():
    # Step 1: grab the first digit and print it
    token = lexan()
    if not token.isdigit():
        print("syntax error: expected digit")
        return
    print(token, end='')

    # Step 2: keep reading (operator, digit) pairs
    while True:
        operator = lexan()
        if operator == 'EOF':
            break

        if operator != '+' and operator != '-':
            print("syntax error: expected + or -")
            return

        right = lexan()
        if right == 'EOF' or not right.isdigit():
            print("syntax error: expected digit after operator")
            return

        print(right, end='')
        print(operator, end='')

    print()  # final newline

if __name__ == "__main__":
    main()
