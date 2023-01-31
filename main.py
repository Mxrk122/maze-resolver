from PIL import Image
from maze_problem import Maze_resolver
from numpy import asarray
# Es necesario isntalar opencv-python con pip install
import cv2 as opencv
from graph_search import *
image = Image.open('maze.bmp')

# Metodo para simplificar la imagen en cuadrados
def pixelate(file, size, obj):
    # Metodo para simplificar la imagen en cuadrados
    MazeColors = opencv.imread(file)
    MazeColors = opencv.resize(MazeColors, size)
    opencv.imwrite(obj, MazeColors)
    #Exportar imagen al archivo objetivo
    image = Image.open(obj)
    return image

#Laberinto, ajustar la resolucion para pdoer resolver cualquier laberinto
maze = pixelate("maze.bmp", (150, 150), "dum.bmp")
maze.save("dum.bmp")

# Instanciar el problema
mr = Maze_resolver(maze)
path = graph_search(mr)
mr.paint_path(path)
mr.save_image()