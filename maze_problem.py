from PIL import Image
from numpy import asarray
from problem import Problem
from PIL import Image
class Maze_resolver(Problem):

    def __init__(self, maze: Image):
        self.maze = maze
        self.maze_arr = asarray(maze)
        self.width = 0
        self.height = 0
        self.initial_state = self.def_initial_state()
        print('Desde el constructor del problema', self.initial_state)
    
    def def_initial_state(self):
        # REalizar laa busqueda del punto rojo en la imagen
        maze_arr = self.maze_arr

        self.width = len(maze_arr[0])
        self.height = len(maze_arr)
       
        #buscar en cada pixel el inicio (punto rojo)
        for y in range(self.height):
            for x in range(self.width):
                current_pixel = maze_arr[y][x]

                r, g, b = current_pixel

                # Identificar color rojo
                if 200 <= r <= 254:
                    if (g <= 150) and (b <= 150):
                        initial_state = [x, y]
                        break
            
        return initial_state
                
    # Encargada de dar la accion de moverse hacia otras posiciones
    def actions(self, s):
        # Quiere decir que dara las coordenadas par amoverse
        # s es el punto en el que se encuentra actualmente
        x, y = s

        # hacer los movimientos a cada lugar
        upper = [x, y - 1]
        lower = [x, y + 1]
        left = [x - 1, y]
        right = [x + 1, y]

        # devolver un aarray de aciones
        return [upper, lower, left, right]
    
    def results(self, s, a):
        # Dado un punto y accion -> moverse a las demas direcciones
        # s es el punto inicial y a hacia donde se movera

        # REvisar que el movimiento no se pase de los limites
        x, y = a
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            # Revisar que no se trate de una pared
            maze_arr = self.maze_arr
            current_pixel = maze_arr[y][x]

            r, g, b = current_pixel
            # Identificar color negro
            if (0 <= r <= 10) and (0 <= g <= 10) and (0 <= b <= 10):
                # retornar el mismo estado para que no vuelva a pasar por el
                return s
            else:
                # no pintar la entrada ni salida
                # Identificar color verde
                if 200 <= g <= 254:
                    if (r <= 150) and (b <= 150):
                        print("encontre la salida")
                        pass
                # Identificar color rojo
                elif 200 <= r <= 254:
                    if (g <= 150) and (b <= 150):
                        pass
                else:
                    maze_arr[y][x] = [0, 0, 100]

                return a
        else:
            # si se pasaa de los indices devolver el mismo estado
            return s
    
    def goalTest(self, s):
        # REalizar laa busqueda del punto verde en la imagen
        maze_arr = self.maze_arr
        #buscar en cada pixel el final (punto verde)
        x, y = s

        current_pixel = maze_arr[y][x]

        r, g, b = current_pixel

        # Identificar color verde
        if 200 <= g <= 254:
            if (r <= 150) and (b <= 150):
                return True
        else:
            return False
    
    def stepCost(self, s, a, s_):
        return super().stepCost(s, a, s_)
    
    def pathCost(self, states):
        return super().pathCost(states)

    # Metodos propios del problema
    def paint_path(self, path):
        maze = self.maze_arr
        for cord in path.getStates():
            x, y = cord
            maze[y][x] = [100, 100, 100]

    def save_image(self):
        new_image = Image.fromarray(self.maze_arr)
        new_image.save('result.bmp')
