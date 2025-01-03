class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if isinstance(owner, Owner):
            self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise TypeError(f"{value} is not a valid pet type.")
        else:
            self._pet_type = value

class Owner:
    
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return list(pet for pet in Pet.all if pet.owner == self)
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of the Pet Class")
        else:
            pet.owner = self

    def get_sorted_pets(self):
        unsorted_pets = self.pets()
        return sorted(unsorted_pets, key=lambda pet: pet.name)

