# Phase 4:
input file, output file and error file:
In this phase the changes are made only for the input, output and error files instad of
using the keyboard and the screen.
We add a new function called init() to read from the inputfile and to initilaize settings at the start of the compiler.
Update term() and rest() to write into outputfile and error to write into errorfile
Translate to Intermediate Language.

# Phase 5
split code into files
New grammar
expr -> expr + expr
expr -> expr - expr
expr -> expr * expr
expr -> expr div expr
expr -> expr / expr
expr -> expr mod expr
expr -> (expr)
expr -> ID | NUM