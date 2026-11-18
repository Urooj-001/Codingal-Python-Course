class Parrot:
    species = "Bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def addition(self,a,b):
        return a+b

    

bluey = Parrot("Bluey",12)
Velvet = Parrot("Velvet",14)
result = bluey.addition(12,5)
print(result)

print("Bleu is a {}".format(bluey.species))
print("Velvent is also a {}".format(Velvet.species))

print("Bluey is {} old".format(bluey.age))
print("Velvet is also {} old".format(Velvet.age))

        