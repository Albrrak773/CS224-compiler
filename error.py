
error_file = open("file.err", "w", encoding="utf-8")
def error(reason: str | None = None):
    error_file.write(f"syntax error: {reason}")
    print(f"\n\033[31msyntax error\033[0m\n{reason}")
    exit(1)