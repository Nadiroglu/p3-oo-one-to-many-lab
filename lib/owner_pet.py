    
class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, new_pet_type):
        if not new_pet_type in Pet.PET_TYPES:
            raise Exception("Sorry")
        self._pet_type = new_pet_type
    
    def __repr__(self):
        return f"<Pet {self.name} {self.pet_type}"


class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Sorry")
        pet.owner = self

    def get_sorted_pets(self):
        my_pets = self.pets()
        return my_pets
        
joe_obj = Owner('joe')
fido = Pet('fido', 'dog', joe_obj)
rex = Pet('rex', 'dog')

print(joe_obj.add_pet(rex))
# print(joe_obj.pets())

print(fido)