import cv2 as cv
import numpy as np

path = 'C:/Users/Ernesto Fernandes/Desktop/projects/runescape/fishing/photos/'
screen = cv.imread(path + 'fishing_spot.png', cv.IMREAD_UNCHANGED)
shrimp = cv.imread(path + 'shrimp.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(screen,shrimp,cv.TM_CCOEFF_NORMED)



min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

""" cv.imshow('shrimp', result)
cv.waitKey()
cv.destroyAllWindows() """


if __name__ == '__main__':
    print(min_val, max_val, min_loc, max_loc)