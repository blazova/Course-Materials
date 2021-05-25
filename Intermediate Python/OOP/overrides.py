class Dog():

    def __init__(self, name:str, age:int,
                 breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')
     
# TODO:   Override the __gt__ method to compare using the greater than operator

    def __gt__(self, other):
        return self.age > other.age

# TODO: Override the __str__ method to print the Dog's name instance variable

    def __str__(self):
        return self.name

if __name__ == "__main__":
    sally = Dog('Sally', 6, 'chihuahua', 7)
    henry = Dog('Henry', 7, 'terrier', 15)
    if(sally > henry):
        print(f'{sally} is older than {henry}')
    else:
        print(f'{henry} is older than {sally}')

