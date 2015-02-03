#!env/bin/python
import ply.lex as lex

reserved = {
    "program":"PROGRAM",
    "if":"IF",
    "else":"ELSE",
    "print":"PRINT",
    "var":"VAR",
    "int":"INT",
    "float":"FLOAT"
}
literals = ";:}{><+-*/)(="
tokens = (
    'CTEI','CTEF','CTES','DIFF','ID',
    'PROGRAM','IF','ELSE','PRINT','VAR',
    'INT','FLOAT'
)

# token regular definition
t_ignore = ' \t'
t_CTEI   = '[0-9]+'
t_CTEF   = '[0-9]+\.[0-9]+'
t_CTES   = '".*"'
t_DIFF   = '<>'

def t_ID(t):
    '[a-zA-Z][a-zA-Z0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    print "Error de lexico en: ", t
    exit(-1)
    t.lexer.skip(1)

lexer = lex.lex();
