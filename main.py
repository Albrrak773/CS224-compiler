"""
Phase 1: A compiler that translates from infix input to postfix output
Phase 2: clear whitespace and newlines from the input
Phase 3: Allow Numbers instead of just single digits

Grammar:
    expr  -> term rest
    rest  -> + term rest | - term rest | ε
    term  -> NUM { print(NUM.value)  }
"""

import re

# region ── Global State ──────────────────────────────────────────────
input_text0 = "44  +    3      3\n-5+1"
input_text0 = input_text0.replace(" ", "").replace("\t", "").replace("\n", "")
input_text = re.split(r"(\W+)", input_text0)
print(f"Input: {input_text}")
input_index = 0
lookahead = ""
tokenval = 0
# endregion


# region ─── Lexer ─────────────────────────────────────────────────────
def lexan():
    global input_index, input_text
    if input_index < len(input_text):
        t = input_text[input_index]
        input_index += 1
        if t.isdigit():
            global tokenval
            tokenval = int(t)
            return "NUM"
        return t
    else:
        return "EOF"


# endregion


# region ─── Utilities ─────────────────────────────────────────────────
def error(reason: str | None = None):
    print(f"\n\033[31msyntax error\033[0m\n{reason}")
    exit(1)


def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()


# endregion

# region ─── Grammar Rules ─────────────────────────────────────────────


def term():
    """
    term -> NUM { print(NUM.value) }
    """
    if lookahead == "NUM":
        print(tokenval, end=" ")
        match(lookahead)
    else:
        error(f"Expected '{lookahead}' to be a NUM")


def rest():
    """
    rest -> + term  { print('+') } rest
    rest -> - term { print('-') } rest
    rest -> ε
    """
    if lookahead == "+":
        match(lookahead)
        term()
        print("+", end=" ")
        rest()
    elif lookahead == "-":
        match(lookahead)
        term()
        print("-", end=" ")
        rest()
    elif lookahead == "EOF":
        match(lookahead)
        print("\033[31mEOF\033[0m")
    # we allow ε so we shouldn't error here?
    # else:
    #     error(f"Expected '{lookahead}' to be one of: +, - or EOF")


# expr -> term rest
def expr():
    term()
    rest()


# endregion


# region ─── Entry Point ───────────────────────────────────────────────
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
# endregion
