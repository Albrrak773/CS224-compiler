import enum
import symbol

output_file = open("file.obj", "w", encoding="utf-8")
il_file = open("file.il", "w", encoding="utf-8")

# region ─── utils ─────────────────────────────────────────────────────


class colors(enum.Enum):
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    PURPLE = "\033[35m"
    CLEAR = "\033[0m"


def print_and_write(input: str, color: colors | None = None):
    if color:
        print(f"{color.value}{input}{colors.CLEAR.value}", end=" ")
    else:
        print(input, end=" ")
    output_file.write(input + " ")


def push_il(input: str):
    il_file.write("push " + input + "\n")


# region ─── emitter ─────────────────────────────────────────────────────
def emit(token: str, value: str | None = None):
    match token:
        case "+":
            print_and_write(token, colors.CYAN)
            il_file.write("pop r1\npop r2\nadd r2, r1\npush r2\n")

        case "-":
            print_and_write(token, colors.CYAN)
            il_file.write("pop r1\npop r2\nsub r2, r1\npush r2\n")

        case "*":
            print_and_write(token, colors.CYAN)
            il_file.write("pop r1\npop r2\nmul r2, r1\npush r2\n")

        case "/":
            print_and_write(token, colors.CYAN)
            il_file.write("pop r1\npop r2\nRdiv r2, r1\npush r2\n")

        case "DIV":
            print_and_write('div', colors.CYAN)
            il_file.write("pop r1\npop r2\nidiv r2, r1\npush r2\n")

        case "MOD":
            print_and_write('mod', colors.CYAN)
            il_file.write("pop r1\npop r2\nmod r2, r1\npush r2\n")

        case "NUM":
            if value is None:
                raise Exception("NUM token requires a value")
            print_and_write(value, colors.YELLOW)
            push_il(value)

        case "ID":
            if value is None:
                raise Exception("ID token requires a value")
            print_and_write(symbol.symbol_table[int(value)].string, colors.PURPLE)
            push_il(symbol.symbol_table[int(value)].string)
        
        case "IDC":
            if value is None:
                raise Exception("ID token requires a value")
            il_file.write(f"call {symbol.symbol_table[int(value)].string}\n")

        case 'if':
            print_and_write('if', colors.RED)
            il_file.write("pop r2\ncmp r2, 0\nbe else\n")

        case 'then':
            print_and_write('then', colors.RED)
            il_file.write("else\n")

        case 'w1':
            print_and_write('while', colors.RED)
            il_file.write("while\n")

        case 'w2':
            print_and_write('while', colors.RED)
            il_file.write("pop r2\ncomp r2,0\nbe endwhile\n")

        case 'w3':
            print_and_write('while', colors.RED)
            il_file.write("b while\nendwhile\n")
        case 'l1':
            if value is None:
                raise Exception("ID token requires a value")
            il_file.write(f"{symbol.symbol_table[int(value)].string}:\n")
        case "l2":
            il_file.write("ret\n")
        case "main":
            il_file.write("main:\n")

        case "EOF":
            print_and_write("EOF", colors.RED)
        case _:
            raise Exception(f"Unknown token: {token}")
