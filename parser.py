#!env/bin/python
import lexer
import ply.yacc as yacc

tokens = lexer.tokens

def p_programa(p):
    '''programa : PROGRAM ID ';' programa2 bloque'''

def p_programa2(p):
    '''programa2 : vars
                 | empty'''

def p_vars(p):
    '''vars : VAR vars2'''

def p_vars2(p):
    '''vars2 : ID vars3'''

def p_vars3(p):
    '''vars3 : ',' vars2
             | ':' tipo ';' vars4'''

def p_vars4(p):
    '''vars4 : vars2
             | empty'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT'''

def p_bloque(p):
    '''bloque : '{' bloque2 '}' '''

def p_bloque2(p):
    '''bloque2 : estatuto bloque2
               | empty '''

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura'''

def p_asignacion(p):
    '''asignacion : ID '=' expresion ';' '''

def p_expresion(p):
    '''expresion : exp expresion2 '''

def p_expresion2(p):
    '''expresion2 : '>' exp
                  | '<' exp
                  | DIFF exp
                  | empty'''

def p_condicion(p):
    '''condicion : IF '(' expresion ')' bloque condicion2 ';' '''

def p_condicion2(p):
    '''condicion2 : ELSE bloque
                  | empty '''

def p_escritura(p):
    '''escritura : PRINT  '(' escritura2 ')' ';' '''

def p_escritura2(p):
    '''escritura2 : expresion escritura3
                  | CTES escritura3'''

def p_escritura3(p):
    '''escritura3 : ',' escritura2
    | empty '''

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
                | empty '''

def p_factor(p):
    '''factor : '(' expresion ')'
              | factor2 '''

def p_factor2(p):
    '''factor2 : '+' varcte
               | '-' varcte
               | varcte '''

def p_varcte(p):
    '''varcte : ID
              | CTEI
              | CTEF'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print "Error de sintaxis en token: ", p.type
    print "en la siguiente posicion: {0} ".format(p.lexpos)
parser = yacc.yacc()
