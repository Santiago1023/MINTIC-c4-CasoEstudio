from abc import ABCMeta     #esto se hace porque se quiere que todos los modelos hereden de esta clase 
import json
class AbstractModel(metaclass = ABCMeta):
    def __init__(self, data) :
        for key,value in data.items():  #items() me devuelve una lista de tuplas 
            setattr(self, key, value)   # crea los atributos de cada clase y le da sus valores 

    

