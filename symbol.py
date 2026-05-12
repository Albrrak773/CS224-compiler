class entry:
    def __init__(self, string, token):
        self.string = string
        self.token = token

symbol_table: list[entry] = []

def lookup(string):
    for i in range(len(symbol_table)):
        if symbol_table[i].string == string:
            return i
    return None

def insert(string, token):  
    symbol_table.append(entry(string, token))
    return len(symbol_table) - 1


keywords = [entry('div', 'DIV'), entry('mod', 'MOD')]

def intialize_symbol_table():
    for keyword in keywords:
        insert(keyword.string, keyword.token)

