
#def fun():
#   return "def fun"

#dic = {"a":fun()}
#print(fun())
#if dic["a"]!=None:
 #  print(dic["a"])
#dic = {}
#print(dic["a"])

#g = open('display/name_file11.txt')
#print(g.read())

#text = ""
#def print_web():
#        with open('name_file1.txt') as file:
#            for line in file:
#                text = line
#        if text == "":
#            return "-------"
#        else:
#            return print(text)

#print_web()

class Static:
    d = 0

    @staticmethod
    def stat():
        d = 1

class Fruit:
    name = ''

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit().printName()
Fruit().name = 'Maks'

Fruit.name = 'Maks'
Fruit().printName()