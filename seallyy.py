from random import randrange

class Pet(object):
    """A virtual pet"""
    excitement_reduce = 3
    excitement_max = 10 
    excitement_warning = 3 
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrr..."', '"Gyuuu"']
    
    def __init__(self, name, animal_type):
        self.name = name 
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]
        
    def __clock_tick(self):
        self.excitement -= 1
        self.food -= 1
        
    @property
    def mood(self):
        if self.food > self.food_warning and self.excitement > self.excitement_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"
        
    def __str__(self):
        return "\nI'm " + self.name + "." + "\nI feel " + self.mood + "."
    
    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self): 
        print(
            "I am a",
            self.animal_type, 
            " named ", 
            self.name, 
            "I feel ", 
            self.mood,
            " now.\n"
        )
        self.__clock_tick()

    def feed(self):
        print("***crunch***\n mmm. Thank you!")
        meal = randrange(self.food, self.food_max) 
        self.food += meal 

        if self.food < 0:
            self.food = 0
            print("I am still hungry!")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I'm full!")
        # else: food is within range, no message needed

        self.__clock_tick()
    
    def play(self):
        print("YAYYY!")
        fun = randrange(self.excitement, self.excitement_max)  
        self.excitement += fun 
        if self.excitement < 0: 
            self.excitement = 0
            print("I am bored")
        elif self.excitement > self.excitement_max: 
            self.excitement = self.excitement_max
            print("I am happy!")
        self.__clock_tick()

def main():
    pet_name = input("What do you want to name your pet? ")
    pet_type = input("What type of animal is your pet? ")

    my_pet = Pet(pet_name, pet_type)

    input(
        "Hello! I am " +
        my_pet.name + 
        " and I am new here!" +
        "\n♡Press enter to start♡"
    )
    choice = None 

    while choice != 0: 
        print(
            """
            ***INTERACT WITH YOUR PET***

            1 - feed ur pet (˶˃ ᵕ ˂˶)
            2 - talk to ur pet ₍^. .^₎⟆
            3 - teach ur pet a new word ᥬᩤ
            4 - play with ur pet ୭ ˚. 
            0 - quit /ᐠ - ˕ -マ
            """
        )
        choice = input("Your choice: ")   # <-- ADD THIS LINE

        if choice == "0":
            print("Good bye!☘︎")
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("What do you want to teach ur pet to say? ")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else: 
            print("Sorry, that option doesn't exist")

if __name__ == "__main__":
    main()