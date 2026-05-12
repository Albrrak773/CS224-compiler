import re
from symbol import lookup, insert
import symbol

input_file = open("file.exp", "r", encoding="utf-8")
input_text_raw = input_file.read()
input_text = re.split(r"([\W])", input_text_raw)
input_text = [t for t in input_text if t.strip() != ''] 
print(f"Input: {input_text}")
input_index = 0
tokenval = 0


def lexan():
    global input_index, input_text, tokenval
    while True:
        if input_index < len(input_text):
            t = input_text[input_index]
            input_index += 1
            if t == ' ' or t == '\t':
                continue
            if t.isdigit():
                tokenval = int(t)
                return "NUM"
            elif t.isalnum() and t[0].isalpha():  # e.g asdf and not 123abc
                p = lookup(t)
                if p is None:
                    p = insert(t, "ID")
                tokenval = p
                return symbol.symbol_table[p].token
            return t
        else:
            return "EOF"
