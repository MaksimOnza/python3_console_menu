
#def fun():
#   print("def fun")

#dic = {"a":fun(), "b":22, "c":33}

#if dic["a"]==None:
#   print(dic["a"])
#   print("second line")

#g = open('display/name_file11.txt')
#print(g.read())

text = ""
def print_web():
        with open('name_file1.txt') as file:
            for line in file:
                text = line
        if text == "":
            return "-------"
        else:
            return print(text)

print_web()