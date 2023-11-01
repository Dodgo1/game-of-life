# Game of life 
#### by Adam Jaskierski

A simulator of the game of life implemented in python, visualized and animated in matplotlib

### Dependencies
- matplotlib
- numpy

pipfile is provided, all can be installed using pipenv - `pipenv install`

### Usage
- #### Demo

To run the provided demo simply execute `python life.py`. Patterns from sample_patterns can be used - default is pulsar.txt
This can be changed by editing `file_path` parameter at the bottom of the file 

- #### Importing

`life.py` is a module which can be imported:
`from life import Map`

Next, when creating `Map` object either:

 - size of the map can be specified which will create an empty map, then using `Map.set_cell()` cells values can be modified
 - `file_path` of a txt file can be provided, it will be imported by the object. `empty_sign` is an optional parameter 
defining the character which corresponds to an empty space (any other character will be treated as an alive cell). 

_When creating a map file all lines must have the same number of characters!_

After creating the plane, `Map.step()` can be called manually and using `print(Map)` the plane can be viewed.

The game can also be run as an animation simply by calling `Map.animate()`, frames per second and interval can be passed
as optional parameters



