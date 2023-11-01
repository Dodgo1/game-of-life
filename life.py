import matplotlib.animation
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


class Map:
    width: int
    height: int
    img: any
    arr: ndarray

    def __init__(self, size: tuple = (5, 5), file_path=None):
        if file_path:
            with open(file_path) as file:
                arr = []
                for line in file.readlines():
                    row = [0 if char == "." else 1 for char in line.strip("\n")]
                    arr.append(row)
            self.arr = np.asarray(arr)
        else:
            self.arr = np.full(size, 0)
        self.width, self.height = self.arr.shape

    def __str__(self):
        """ Dunder method to allow printing the map by simple "print(Map)" """
        return str(self.arr)

    def get_neighbours(self, target: tuple) -> list[int]:
        """ Method which allows to get values of all neighbours of a cell,
        can be used to sum up values and decide its fate in the next step """
        values = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                try:
                    values.append(self.get_cell((target[0] + x, target[1] + y)))
                except IndexError:
                    continue
        return values

    def step(self) -> None:
        """ Function for simulating time """
        new_arr = np.full((self.width, self.height), 0)
        for x, row in enumerate(self.arr):
            for y, cell in enumerate(row):
                value_neighbours = sum(self.get_neighbours((x, y)))

                if cell and value_neighbours in (2, 3):
                    new_arr[x][y] = 1
                    continue  # stays alive

                if not cell and value_neighbours == 3:
                    new_arr[x][y] = 1
                    continue  # dead becomes alive
                # rest becomes/stays dead
        self.arr = new_arr

    def set_cell(self, position: tuple, value) -> None:
        """ Setter for values of cells """
        self.arr[position[0]][position[1]] = value

    def get_cell(self, position: tuple) -> int:
        """ Getter of values of cells """
        return self.arr[position[0]][position[1]]

    def animate(self, frames: int = 10, interval: int = 30):
        """ Function which automatically calls step() then animates each step using matplotlib """
        fig, ax = plt.subplots()
        self.img = plt.imshow(self.arr)
        _ = matplotlib.animation.FuncAnimation(fig=fig, func=self._frame, frames=frames, interval=interval)
        plt.show()

    def _frame(self, _):
        """ Update function to be used in matplotlib.animation.FuncAnimation,
        calls step then updates data in the plot """
        self.step()
        self.img.set(data=self.arr)


life = Map(file_path="sample_patterns/pulsar.txt")
life.animate()
