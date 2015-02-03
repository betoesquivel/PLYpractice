#!env/bin/python
import lexer
import ply.yacc as yacc

tokens = lexer.tokens

def p_programa(p):
    '''programa : PROGRAM ID ';' vars bloque
                | PROGRAM ID ';' bloque'''

def p_vars(p):
    '''vars : VAR vars2'''

def p_vars2(p):
    '''vars2 : ID ':' tipo ';' vars3
             | ID ',' vars2'''

def p_vars3(p):
    '''vars3 : vars2
             | empty'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT'''

def p_bloque(p):
    '''bloque : '{' bloque2'''

def p_bloque2(p):
    '''bloque2 : estatuto bloque2
               | '}' '''

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura'''

def p_asignacion(p):
    '''asignacion : ID '=' expresion ';' '''

def p_expresion(p):
    '''expresion : exp expresion2 exp'''

def p_expresion2(p):
    '''expresion2 : '>'
                  | '<'
                  | DIFF'''

def p_condicion(p):
    '''condicion : IF '(' expresion ')' bloque condicion2'''

def p_condicion2(p):
    '''condicion2 : ELSE bloque ';'
                  | ';' '''

def p_escritura(p):
    '''escritura : PRINT  '(' escritura2'''

def p_escritura2(p):
    '''escritura2 : expresion ','
                  | CTES ','
                  | ')' ';' '''

def p_exp(p):
    '''exp : termino exp2'''

def p_exp2(p):
    '''exp2 : '+' exp
            | '-' exp
            | empty'''

def p_termino(p):
    '''termino : factor termino2'''

def p_termino2(p):
    '''termino2 : '*' termino
                | '/' termino
                | empty'''

def p_factor(p):
    '''factor : '(' expresion ')'
              | '+' varcte
              | '-' varcte
              | empty'''

def p_varcte(p):
    '''varcte : ID
              | CTEI
              | CTEF'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print "Error de sintaxis: ", p

parser = yacc.yacc()
