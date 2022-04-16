import cv2 as cv 
import numpy as np
from fishing import findClickPositions

path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/'
findClickPositions(path + 'fishing_spot.png', path + 'shrimp.png', 0.5, True)