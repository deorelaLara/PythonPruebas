# Practica #1.
#
# Contador de Palabras.
#
# Objetivos:
#
# 1.	Recordar el manejo de archivos tipo texto tanto de entrada como salida.
# 2.	Implementar un ejercicio que permita manejo de String, identificando cadenas separadas por espacios.
#
# Escribir una aplicación llamada ”ContadorDePalabras”, que lea líneas de un archivo tipo texto, hasta que encuentre el fin de archivo.
#
# La aplicación debe indicar cuantas palabras tiene cada línea, una palabra es un conjunto de caracteres separados por uno ó más espacios. Y también debe indicar el número de líneas leídas.
#
# La salida se grava en un archivo tipo texto.
# Ejemplo:
# Entrada del programa:
# Este es     un   ejemplo
# del programa         que cuenta
# palabras
# quizás no es un buen ejemplo
# pero algo es algo
#
# Salida del programa:
# línea 1: 4 palabras
# línea 2: 4 palabras
# línea 3: 1 palabras
# línea 4: 6 palabras
# línea 5: 4 palabras
# total 5 líneas.

########################################################################################################################

def contarPalabras(archivo = 'prueba.txt'):
    local = open(archivo, 'r')
    lineas = local.readlines()
    for i in range(0,len(lineas)):
        print('línea {}: {} palabras'.format(i+1, len(lineas[i].split())))

def contarLineas(archivo = 'prueba.txt'):
    local = open(archivo, 'r')
    print('total {} líneas.'.format(len(local.readlines())))
    local.close()

def main():
    # Prueba #1
    # contarLineas()
    # Prueba #2
    # print('Este es     un   ejemplo'.split())
    # Prueba #3
    # contarPalabras()
    contarPalabras()
    contarLineas()

if __name__ == '__main__':
    main()
