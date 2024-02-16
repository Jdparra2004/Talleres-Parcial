#contruye expresiones logicas
a = 10
b = 12
c = 12
d = 10

#primera expresión
resultado = ((a>b) and (b<c))
print(resultado)

#segunda expresión
expresion = ((a>b) or (a<c)) and ((a==c) or (a>=b))
print(expresion)