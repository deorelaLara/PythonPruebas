import copy

class Oveja:
    def __init__(self):
        self.name = 'Dolly'
        self.type = 'equisde'

    def __str__(self):
        return '{} - {}'.format(self.name, self.type)

class Prototype:

    def __init__(self):
        self._objetos = {}

    def rObjects(self, name, obj):
        self._objetos[name] = obj

    def delateObjects(self, name):
        del self.objetos[name]
    def clone(self, name, **kwargs):
        clonedObj = copy.deepcopy(self._objetos.get(name))
        clonedObj.__dict__.update(kwargs)
        return clonedObj

sheep = Oveja()
proto = Prototype()
proto.rObjects('Sheep', sheep)

sheep1 = proto.clone('Sheep',type= 'Suffolk')
print('Information about Sheep #1: ', sheep1)
sheep2 = proto.clone('Sheep',type='Dorper')
print('Information about Sheep #2: ', sheep2)