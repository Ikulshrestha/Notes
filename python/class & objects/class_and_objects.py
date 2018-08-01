class DeathNote:
   'Common Notebook for all criminals'
   killCount = 0 # empCount is class variable
 
   def __init__(self, name, cause):
      self.name = name
      self.cause = cause
      DeathNote.killCount += 1
# defining method displayCount    
   def displayCount(self):
     print("Total Deaths = %d" % DeathNote.killCount)
# defining method displayCount
   def displayCriminals(self):
      print("Name : ", self.name,  ", cause: ", self.cause)

print("DeathNote.__doc__:", DeathNote.__doc__)
 
print("DeathNote.__name__:", DeathNote.__name__)
 
print("DeathNote.__module__:", DeathNote.__module__)
 
print("DeathNote.__bases__:", DeathNote.__bases__)
 
print("DeathNote.__dict__:", DeathNote.__dict__)

