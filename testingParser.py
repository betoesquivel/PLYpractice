import parser
import logging

def test(code):
    log = logging.getLogger()
    parser.parser.parse(code, tracking=True)

print "Programa con 1 var y 1 asignacion bien: "
s = "program id; var beto: int; { id = 1234; }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con 1 var mal: "
s = "program ; var beto: int; { id = 1234; }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa sin vars bien: "
s = "program id;  { id = 1234; }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con var mal: "
s = "program id; var beto int; { id = 1234; }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con var mal: "
s = "program id; var beto: int { id = 1234; }"
test(s);
print "Original: \n{0}".format(s)
print "\n"

print "Programa con var mal: "
s = "program id; beto: int; { id = 1234; }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con bloque vacio bien: "
s = "program id; var beto: int; {  }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con bloque lleno y estatuto mal: "
s = "program id; var beto: int; { id = 1234; id2 = 12345 }"
test(s)
print "Original: \n{0}".format(s)
print "\n"

print "Programa con bloque lleno y condicion mal: "
s = "program id; var beto: int; { id = 1234; if ( 8 > 3 ) { id3 = 34234; } else { } }"
test(s)
print "\n"
print "Original: \n{0}".format(s)

