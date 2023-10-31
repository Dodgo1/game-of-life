import os
import time

import matplotlib.animation
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


class Cell:
    pass
#TODO:? change cells to dicts {x:0 y:0 value:1 sign:?}

class Map:
    width:int
    height:int
    arr:ndarray
    def __init__(self,size:tuple=(5,5),file_path=None):
        if file_path:
            with open(file_path) as file:
                arr = []
                for line in file.readlines():
                    row = [0 if char == "." else 1 for char in line[:-1]]
                    arr.append(row)
            self.arr = np.asarray(arr)
        else:
            self.arr = np.full(size,0)
        self.width, self.height = self.arr.shape[0], self.arr.shape[1]

    def __str__(self):
        return str(self.arr)

    def get_neighbours(self,target:tuple) -> list[int]:
        values = []
        for x in range(-1,2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                try:
                    values.append(self.get_cell((target[0]+x,target[1]+y)))
                except IndexError:
                    continue
                    #TODO: check so this error never occurs
        return values

    def step(self) -> ndarray:
        new_arr = np.full((self.width,self.height),0)
        for x,row in enumerate(self.arr):
            for y,cell in enumerate(row):
                value_neighbours = sum(self.get_neighbours((x,y)))

                if cell and value_neighbours in (2,3):
                    new_arr[x][y] = 1
                    continue # stays alive

                if not cell and value_neighbours == 3:
                    new_arr[x][y] = 1
                    continue # dead becomes alive
                # rest becomes/stays dead
        self.arr = new_arr
        return self.arr

    def frame(self,frame):
        self.step()
        self.img.set(data=self.arr)


    def set_cell(self,position:tuple,value):
        self.arr[position[0]][position[1]] = value

    def get_cell(self,position:tuple):
        return self.arr[position[0]][position[1]]

    def animate(self):
        fig, ax = plt.subplots()
        self.img = plt.imshow(self.arr)
        matplotlib.animation.FuncAnimation(fig=fig, func=self.frame, frames=3, interval=30)
        plt.show()



map = Map(file_path="sample_patterns/pulsar.txt")




