"""
Phase 1: A compiler that translates from infix input to postfix output.
Phase 2: clear whitespace and newlines from the input.
Phase 3: Allow Numbers instead of just single digits.
Phase 4: input files and Intermediate Language.
Grammar:
    Start -> stmt eof
    stmt -> id = expr
    stmt -> if (expr) then stmt
    stmt -> while (expr) do stmt
    stmt -> begin CS end
    CS -> stmt ; CS | ε
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
from emitter import il_file
import symbol
lookahead = ""


def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexan()


# region ─── Grammar Rules ─────────────────────────────────────────────


def stmt():
    """
    stmt -> id = expr
    stmt -> if (expr) then stmt
    stmt -> while (expr) do stmt
    stmt -> begin CS end
    """

    if lookahead == "ID":
        match("ID")
        id = symbol.symbol_table[int(lexer.tokenval)].string
        match("=")
        expr()
        il_file.write(f"pop {id}\n")
    elif lookahead == "if":
        match("if")
        match("(")
        expr()
        match(")")
        emit('if')
        match("then")
        stmt()
        emit('then')
    elif lookahead == "while":
        match("while")
        emit('w1')
        match("(")
        expr()
        match(")")
        emit('w2')
        match("do")
        stmt()
        emit('w3')
    elif lookahead == "begin":
        match("begin")
        CS()
        match("end")
    else:
        error(f"Expected '{lookahead}' to be one of: ID, if, while or begin")

def CS():
    """
    CS -> stmt ; CS | ε
    """
    # CLANKER SUGGESTION
    # if lookahead in ["ID", "if", "while", "begin"]:
        # stmt()
        # match(";")
        # CS()
    # ε means we do nothing. we still raise the correct error in stmt()
    # else:
    #     error(f"Expected '{lookahead}' to be one of: ID, if, while, begin or EOF")
    while lookahead != 'end':
        stmt()
        match(";")



def moreterms():
    """
    moreterms -> + term { print('+') } moreterms
    moreterms -> - term { print('-') } moreterms
    moreterms -> ε
    """
    if lookahead == "+":
        match("+")
        term()
        emit("+")
        moreterms()
    elif lookahead == "-":
        match("-")
        term()
        emit("-")
        moreterms()
    # ε means we do nothing. we still raise the correct error in factor()
    # else:
    #     error(f"Expected '{lookahead}' to be one of: +, - or EOF")


def term():
    """
    term -> factor morefactors
    """
    factor()
    morefactors()


# expr -> term rest


def factor():
    """
    factor -> (expr)
    factor -> id { print(id.lexeme) }
    factor -> num { print(num.value) }
    """
    if lookahead == "(":
        match("(")
        expr()
        match(")")
    elif lookahead == "NUM":
        emit("NUM", str(lexer.tokenval))
        match("NUM")
    elif lookahead == "ID":
        emit("ID", str(lexer.tokenval))
        match("ID")
    else:
        error(f"Expected '{lookahead}' to be one of: (, NUM or ID")


def morefactors():
    """
    morefactors -> * factor { print('*') } morefactors
    morefactors -> / factor { print('/') } morefactors
    morefactors -> div factor { print('DIV') } morefactors
    morefactors -> mod factor { print('MOD') } morefactors
    morefactors -> ε
    """
    if lookahead == "*":
        match("*")
        factor()
        emit("*")
        morefactors()
    elif lookahead == "/":
        match("/")
        factor()
        emit("/")
        morefactors()
    elif lookahead == "DIV":
        match("DIV")
        factor()
        emit(
            "DIV",
        )
        morefactors()
    elif lookahead == "MOD":
        match("MOD")
        factor()
        emit(
            "MOD",
        )
        morefactors()
    # ε means we do nothing. we still raise the correct error in factor()
    # else:
    #     error(f"Expected '{lookahead}' to be one of: *, /, DIV, MOD or EOF")


def expr():
    term()
    moreterms()


# endregion


def parser():
    global lookahead
    intialize_symbol_table()
    lookahead = lexan()
    stmt()
