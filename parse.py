"""
Phase 1: A compiler that translates from infix input to postfix output.
Phase 2: clear whitespace and newlines from the input.
Phase 3: Allow Numbers instead of just single digits.
Phase 4: input files and Intermediate Language.
Grammar:
    start -> list eof
    list -> expr ; list | ε 
    expr -> term moreterms
    moreterms -> + term { print('+') } moreterms
           | - term { print('-') } moreterms
           | ε
    term -> factor morefactors
    morefactors -> * factor { print('*') } morefactors
             | / factor { print('/') } morefactors
             | div factor { print('DIV') } morefactors
             | mod factor { print('MOD') } morefactors
             | ε
    factor -> (expr)
      | id { print(id.lexeme) }
      | num { print(num.value) }
"""

import lexer
from lexer import lexan
from error import error
from emitter import emit
from symbol import intialize_symbol_table

lookahead = ""


def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()


# region ─── Grammar Rules ─────────────────────────────────────────────


def term():
    """
    term -> NUM { print(NUM.value) }
    """
    if lookahead == "NUM":
        emit("NUM", str(lexer.tokenval))
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
        emit("+")
        rest()
    elif lookahead == "-":
        match(lookahead)
        term()
        emit("-")
        rest()
    elif lookahead == "EOF":
        match(lookahead)
        emit("EOF")  # not part of the grammar
    else:
        error(f"Expected '{lookahead}' to be one of: +, - or EOF")


# expr -> term rest
def expr():
    term()
    rest()


# endregion


def parser():
    global lookahead
    intialize_symbol_table()
    lookahead = lexan()
    expr()
