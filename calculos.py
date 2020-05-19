from sympy import *

'''
aqui puedes crear funciones que recojan resultados de la web y con ello, puedes empezar a 
dividir el contenido de la web dependiendo del calculo que quieras mostrar. Un ejemplo es lo que esta abajo
Al usar latex, puedes mostrar un resultado como una imagen. El unicode, lo muestra como si fuera
en assci

Tambien, en vez de una pagina web, puedes empezar a utilizar visual studio code para realizar tus calculos y 
hacer graficos de todo tipo y crear estadisticas y todo lo que quieras. 

es un lenguaje muy potente para el calculo matematico y personalmente lo uso bastante a la hora de crear estadisticas
y mostrarlas en la web con pandas. 
'''

x,y,z = symbols('x y z')
# init_session(use_latex=True) se imprime una especie de foto
init_printing(use_unicode=True)

def muestra():

    # print_mathml(Integral(sqrt(1/x), x))
  
    # ecuacion = Eq(1 + x,x**2)
    # res=solve(ecuacion, x)
    
    return print_mathml(Integral(sqrt(1/x), x))