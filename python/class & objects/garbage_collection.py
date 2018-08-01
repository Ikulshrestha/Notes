class DeathNote:
   def __init__(self, name=0, cause=0):
      self.name = name
      self.cause= cause
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

criminal_1 = DeathNote()
criminal_2 = criminal_1
criminal_3 = criminal_1
print(id(criminal_1), id(criminal_2), id(criminal_3)) # prints the ids of the obejcts
del criminal_1
del criminal_2
del criminal_3