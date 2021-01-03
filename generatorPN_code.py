#Generador de código PN - Tercer parcial - Comunicaciones moviles.
#Librerias
import argparse 
def portXOR(A,B):
    if(A == 1):
        if(B == 0):
            return 1
        else: # A = 1 , B = 1
            return 0
    else:# A = 0
        if(B == 0):
            return 0
        else: # A = 0 , B = 1
            return 1
class convert:
    def __init__(self , semilla):
        """Constructor del objeto """
        self.semilla = semilla
    def longitud(self):
        """Retorna la longitud del código psedoaleatorio (PN)"""
        m = self.semilla
        return (2**len(list(m)))-1
    def generator(self,longitud):
        """Retonar el código PN """
        lista = list(self.semilla)
        two = []
        for i in lista:
            two.append(int(i))
        originalCode = two# Estado inicial.
        copy = originalCode
        out = []
        cont = 0
        while True:
            # Realizamos la operacion XOR
            out.append(copy[-1])
            index = portXOR(copy[-1],copy[-2])# Parametros: Ultimo y Penultimo elemento. 
            copy.pop(-1)# Delete - ultimo elemento.
            copy.insert(0,index)
            cont += 1
            if(cont == longitud):# Regreso al estado inicial.
                break # fin del ciclo infito
        return str(out)
if __name__ == "__main__":
        description = """Ejemplo de uso: 
        + Ingreso Semilla (Estado inicial):
            --s 1010
        """
        # Creamos nuestro  objeto  analizador de argumentos.
        parser = argparse.ArgumentParser(description = "Paso de parametros" , epilog = description ,
            formatter_class = argparse.RawDescriptionHelpFormatter)
        # Agregamos  las opciones  de lineas de comando  que podra  utilizar nuestro programa.
        # Indicando el tipo de dato que ese  argumento  opcional  debe tener
        parser.add_argument("--s" , help = "Semilla" , required = True)
        args = parser.parse_args()# Guardamos parametros ingresados.
        # Instanciamos..
        code_generator = convert(args.s)# Parametros: semilla (Estado inicial)
        longt = code_generator.longitud()
        programOut = code_generator.generator(longt)
        print(programOut)
        
