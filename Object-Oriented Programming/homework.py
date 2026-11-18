class Dogs:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

Snowy = Dogs("Siberian Husky","White")
Rory = Dogs("Pomeranian","Golden Brown")

print(f"Snowy is a {Snowy.breed} and is in {Snowy.color} color.")
print(f"Rory is a {Rory.breed} and is in {Rory.color} color.")

