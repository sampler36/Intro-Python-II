# Implement a class to hold room information. This should have name power ups and power downs / lights_on or lights_out
# description attributes.
class Room:
    def __init__ (self, name, lights_on=True, lights_out=True):
            # attributes / fields
       self.name = name
       self.lights_on = lights_on
       self.lights_out = lights_out

    def __str__(self):
       return f"\nName: {self.name} \nLight On: {self.lights_on} \nLight Out: {self.lights_out} \n"

a = Room("Room 1", True, False)
b = Room("Room 2", True, False)
c = Room("Room 3", True, False)
d = Room("Room 4", False, True)
e = Room("Room 5", True, False)
f = Room("Room 6", False, True)


print(a)