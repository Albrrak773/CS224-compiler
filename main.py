"""
Phase 1: A compiler that translates from infix input to postfix output.
Phase 2: clear whitespace and newlines from the input.
Phase 3: Allow Numbers instead of just single digits.
Phase 4: input files and Intermediate Language.
Grammar:
    expr  -> term rest
    rest  -> + term rest | - term rest | ε
    term  -> NUM { print(NUM.value)  }
"""

import enum
import re

# region ── Global State ──────────────────────────────────────────────
input_file = open("file.exp", "r", encoding="utf-8")
output_file = open("file.obj", "w", encoding="utf-8")
il_file = open("file.il", "w", encoding="utf-8")
error_file = open("file.err", "w", encoding="utf-8")

input_text_raw = input_file.read()
input_text_raw = input_text_raw.replace(" ", "").replace("\n", "")
input_text = re.split(r"(\W+)", input_text_raw)
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
    error_file.write(f"syntax error: {reason}")
    print(f"\n\033[31msyntax error\033[0m\n{reason}")
    exit(1)


class colors(enum.Enum):
    RED = "\033[31m"
    CYAN = "\033[36m"
    END = "\033[0m"

def print_and_write(input: str, color: colors | None = None):
    if color:
        print(f"{color.value}{input}{colors.END.value}", end=" ")
    else:
        print(input, end=" ")
    output_file.write(input + " ")

def push_il(input: str):
    il_file.write("push " + input + "\n")


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
        print_and_write(str(tokenval))
        push_il(str(tokenval))
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
        print_and_write("+", colors.CYAN)
        il_file.write("pop r1\npop r2\nadd r2, r1\npush r2\n")
        rest()
    elif lookahead == "-":
        match(lookahead)
        term()
        print_and_write("-", colors.CYAN)
        il_file.write("pop r1\npop r2\nsub r2, r1\npush r2\n")
        rest()
    elif lookahead == "EOF":
        match(lookahead)
        print_and_write("EOF", colors.RED)
    # we allow ε so we shouldn't error here?
    else:
        error(f"Expected '{lookahead}' to be one of: +, - or EOF")


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
