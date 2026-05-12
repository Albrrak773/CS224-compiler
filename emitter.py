import enum
output_file = open("file.obj", "w", encoding="utf-8")
il_file = open("file.il", "w", encoding="utf-8")

# region ─── utils ─────────────────────────────────────────────────────


class colors(enum.Enum):
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
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
        case "NUM":
            if value is None:
                raise Exception("NUM token requires a value")
            print_and_write(value, colors.YELLOW)
            push_il(value)
        case "EOF":
            print_and_write("EOF", colors.RED)
        case _:
            raise Exception(f"Unknown token: {token}")
