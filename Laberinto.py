## LABERINTO ##

# Variables
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
empezar = ((0,0),)
salida = ((4,4),)


class Laberinto:
    # Inicializa variables de instancia
    def __init__(self, muro, empezar, salida, filas, columnas):
        self.laberinto = []
        self.muro = muro
        self.empezar = empezar
        self.salida = salida 
        self.filas = filas
        self.columnas = columnas
     
    '''
    Con esta función crearemos el laberinto en función de las dimensiones
    y de los puntos que le damos para colocar los muros, la salida y la entrada.
    '''        
    def crear_tablero(self):
        for i in range(self.filas):
            x = []
            for j in range(self.columnas):
                if (i, j) in self.muro:
                    x.append("X")
                if (i, j) in self.empezar:
                    x.append("E")
                if (i, j) in self.salida:
                    x.append("S")
                if ((i, j) not in self.muro) and ((i, j) not in self.empezar) and ((i, j) not in self.salida):
                    x.append(" ")
            self.laberinto.append(x)
            
    '''
    Con esta función recorremos el laberinto que hemos creado y lo mostraremos por consola
    '''
    def mostrar_laberinto(self):
        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[i])):
                print(self.laberinto[i][j], end='')
            print()    
        
            
            
# Crear una instancia de la clase Laberinto         
lab = Laberinto(muro, empezar, salida, 5, 5)

# Generar y mostrar el laberinto
lab.crear_tablero()
lab.mostrar_laberinto() 
