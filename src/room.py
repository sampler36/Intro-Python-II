# Implement a class to hold room information. This should have name power ups and power downs / lights_on or lights_out
# description attributes.
class Room:
    def __init__ (self, name, power_up, power_down):
            # attributes / fields
       self.name = name
       self.power_up = power_up
       self.power_down = power_down

    def __str__(self):
        # create a variable to hold the output
        output = " "
        # concatinate the name to the output
        output += self.name + "\n"
        # create an indexing variable and set it to 1
        i = 1
        # itterate over the player
        for c in self.categories:
            # the index and category name in to output
            output += " " + str(i) + "." + c.name + "\n"
            # incremement the index variable by 1
            i += 1
        output += " " + str(i) + ". Quit\n"
        # return the output
        return output

class Room:

    def __init__(self, name):
        # , products)
        self.name = name

    def __str__(self):
        return "Room closed" + self.name