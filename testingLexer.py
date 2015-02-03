import lexer
s = "program id; var beto: int; { id = 1234; }"
lexer.lexer.input(s)


for token in lexer.lexer:
    print token
